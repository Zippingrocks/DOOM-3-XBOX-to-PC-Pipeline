# Format findings and unknowns

## Checkpoint 042 split-script entrypoint and VM findings

An Xbox split-stage `_main.script` identifies the shared retail source file,
but it does not prove that the segment should call that namespace's `main()`.
The recovered `alphalabs1_2` and `monorail_2` sources each define a distinct
`main2()` for their second half. A PC host bridge must therefore bind the exact
map path to `map_alphalabs1::main2()` or `map_monorail::main2()`; calling the
first-half `main()` compiles cleanly while initializing the wrong stage. No
other recovered solo source defines a numbered entrypoint used by its segment.

Doom script preprocessing also applies object-like macros before resolving a
`$entityName` global. For example, `$TRAIN_ANCHOR` in Monorail resolves through
`#define TRAIN_ANCHOR monorail_anchor`. Static entity auditing must expand that
macro instead of reporting the uppercase token as a missing map entity. With
this correction, 7,193 direct references resolve locally and 974 are retained
as source-authored missing references; no source-present name is lost.

The official GPL VM distinguishes a null receiver from a null required entity
argument. An event call on a missing object/entity receiver is safely skipped
or returns the event's zero value. Supplying a missing entity to a required
event argument can instead terminate the current script thread. The
reachability report therefore classifies 334 reachable source-authored residue
records by their stock-runtime effect and keeps them as attention items. It
does not turn source-authored retail residue into a port regression, nor does
it declare every reachable use harmless without native activation.

## Checkpoint 041 direct script-entity findings

Doom script `$name` literals form a much larger entity-reference graph than
MAP target epairs or explicit `sys.getEntity` calls. After stripping comments
and strings while preserving source offsets, the solo corpus contains 8,492
active direct references across 2,627 unique map/name pairs. Of these, 7,167
resolve to decoded map entities and 325 are engine-created world/player names.

The other 1,000 are absent from the decoded source map itself and remain absent
from the overlay. This is strong evidence against conversion loss, but not
evidence that every reference is unreachable. The next static gate must build a
function call graph from each generated main and MAP callback before deciding
which shared-script references can execute in a given split segment.

## Checkpoint 040 script entity-lookup findings

Static MAP epairs are not the complete entity graph. Recovered scripts contain
225 `sys.getEntity` calls: 44 literal and 181 computed. A balanced call parser
preserves nested arithmetic and ignores commented calls. Computed expressions
are evaluated only through explicit profiles sourced from visible loop bounds,
function argument sets and map-name families; arbitrary script code is not
executed.

The domain profile covers Alpha Labs EMP/path loops, Alpha Labs 3 flare names,
Comm Outside airlocks and lift paths, CPU falling geometry, Delta light banks
and crane slots, MCU bridge/communications arrays, and Monorail beam, door and
light grids. It expands to 1,532 references and 871 unique map/name pairs. No
source-present name disappears in the PC overlay. The 408 unique absent names
are also absent in the decoded source and therefore identify retail split-map
or conservative-domain residue rather than conversion loss. Reachability is
still required before any such path can be called dead.

## Checkpoint 039 runtime-consumed reference findings

Reading the stock PC game source expands the MAP entity-reference vocabulary
beyond `target*`, `bind`, `entityname`, `killtarget` and `cameraTarget`.
`idCameraView`, `idItem`, `idObjective`, `idSpring`, `idMoveable`, elevators,
binary movers, doors and influence targets also consume `attachedTo`,
`attachedView`, `camShot`, `ent1`, `ent2`, `owner`, `visualView`,
`switchToView`, `innerDoor`, `statusGui*`, `guiTarget*`, `buddy*`, `syncLock`
and the `triggerBlocked*`/`triggerClosed*`/`triggerOpened*` families as entity
names.

Across all maps these add 95 references. Eighty-four resolve locally. Eleven
are source-authored dangling values: three objective cameras, five door buddy
or open-trigger values and three other split-stage mover references. Each
matches the decoded source by source entity, origin, key and target. None is
silently retargeted.

## Checkpoint 038 PC entity-name and link findings

PC entity lookup is case-insensitive. `idGameLocal::AddEntityToHash` rejects an
existing name, while `FindEntity` compares candidate names with `idStr::Icmp`;
`GetTargets` resolves target values through that lookup. See the official
[id Software Doom 3 source](https://github.com/id-Software/DOOM-3/blob/master/neo/game/Game_local.cpp#L3046-L3152).

The Xbox solo corpus contained three case-only pairs. Alpha Labs 2 had two
lowercase/camel-case `info_vacuumseparator` marker pairs with no authored name
references. The lowercase exact-origin entities now use `_split` suffixes.
Delta 2A had two differently cased `target_endlevel_1` exits, each with its own
trigger; the second entity and its unique trigger target now use `_secondary`.
No entity is removed and both transitions still select `vv/delta2b_2`.

The campaign has 14,605 explicit `target*`, `bind`, `entityname`, `killtarget`
or `cameratarget` values. 13,000 resolve to a named entity and 16 are engine or
empty sentinels. The other 1,589 are identically dangling in the decoded retail
source when matched by entity, origin, key and value. This distinguishes
source-authored split-map residue from conversion regressions without inventing
targets. Native activation remains the authority on whether any retained
source residue affects gameplay.

## Checkpoint 037 solo semantic and audio findings

The segmented solo campaign forms one closed directed chain across all 41
decoded maps. It begins at `mars_city1_1`, terminates at `hellhole_2`, has no
external destination and visits every segment exactly once. One retained stock
`game/delta2b` destination in the second Delta 2A exit was a real PC-port leak;
both exits now converge on the only decoded Xbox successor, `vv/delta2b_2`.

Callback lookup must be entity-aware. `target_callobjectfunction` values name
script-object methods rather than global map functions, and localized callback
`#str_02680` resolves to `map_comm1::airlock_door1_open`. After those semantics,
403 calls resolve to namespaced functions and two to object methods. The MCU
inner-elevator door had one unqualified `elevatorDoorsHide` call even though the
function lives in `map_mc_underground`; the same MAP already provided a fully
qualified witness. Four unresolved callbacks are retained stock-PC-identical
warning/no-op remnants. Two Alpha Labs 2 relays instead belong to absent
texture-separator logic from the unsplit authoring map; neither functions nor
targets exist in the recovered segment, so their exact epairs are made inert.

Direct audio is not closed by declaration scanning. The final MAP corpus has
3,891 active direct-WAV references representing 2,739 unique map/path pairs.
Stock PC packages satisfy 2,320 pairs through WAV or transparent OGG fallback.
The remaining 419 route through each map's 14,150-byte INDEXLIST and XSB into
the bounded retail global XWB; decoding produces 171,347,256 bytes of PCM WAV
data across 39 maps. Every decoded WAV is copied into its consuming overlay and
rehashes against both the XACT and overlay receipts.

Twelve `inner1.wav` door-open values have a unique `inner_1` correction: the
Xbox XSND and PC packages contain only that spelling and the same entities
already use it for `snd_close`. Fifteen other speaker values have no XSND entry,
no shared or map GFC member and no PC WAV/OGG. They are retained as explicit
silent remnants, not fuzzy-matched to similarly named audio.

The final 41-map overlay corpus has 1,787 payload records and 780,869,086 bytes.
Its manifest ledger is
`a99b35fe5bfbf85c5a617be76f38082e752748f7489b5a7d3c9562d7df44cdf3`
and its payload ledger is
`d6756e9cf3a40cb4c934ab2efbe3a33538f6f492ed942934f7583bbc335bc22b`.
These checks prove static routing and packaged audio coverage, not that every
event fires at the right time or sounds correct in native play.

## Checkpoint 036 solo overlay findings

The same deterministic overlay builder used for co-op can package the 41 Xbox
solo segments without borrowing stock PC map geometry. Each segment supplies
decoded `maps/vv/<segment>.map`, `.proc`, every shipped `.aas*`, direct authored
`.cm`, its decoded MDV/MD5 corpus and its recovered portable source files. The
solo namespace keeps generated materials, declarations and strings separate
from the co-op runtime namespace.

Xbox split-stage scripts are not directly loadable by the PC map loader. Each
retail `<segment>_main.script` includes one or more map source files, while the
actual `main` lives in exactly one namespace. A generated global
`maps/vv/<segment>.script` includes the same recovered sources and calls that
namespaced main. This contract succeeds for all 41 segments, including the
multi-include `alphalabs2_2` case; it does not synthesize gameplay logic.

Five classname families required evidence-scoped handling:

- Admin's `func_spawner_1` is the same unregistered retail orphan already
  established in co-op and remains a named inert target.
- Seven `particle` entities have no Xbox entityDef/XBE class, no
  `particle_model` key in the XBE and no referenced `.particle` members in the
  map/shared archives. They are exporter remnants, not guessed PC emitters.
- `alphalabs2_1` and `delta5_1` each contain one brush `func_moveable`. The
  stock PC Alpha Labs 2 map contains the same-origin brush entity as
  `moveable_base`, whose declaration selects `idMoveable`; both Xbox entities
  retain their authored render and collision models under that PC class.
- The silent `sound_lightsout_shutter` entity is spawnarg-equivalent to the
  unregistered, unreferenced orphan shipped in stock PC `mars_city2.map`; it
  remains named and inert rather than inventing a shader.
- `mars_city1_1` contains one editor label serialized as a classname. Its
  exact classname/name/origin-only entity remains inert while the adjacent
  real `info_location` remains unchanged.

The strict corpus audit rehashed all 1,368 payload receipts and all 41
manifests. No payload was missing or changed, all collision sources are
`direct-authored-cm`, and unresolved classname/resource/string totals are zero.
This proves deterministic packaging and declared dependency closure, not
native loader, timing, audio playback, transition or visual fidelity.

## Checkpoint 024 offline findings

`xc_delta2b_2` decodes to a 3,974,751-byte MAP with geometry CRC `3474151774`,
a 5,612,977-byte PROC and a 5,645,593-byte direct PC CM. The authored collision
set has 229 models, 25,808 vertices, 45,113 edges, 18,935 polygons, 3,462
brushes and 8,629 nodes. The MAP has 47 named `func_static` entities carrying
`noclipmodel 1`, none present in authored CM. They predict the independently
compiled additions but do not substitute for a later dmap audit.

Corrected AAS48 has 849 areas, 3,558 reachabilities and 2,759 nodes with full
nonzero coverage. The decoded PROC has 91 areas and 101 portals. The archive's
343-file model set contains 11 meshes, 242 MDV animations and 90 MD5ANIM.X
animations; every file decodes.

The map independently confirms the checkpoint-023 ZCT compatibility contract.
Its `head_butt.mdvanim` has the same raw SHA-256, while three commando entities
select the DEF that references it. The 63-joint retarget is therefore a direct
reuse of identical source bytes. The retail map script is present, and the only
MAP `call` value has one definition. No empty-script transform is applied.

Direct sample closure can also be established before native loading. Of 68
unique direct `.wav` paths in the retail MAP, 63 have stock PC `.wav`/`.ogg`
media. Four of the remaining paths route through the map's 14,150-byte
INDEXLIST and 28,724-byte XSB into the global XWB, yielding 1,420,036 bytes of
PCM WAV data. The last spelling, `inner1.wav`, is absent from both Xbox XSND
and stock PC while `inner_1` exists in both; it occurs in exactly two
`snd_open` epairs whose same entities already use `inner_1` for `snd_close`.
The exact paired transform leaves 67 unique post-transform paths, all covered.

## Checkpoint 023 tenth-segment findings

`xc_delta2b_1` extends the direct-CM contract to a tenth co-op segment. Its
3,291,335-byte decoded MAP has geometry CRC `4216080146`; the 1,726,149-byte
CM.X expands to a 2,677,242-byte PC CM containing 238 models, 12,857 vertices,
20,711 edges, 7,914 polygons, 3,068 brushes and 7,390 nodes. Independent PC
`dmap` emits 295 models. All 238 authored names are shared, and each of the 57
PC-only names belongs to a MAP entity carrying `noclipmodel 1`.

Corrected AAS48 has 698 areas, 3,361 reachabilities and 2,532 nodes, with no
unreachable nonzero node or unreferenced nonzero area. The archive has no AAS96
or second navigation class. The decoded PROC has 4,679 BSP nodes, 1,965
surfaces, 49,404 vertices and 133,152 indices; its 70 areas and 74 portals match
the independently PC-dmapped portal geometry exactly.

The selected model set is 437 files: 15 MDV meshes and 422 animations. This
segment exposes a PC-skeleton compatibility case rather than a corrupt Xbox
asset. Xbox `head_butt.mdvanim` and its ZCT mesh have 50 joints; the stock PC
ZCT mesh has 63. Direct copying therefore fails the PC joint-count invariant,
while replacing the complete PC ZCT set with the Xbox set breaks the stock AF
at `Lindex3`. The expansion retarget keeps Xbox world-space animation on every
shared joint, fills the 13 PC-only joints from the target bind pose, and
accounts for the inserted `joint12` parent before emitting a 63-joint,
378-component animation.

The remaining location issue was geometric, not a binary PROC defect. Stock PC
Delta 2B places portal 37 on `y=-608`, covering `x=1568..1824`; Xbox co-op
places portal 31 on `y=-557`, covering `x=1600..1792`. The MAP retained the
stock separator origin `1694 -608 84`. `idLocationSeparatorEntity::Spawn`
searches an origin expanded by only 16 units, so the 51-unit offset cannot find
the Xbox portal. Independent PC `dmap` preserves the Xbox portal and reproduces
the warning. The exact transform to `1694 -557 84` is therefore tied to two
independent geometry witnesses and fails closed on any entity/origin mismatch.

## Checkpoint 022 ninth-segment findings

`xc_recycling2_1` extends the direct-CM contract to a ninth co-op segment. Its
3,783,693-byte MAP has geometry CRC `1305987032`; the 2,294,941-byte CM.X
expands to a 3,515,885-byte PC CM containing 105 models, 16,998 vertices,
28,366 edges, 10,972 polygons, 2,996 brushes and 10,497 nodes. Independent PC
`dmap` emits 209 models. All 105 authored names are shared, and each of the 104
PC-only names belongs to a MAP entity carrying `noclipmodel 1`.

This archive demonstrates a second navigation class. Corrected AAS48 has 1,087
areas, 4,759 reachabilities and 3,697 nodes. The shared retail archive carries
the map's separate `aas_mancubus.x`; its corrected export has 126 areas, 299
reachabilities and 521 nodes. Both files have complete nonzero BSP/area
coverage, and the native run emits no Mancubus AAS warning after both are
staged.

The selected model set is 341 files: eight meshes, 246 MDV animations and 87
MD5ANIM.X animations. All decode. Twenty-nine runtime WAVs route through the
map's 14,150-byte INDEXLIST and 30,800-byte XSB to the original global/memory
XWB banks; decoded WAV payloads total 10,514,246 bytes.

The segment also establishes a strict boundary for missing-art handling. The
retail breakable-light convention requests `recycwallight_broken.ase`, but the
file is absent from Xbox co-op, Xbox solo and stock PC inventories, and the
stock PC Recycling 2 run reproduces the warning. `guisurfs/hazard1:1` is also
reproduced by the stock run. The shared retail material
`textures/base_door/a_deldoorgutter_d02` references three image stages. Its
exact 64x128 diffuse image is recovered from Xbox D3TFULL key `3D1761C9` as a
5,584-byte DDS with SHA-256
`e1a5206cf6a0313c14e7facd90c016852bdc73e5e108d1c8a31420d8d6fc872f`.
The normal and specular images are absent from both Xbox D3TFULL and stock PC
packages. Those two are recorded as source absences; no nearest-name texture
substitution is treated as fidelity.

## Checkpoint 021 eighth-segment findings

`xc_enpro_2` confirms the EnPro contracts independently: direct CM.X has 163
models and PC `dmap` adds only six MAP-authored `noclipmodel 1` models; corrected
AAS48 has 929 areas, 5,167 reachabilities, 2,885 nodes and complete nonzero
coverage. Its 321-file model set decodes fully. Eleven runtime WAVs route
through the distinct `xc_enpro_2` INDEXLIST/XSB into the shared XWB banks. The
same stale `setupCoop` pattern appears here with its only source body commented,
providing a second exact witness for the path-scoped callback transform.

## Checkpoint 020 seventh-segment findings

`xc_enpro_1` extends the direct-CM contract to a seventh co-op segment. Its
3,626,728-byte MAP has geometry CRC `2226283201`; the 3,240,749-byte CM.X
expands to a 5,495,477-byte PC CM containing 182 models, 24,495 vertices,
42,569 edges, 17,196 polygons, 3,029 brushes and 12,040 nodes. Independent PC
`dmap` emits 208 models. All 182 authored names are shared, and every one of
the 26 PC-only names belongs to a MAP entity carrying `noclipmodel 1`.

The corrected AAS48 has 1,112 areas, 5,319 reachabilities, 3,834 nodes and no
unreachable or unreferenced nonzero records. The archive has no AAS96. All 315
selected map-local model files decode: ten meshes, 231 MDV animations and 74
MD5ANIM.X animations. The shared 48-joint skeleton is now byte-identical across
four independently recovered segment archives.

EnPro demonstrates why a clean model/GUI closure is insufficient for campaign
fidelity. Sixteen referenced sounds must be routed through four independent
Xbox layers: the global XSND name table, `xc_enpro_1.indexlist`, the segment
XSB cue table and the global/memory XWB wave banks. Their decoded PCM payloads
total 5,535,714 bytes. The additional `monster_demon_maggot_sight2` name is not
in the Xbox XSND or archive inventories, so the exact optional DEF epair is
disabled rather than mapped to a guessed vocalization.

The retail MAP calls `setupCoop`, but its only source body is block-commented;
disabling that one stale epair preserves the trigger and its other targets.
Retail `func_explodable` also spells a particle extension `.ips`; other Xbox
declarations and stock PC use the shipped `.prt`, giving an independent exact
correction witness. With these receipts, the recovered XACT audio and the exact
`lights/nofalloff` DDS, native true `COOP` spawns 709/0 with no map-specific
warning or missing resource.

## Checkpoint 019 sixth-segment findings

`xc_alphalabs2_2` extends the direct-CM contract to a sixth co-op segment. Its
3,787,497-byte MAP has geometry CRC `3745531086`; the 3,298,539-byte CM.X
expands to a 5,784,631-byte PC CM containing 147 models, 24,551 vertices,
43,280 edges, 18,742 polygons, 2,719 brushes and 9,801 nodes. Independent PC
`dmap` emits 261 models. All 147 authored names are shared, and every one of
the 114 PC-only names belongs to a MAP entity carrying `noclipmodel 1`.

The corrected AAS48 hashes to
`f56dd1520d36f818bb780fdb05286b0f1053dbb42996eebac7e0f8c389d148f9`
and has no unreachable or unreferenced nonzero records. There is no AAS96 in
the map archive. Together with decoded PROC and direct authored CM it reaches
native true `COOP` without a path failure.

The map-local selected model set is 299 files: eight meshes, 217 MDV animations
and 74 MD5ANIM.X animations. Every file decodes with a receipt. The 48-joint
skeleton is byte-identical to copies recovered independently from
`xc_mars_city1_1` and `xc_mcu`, strengthening the shared-skeleton identity
contract across three archive boundaries. This map needs no new compatibility
transform; inherited transforms close the runtime dependency graph exactly.

Native loading spawns 764 entities and inhibits two. These are not lost
entities: `ammo_clip_large_27` and `item_armor_security_8` are player-two
pickups whose retail MAP declarations set both `not_medium 1` and `not_hard 1`.
The default medium run therefore proves the retail difficulty gate is being
honored. Mutating those epairs merely to obtain a 766/0 count would reduce
fidelity. With the retail flags intact, the bounded run has no map-specific
warning, missing resource, invalid joint, callback, class, navigation, error or
fatal line.

## Checkpoint 018 fifth-segment findings

`xc_mcu` extends the direct-CM contract to a fifth co-op segment. Its
3,223,941-byte MAP has geometry CRC `2327495450`; the 2,175,464-byte CM.X
expands to a 3,537,686-byte PC CM containing 212 models, 16,053 vertices,
28,045 edges, 11,270 polygons, 2,322 brushes and 8,604 nodes. Independent PC
`dmap` emits 228 models. All 212 authored names are shared, and every one of
the 16 PC-only names belongs to a MAP entity carrying `noclipmodel 1`.

The corrected AAS48 hashes to
`4b1bf8e5d89af1a013beb97de01868eaccc4ef07a20f1baa1c63f1732b37c0eb`.
There is no AAS96 member in this map archive. Together with decoded PROC and
direct authored CM, AAS48 reaches native true `COOP` with 811 entities spawned,
zero inhibited and no path failure.

Dependency-driven extraction alone can understate the authoritative Xbox
skeleton set. The MCU GFC contains 410 MDV members—19 meshes and 391
animations—and every one decodes. The 48-joint skeleton is byte-identical to an
independent first-segment recovery. The Xbox pruner removes identity-only
terminal finger joints from the 48-joint labcoat, 44-joint pistol-zsec and
42-joint shotgun-zsec meshes while retaining predecessors in the same chains.
The corresponding stock PC AF endpoints therefore require exact, path-scoped
aliases. Each expected endpoint occurs twice; any different count is a source
identity failure, not permission for a broad text replacement.

The security co-op GUI declares `ContentClipLocker` but two early transitions
refer to nonexistent `ContentClipLocker2`; later duplicated transitions already
target the declared window. Redirecting exactly those two references fixes the
retail defect without inventing a window. The MAP likewise places two identical
`#str_02859` location entities eight units apart in one portal area. Keeping
`info_location_9` and making only `info_location_11` inert removes PC's overlap
warning while preserving the location and all geometry.

`lights/spot08` is stored in global D3TFULL under key `06EFB410`. It decodes as
a 64×64, five-mip DDS with SHA-256
`6f07805e4367a6fa7fd3d430852e60358a69908a9d1a18b3b318e1ffb14326ea`.
Stock PC already declares the same image path, so the final closure keeps that
declaration and copies only the exact Xbox DDS. Staging the Xbox material body
as well creates a redundant-declaration warning and is rejected. With the
complete MDV set, three AF aliases, the exact GUI and location corrections and
this image, the native map slice has no map-specific missing-resource,
invalid-joint, callback, class, navigation, error or fatal line.

## Checkpoint 017 fourth-segment findings

`xc_admin` independently extends the direct-CM contract to a fourth co-op
segment. The 2,107,679-byte MAP has geometry CRC `25560181`; its 1,282,663-byte
CM.X expands to a 1,929,264-byte PC CM containing 199 models, 10,449 vertices,
16,170 edges, 5,959 polygons, 2,054 brushes and 5,507 nodes. PC `dmap` emits 238
models. All 199 authored names are shared, and every one of the 39 PC-only names
is a MAP entity carrying `noclipmodel 1`.

This map requires both corrected navigation families: the 824,144-byte AAS48
hashes to `ab4194f0e152ea40cccbbfa4392a53783a4b48dbb7ce51cda7a0e3c41df3f41d`
and the 208,113-byte AAS96 hashes to
`b2ae58682ec87bd2fa42b22adb0081cf041d1fd73e4732fddbcf754dd2ac8a0c`.
Both load natively. `admin_wounded_marine` deliberately sets `use_aas` to an
empty string in Xbox and stock PC data; its warning is not evidence of a missing
navigation payload and assigning one would change a prone scripted NPC.

The admin GFC supplies 37 Pinky/zjump/combo MDV files. The decoded Pinky mesh
contains `Waist` but not `LoNeck`, exactly matching the exporter directive that
renames `LoNeck` to `Waist`; the Xbox DEF's residual `look_joint LoNeck` is
therefore inert and is disabled by an exact transform. The stock PC chainsaw AF
instead requests `Rfings3/Lfings3`, which do not exist in the decoded zjump
mesh. The retail Xbox AF is the authoritative fix: it uses `Rindex1/Lindex1`
and removes every invalid-joint warning without modifying the mesh.

The lone map entity named `func_spawner_1` has no matching declaration in the
retail Xbox DEF corpus, no `idSpawner`/`idFuncSpawner` registered XBE type and no
equivalent entity in stock PC admin; only dangling target names remain there.
Staging it as stock inert `target_null` preserves identity and target wiring
without inventing behavior. Likewise, `map_admin1::setupCoop` has no body in the
retail admin script closure, while related co-op scripts retain matching bodies
only as comments. The call is disabled and the absent map script is represented
by a minimum empty PC `main` entry point.

The Xbox D3T contains `leftframe_d`, `id_badge` and `id_gui`, but contains no
`leftframe_s`, `leftframe_local`, `id_badge_s` or `id_badge_local`; stock PC PK4
data omits the same four images while retaining stale stages. Exact transforms
on the native Xbox material paths disable only those unshipped stages. The final
native run has no missing image, model, animation or sound line and no unknown
joint, callback or class line.

## Checkpoint 016 third-segment findings

`xc_mars_city2_2` confirms the direct-CM contract on a third co-op segment.
The 1,746,525-byte MAP has geometry CRC `2356338129`; the 966,528-byte CM.X
expands to a 1,526,425-byte PC CM containing 129 models, 7,205 vertices,
11,941 edges, 4,663 polygons, 1,563 brushes and 3,987 nodes. Independent PC
`dmap` emits 171 models. All 129 authored names are shared, and all 42 PC-only
names belong to MAP entities marked `noclipmodel 1`.

The corrected AAS48 hashes to
`bf118f9643843b369c6de0c371356aa4150b1509c6c5c2baf951c7ec4bba8657`.
Together with decoded PROC and direct authored CM, it reaches native true
`COOP` with 516 entities spawned, zero inhibited and no path failure.

The only new runtime asset was `lights/nofalloff`. It is not a loose GFC file;
the Xbox global D3TFULL resolves the logical-name key `9704C74E` to a 16×16,
three-mip DDS. Its payload SHA-256 is
`1d632a0e7b695186ed6462ff026215fe4bf217c6a57370a5bb9c9dfdd775e11b`.
Because stock PC `materials/lights.mtr` already contains the material body, the
correct integration copies only `dds/lights/nofalloff.dds`. Emitting an Xbox
material body as well causes a duplicate-declaration warning and is rejected.

## Checkpoint 015 second-map closure findings

Checkpoint 014 selected the 691,857-byte AAS48 with SHA-256
`9778ae62f8d9e937afa7d89bc1e4a856dcf6ceac2e97daf8f926ae93dfa908a9`.
That file predates the established packed-plane distance correction. At the
only native path failure observed after player creation, both the zsec origin
`(-956,-1456,128.25)` and `path_corner_28` at `(-808,-1472,128)` resolve to
area zero. It is rejected, not an alternate acceptable navigation payload.

The corrected export has SHA-256
`6e9f0b2cbd8981c3117cb20e029d390c4aa792fd449aad64ae3d241f0f70338e`.
The route auditor resolves the same endpoints to areas 41 and 34 and finds the
six-area route `41→39→38→37→35→34` under travel flags `0x400002`. Native Doom 3
then emits neither the path warning nor a failed `XBOX_COOP_PATH_DIAG` line.

The inherited player closure is now separated from map-specific assets. The
229-entry `xbox_coop_player.resources` profile contains shared player AF, HUD
DDS, body/head meshes, player animations, weapon view/world animations and two
player weapon loops. It deliberately excludes the first map's NPC, dialogue,
ambient and cinematic data. This removes every checkpoint-014 player model,
animation, AF, HUD and `Hips`-joint failure.

`guis/assets/hud/items/armor_shard.tga` is absent from all recovered campaign
and multiplayer GFC inventories and both shared-assets inventories. The stock
PC `item_armor_shard` likewise omits that icon. The overlay transform therefore
comments only the exact `inv_icon` epair on 15 affected city2 entities and
records input/output MAP hashes; classname, model and pickup behavior remain
unchanged. With corrected AAS, this closure and the checkpoint-014 control-flow
guard, the native run spawns 1,110/0, joins the player, and reports zero
missing-resource, skeleton, path, error or fatal lines.

## Checkpoint 014 second-map and instant-hit findings

`xc_mars_city2_1` independently reproduces the direct-CM export contract. Its
3,573,456-byte decoded MAP has geometry CRC `3219770337`; its 1,833,167-byte
CM.X expands to a 2,927,667-byte PC CM with 219 models, 13,620 vertices,
22,574 edges, 8,708 polygons, 2,984 brushes and 7,651 nodes. The independent
PC-`dmap` CM has 312 models. Every authored name is shared, and every one of
the 93 generated-only names belongs to a MAP entity marked `noclipmodel 1`.
No generated-only model remains unexplained by that authored omission flag.

The map, direct CM, decoded PROC and decoded AAS48 all reach the native PC
loader. Entity spawning initially fails at `gamex86.dll+0x10caf0`, whose body
is `mov eax,[ecx+0x248]; ret`; the captured context has `ecx == 0`. The caller
at `gamex86.dll+0x22c48` is the unguarded `projectile.GetEntity()->GetPhysics()`
probe in `idAI::Spawn`. The reconstructed `idAI::CreateProjectile` at RVA
`0x16b70` explicitly returns null when `projectileDef` has `net_instanthit 1`.
The first affected map entity is `monster_zsec_machinegun_9`.

This was cross-checked without accepting an asset mutation. Setting only the
machinegun projectile's flag to zero in a temporary local overlay moves the
fault to `monster_zsec_shotgun_2` at the same instruction. Setting all selected
instant-hit flags to zero allows all 1,110 entities to spawn, inhibits none,
joins the local player and exits 0. Therefore the conversion must retain the
Xbox declarations and fix the source integration: `idAI::Spawn` must tolerate
the intentional null result, keep `projectileRadius` zero for that path, and
still derive velocity/gravity/speed from the entity definition.

An independent control-flow diagnostic patched only the eight bytes after the
`CreateProjectile` call: test the returned pointer, skip the physics/bounds
probe on null, otherwise use the returned entity directly. With all original
Xbox `net_instanthit 1` values intact, it also spawned 1,110/0 and exited 0.
The base DLL SHA-256 was restored exactly after the run. This validates the
source change's control flow but is not a distributable or accepted binary.

The 50-file second-map closure is not accepted merely because its manifest has
zero unresolved names. The native run reports a missing ladder animation,
seven HUD item images, a defaulted `model_sp_marine`, and a player `Hips` joint
error. Those are inherited co-op-player dependencies not rooted by the current
map-only closure. They are the next packaging obligation after the gameplay DLL
guard is rebuilt and verified with the original `net_instanthit` values.

## Checkpoint 013 authored-CM overlay findings

The runtime-overlay builder can now select a direct CM.X export with
`--authored-cm`. The ordinary PC-compiled map set remains mandatory so the
authored payload cannot bypass the independent geometry build. Before staging,
the builder requires the authored basename to match the converted map stem,
parses both files as ASCII PC `CM "1.00"` text, and compares their embedded
map CRCs. It removes the generated staged CM only after those checks and records
both collision receipts in the manifest. Any failure removes the staging tree
and publishes no partial overlay.

For `xc_mars_city1_1`, the generated CM is 4,588,408 bytes with SHA-256
`2a62ec67934e572fc0f1fed3fec572f712f103e2252eb889724f781c51daff3a`;
the authored CM is 3,320,995 bytes with SHA-256
`35a8ebff563a9d449995c02a90f1e822aa9dfeb42ec289b0128b8b1132cd8931`.
Both declare map CRC `2410032894`. The finalized overlay has the same 374-path
file set as the generated-CM baseline; its only intended functional payload
change is the CM. Material declaration bodies are unchanged, and provenance
comments now use material-relative paths plus source hashes so caller path
spelling cannot perturb the receipt.

The resulting overlay enters the native true-`COOP` loader and spawns all 940
entities with zero inhibited entities, errors, fatals or missing-resource
warnings. This establishes faithful CM selection and loader compatibility, not
moving collision, trigger dispatch, two-peer behavior or gameplay equivalence.


## Checkpoint 012 live-entity collision findings

`xboxCoopCollisionDigest` now accepts `@entity` targets. The command resolves
a spawned entity's live clip model and queries it with its runtime origin and
axis. Its input digest binds the requested and resolved identities, mask, hull,
origin, full axis, local and absolute bounds, clip contents and link/enable
state, count, seed and raw coordinate bits. Numeric handles remain visible for
diagnosis but are excluded from the digest because equivalent models occupy
different handle slots in the two CM files.

Three generated/authored pairs produced 24,576 records with matching input
digests and coordinates. `doorClip_1` resolves at
`-2560 -1708 212`; `trigger_coop_enablegui_2` at
`-320 -3016 40`; and `func_static_53167` at `64 -1440 218`. All are
linked and enabled under both CMs, and all paired records agree on hit/no-hit.

The equality stops there. The door has 1,067 swept-box contact differences and
the co-op trigger has 800, despite exact point traces and stopping trajectories.
The live static has 1,500 contact differences, 11 point start-contents/skip
differences, one trajectory difference and 97 material-selection differences.
Those material pairs are generated `gotsilvercol1` versus authored
`stesilverswatch`; both names are present in the recovered MAP, so the result
reflects different collision/contact selection rather than a missing material
translation.

Across the three profiles there are 3,393 gameplay and 3,623 stable-topology
mismatches. This confirms the checkpoint-011 named-model result at actual
spawned placements: PC `dmap` preserves broad blocking for these samples but
does not preserve the Xbox-authored contact representation. Direct CM.X export
is therefore the fidelity path. It remains an inference relative to Xbox
hardware until an original-Xbox runtime oracle is available.

## Checkpoint 011 named-model and gameplay-mask findings

`xboxCoopCollisionDigest` now accepts an explicit loaded collision-model name,
numeric contents mask and optional six-float trace hull. It resolves the model
before tracing and rejects a missing name rather than inheriting handle zero.
The input digest binds model name, mask, hull, model bounds, count, seed and raw
coordinate bits. This is necessary because coordinate equality alone cannot
prove that two logs exercised the same gameplay semantics.

Five first-map profiles each produced 8,192 generated/authored record pairs,
for 40,960 total. Every summary input digest and coordinate stream matches,
there are no missing records and no hit/no-hit mismatch. Point geometry agrees
throughout. World `MASK_MONSTERSOLID` with the default actor hull exposes 22
box-trajectory, 216 box-contact and 251 metadata mismatches. World
`MASK_SHOT_RENDERMODEL` with the recovered `projectile_rocket` hull exposes
25 trajectory, 97 contact and 624 metadata mismatches.

The named models sharpen the interpretation. `doorClip_1` with the player mask
and `trigger_coop_enablegui_2` with trigger contents have identical start
classification, execution sets, hits, stopping fractions/endpoints, normals,
contents and materials. Their swept-box contact points/planes still differ in
1,065 and 767 rows. Thus `dmap` preserved broad blocking for those simple
brushes but rebuilt a different contact manifold. Polygon-only
`func_static_52977` differs more materially: 74 stopping trajectories and 596
contact manifolds differ. All named point traces remain geometrically exact.

Across the matrix, the non-equivalence totals are 121 trajectory, 2,741 contact
geometry, 875 material/contents and 3,507 gameplay mismatches. These are not an
Xbox-runtime comparison: both inputs run through the PC collision engine.
They isolate the payload difference and show why the direct authored CM is the
only fidelity candidate. Live transforms, mover motion, trigger dispatch,
projectile orientation and actor-specific axes remain separate runtime gates.


## Checkpoint 010 native collision-trace findings

The first direct CM.X export and the independent PC-`dmap` CM were loaded by
the same PC collision engine and queried with the same deterministic stream.
Each run produced 4,096 point and 4,096 player-box records. Both report world
bounds `(-4032,-3864,-72)-(360,-784,640)`, input digest `8386c90c`,
8,192 paired rows, identical executed/skip sets and identical hit/no-hit
outcomes. This controls the comparison for the host algorithm and isolates the
collision-data difference.

Point-ray geometry is identical within the declared tolerances across all 4,073
executed pairs. Player-sized swept boxes are not: 265 of 3,929 pairs differ in
contact geometry, including 54 movement fractions/endpoints, 39 normals and 114
plane distances outside tolerance. The maximum endpoint delta is 416 map units.
Across both shapes, 501 contacts choose different material or contents metadata;
385 of those retain matching geometry. Ten contents values differ.

The diagnostic hashes fractions, endpoints, contact points/planes, contents and
materials as gameplay results. It hashes stable edge/vertex feature identifiers
separately as topology. Doom 3's `CONTACT_TRMVERTEX` path stores a polygon
pointer cast to `int`; that value changes with process address layout and is
therefore normalized to zero rather than mislabeled as topology. The point
contents fast path also returns a raw first-brush contents value without applying
its requested mask; the diagnostic applies `SOLID|PLAYERCLIP` explicitly
before deciding whether a translation start is safe.

The result is not evidence that PC `dmap` is wrong for the PC map. It is
evidence that regeneration is not behaviorally identical to the Xbox-authored
collision data and therefore cannot serve as the fidelity payload. Direct CM.X
recovery is required. An original-Xbox runtime oracle, entity models, movers,
triggers, projectile/monster masks and remaining-map traces are still open.



## Checkpoint 009 CM.X collision findings

Xbox CM.X is a compact little-endian serialization of runtime collision data.
The file begins with a model count. Each model carries its name, bounds,
contents, convex flag, vertices, 16-byte edges, a shared plane table, brushes,
polygons and a preorder BSP. Brush sides and polygons reference the shared
plane table. BSP nodes carry their original polygon/brush reference lists.
Internal edge normals, primitive numbers, aggregate allocation counters and
node references are runtime metadata; standard PC CM 1.00 text does not encode
all of them and reconstructs its caches from collision geometry plus BSP planes.

As with AAS.X, each packed plane stores internal `idPlane.d`. PC CM text stores
`idPlane::Dist() == -d`, so both polygon and brush plane distances must be
negated on export. Edge records accept two observed flag states (ordinary and
internal) and two observed reserved-field states (world/static and convex trace
models). The decoder rejects unknown flags, bad indices, unsafe names, malformed
node preorder, duplicate model names, non-finite values, truncation and trailing
bytes. Empty brush materials are legitimate in 258 extracted records because PC
CM brushes export numeric contents; no polygon material is empty.

A deterministic corpus audit parsed all 1,200 extracted CM.X members, representing
391 unique SHA-256 payloads and 66,076,100 stored bytes. Across all members it
validated 4,813 models, 428,453 vertices, 792,130 edges, 294,185 planes, 50,693
brushes, 356,793 polygons and 381,933 BSP nodes. Every collision primitive is
reachable from at least one Xbox BSP node, no node repeats a primitive reference,
and no bytes remain unconsumed. The corpus receipt SHA-256 is
`838535f1924ffa89f15bfbfb8397b705fe1178cc74ac01e88a46e6bbc974762f`;
its path-and-payload manifest digest is
`a4e1fd30551a26de22310c7c13085b527d9cd5e7fdbdeb35ef11a1791c3779ca`.

A separate export audit computes each paired converted MAP's geometry CRC using
the GPL `idMapFile::SetGeometryCRC` contract, expands the matching map CM.X
in memory and records the resulting PC CM hash without retaining licensed
outputs. All 20 co-op map CMs export: 43,791,272 CM.X bytes become 71,372,306
PC CM bytes across 3,633 models, 329,260 vertices, 562,201 edges, 50,435
brushes, 224,733 polygons and 182,879 nodes. The MAP/CM.X/output manifest digest
is `3a27835c398b2d5c9bd280a29c397efe47868ea965ae4d9f9900fa2755cf0603`;
the JSON receipt SHA-256 is
`af213e9f7825973f5e02920c00d65a2df2bc97a876dcfdf7d088295546340609`.

The first co-op segment's 2,003,187-byte CM.X has SHA-256
`bbfe12d231e229279757fe6b48fe13490cd0cc4dc6f7db44bd30f82c19b034a5`.
With the converted MAP geometry CRC `2410032894`, it expands to a
3,320,995-byte standard CM with SHA-256
`35a8ebff563a9d449995c02a90f1e822aa9dfeb42ec289b0128b8b1132cd8931`.
An independent PC `dmap` CM contains 277 model names. All 243 authored CM.X
names are present in that set; the 34 PC-only names map exactly to 34 recovered
MAP `func_static` entities marked `"noclipmodel" "1"`. There are no
authored-only or unexplained names. This explains the model-count difference as
intentional non-collision metadata rather than missing authored CM records; the
model-set receipt SHA-256 is
`45cf2b16e579e439ec5172ea533998780818b97be39fa1d2b038a8015078bf13`.

The PC engine loaded that file directly in 29 ms as 243 models, 15,146 vertices,
25,468 edges, 10,005 polygons, 2,784 brushes and 7,167 nodes, then spawned all
940 map entities and exited normally. The log SHA-256 is
`c56451c2e4bff8cbfc6185504baa9a98a08d71c8a16ea4bdeafe2eed09dd6d08`.

The PC loader reconstructed all 9,237 Xbox brush-node references. It constructed
21,999 polygon-node references versus 22,341 references stored in the packed
Xbox BSP. Reference-list placement is an acceleration structure rather than
collision geometry, but the difference prevents a claim of proven trace
equivalence. Matched trace sampling, movers/triggers, actor contacts and native
loading for the remaining maps are required before collision fidelity can be
accepted.

## Checkpoint 008 AAS plane serialization findings

Xbox AAS.X `xboxData` stores each plane as the engine's in-memory
`idPlane` vector `(a, b, c, d)`, whose signed side test is
`normal dot point + d`. Standard PC AAS text stores `idPlane::Dist()`,
which is `-d`; the PC loader reads that value through `SetDist` and restores
the internal fourth component as its negation. The original exporter copied the
packed fourth float directly into PC text, thereby reversing every nonzero BSP
plane distance when the PC engine loaded it.

The old offline route auditor had the complementary error: it treated the PC
text value as internal `d`. That made its point-to-area results appear correct
for the incorrectly exported files while the native engine returned area zero
for every diagnosed start and goal. The exporter now writes the negated packed
component, and the auditor evaluates textual planes as
`normal dot point - distance`. Nonzero-distance regression fixtures cover
both directions of the contract.

All 26 recovered AAS.X products were regenerated with the corrected
serialization. The campaign-port suite passes 116 tests. On
`xc_mars_city1_1`, the corrected AAS48 has SHA-256
`aa4448e1abca303022f6e4efa6c61ced42a0445781a522ec5385488b78821168`;
a true-COOP native run then loaded all 940 entities and produced zero AI path
warnings, zero failed point-to-area diagnostics and zero missing runtime
resources.

Three Xbox DEF files refer to inventory-icon images that are absent from both
the selected-map GFC and the shared `assets.gfc` inventory:
`guis/assets/hud/items/chaingun_ammo.tga`,
`guis/assets/hud/items/rocket_ammo.tga`, and
`guis/assets/hud/items/pda.tga`. Their Xbox gameplay definitions are retained.
The overlay generator comments only the matching `inv_icon` line in the exact
chaingun, rocket-launcher and PDA DEF paths, records each transform and leaves
unrelated definitions unchanged. The corrected native run has zero
missing-image warnings.

## Checkpoint 007 PC-host and HUD-format findings

The Xbox co-op HUD cannot call the stock PC executable's UI manager as though
the Xbox `idUserInterfaceManager` vtable were present. An exact-symbol
first-chance crash dump placed the invalid call in `idPlayer::DrawHUD`; the
target value was `0x3d3d3d3d`. The Xbox branch's `DrawText` virtual slot does
not exist at the same PC ABI position. The source-port solution sets
`xboxCoopStatusText` and `xboxCoopStatusVisible` on the existing player HUD
and lets the normal PC `Redraw` path render an injected status window. This is
a host-compatibility shim, not recovered map content.

The retail HUD uses four Xbox-only GUI script commands. For the PC host the
overlay generator applies these path-scoped translations:

| Xbox command | PC HUD state change |
| --- | --- |
| `HidePDAIcon` | hide `NewPDAVis`, `NEWPDAIcon` and `NEWPDA` |
| `ShowPDAIcon` | show `NEWPDAIcon` |
| `HideVidIcon` | hide `NewVidVis`, `NEWVidIcon` and `NEWVid` |
| `ShowVidIcon` | show `NEWVidIcon` |

The authenticated disc's `global.d3tfull` extent starts at byte
`2825555968`, is `178959016` bytes long, has magic `0xd574dcd2` and table
tag `0x83ac5c28`. Six selected missing HUD images establish three record-type
cases. `0x83f0` is DXT1, while `0x83f2` and `0x83f3` are DXT5. The
`0x83f3` conclusion is supported by valid decoded alpha/color output for
`TipBorder` and all three Xbox-Live icons, plus their retail material usage;
it is not a filename-only guess.

| Logical image | Type | DDS SHA-256 |
| --- | --- | --- |
| `guis/assets/health/hspike1` | `0x83f2` / DXT5 | `774c9836351afa1a83ad86fe3f1739c62ad5896a1509ac5f0098c78473d1517f` |
| `guis/assets/hud/TipBorder` | `0x83f3` / DXT5 | `a043d44ee341a95c002c92c617bcab5d43582a9beb53526087970fd6c6d8aa31` |
| `guis/assets/hud/Vote` | `0x83f0` / DXT1 | `7778109ee07668cb6fb26bc8f95cffa7ffd983a7009c75521e8ccc859b00f450` |
| `guis/live/assets/FriendInviteReceived` | `0x83f3` / DXT5 | `83f993881ce1735971dd5bd2951ff92679badca54c0e042685bd10f9e9bdc17d` |
| `guis/live/assets/FriendOnline` | `0x83f3` / DXT5 | `c51c85219f9477f8fccf7c4cbb2ba1346108d96af6b29773845c01e6871cb81e` |
| `guis/live/assets/GameInviteReceived` | `0x83f3` / DXT5 | `7c3d503a292b5326e45b474a46807c655e5ff4aecd3ef06c17722a21cce61de6` |

Xbox material declarations may contain a standalone `dxt5` storage hint that
the stock PC material parser does not recognize. The generated material closure
removes only that token from the five selected declarations. The referenced DDS
files still carry a DXT5 FourCC, so texture compression is not changed.

The final true-`COOP` native run has no missing-image, unknown-GUI-command or
unknown-material-token warning. Its five remaining AI warnings all have static
directed routes in the recovered AAS48: areas 849→793 (11 areas), 793→718
(14), 575→571 (6), 571→499 (10), and 55→4 (4). The discrepancy is therefore
between static graph connectivity and runtime nearest-area/bounds/obstacle
state; it is not evidence that those five reachability chains are absent.

## Checkpoint 005 runtime-format findings

Xbox MDV (`IDMD`) stores both meshes and animations. Mesh decoding uses the
serialized joint hierarchy and inverse bind transforms to reconstruct MD5
weights; influences are normalized only after rejecting bad joint/range data.
Animation decoding restores local transforms without inventing joints. On the
first-map dependency closure, 21 meshes and 234 animations decode. Xbox
MD5ANIM.X is a separate packed-track representation; 55 first-map files decode
after validating component spans, overlap and complete payload consumption.
Where the Xbox skeleton prunes an identity-only intermediate, retargeting
composes source world transforms onto the target parent hierarchy.

D3TFULL records use a keyed table and store Xbox DXT payloads without a PC DDS
container. The extractor resolves logical names, validates record extents and
emits DDS headers for established DXT1, DXT3 and DXT5 formats. Eight images
selected by the first-map HUD dependency ledger were decoded; this is not a
claim that every D3TFULL format code is known.

Xbox campaign audio resolution is a chain, not a filename lookup: XSND shader
metadata selects an INDEXLIST entry, which selects XSB cue/sound metadata and
then an XWB bank/wave entry. The established codec for the first-map selections
is Xbox IMA ADPCM. Eight required cues were decoded to PCM WAV with channel,
rate, encoded-byte and output-frame accounting. Duplicate PCM hashes are
retained when different logical sounds deliberately point to equivalent data.

Retail XBE inspection is read-only and maps file offsets through XBE virtual
sections. It supports ASCII references, direct address references, calls,
dwords and bounded x86 disassembly. Clean-room analysis of `idTurkeyPuncher`
established two 32-bit scores, network snapshots, a server activation event and
client GUI triggers. This behavioral contract was reconstructed in GPL source;
no executable bytes or disassembly are distributed.

The standard PC script compiler exposes a host mismatch in the first co-op
segment: one relay calls `test_trigger_relay`, another calls
`map_marscity1::test_trigger_relay`, and the segmented co-op script omits the
body. The matching Xbox solo script supplies the exact namespaced callback.
The runtime overlay restores that body and qualifies the unqualified reference,
recording both edits and their hashes.

The Xbox player MDV has 50 joints versus the stock PC body's 75. It retains
`loneckcontrol` but omits identity child `neckcontrol`; the two stock bind-world
transforms are identical. Using `loneckcontrol` as the `copy_joint` source for
the PC head removes the native warning without changing the recovered mesh.

Offline AAS route auditing starts at BSP node 1. Checkpoint 005 incorrectly
treated the fourth PC text component as the engine's internal `d`; the correct
text-side test is `normal dot point - distance`. That sign bug canceled the
original exporter's complementary mistake and made all five warned pairs appear
to have directed walk-only routes. Checkpoint 008 corrects both tools and
confirms the result in the native engine.

## Checkpoint 004 AAS.X findings

AAS.X begins with standard `DewmAAS "1.07"` text. Settings, areas and every
reachability remain textual. The standard geometry/topology arrays are omitted
from their normal positions and stored in one final `xboxData` binary block,
delimited by `# ` and ` #`.

The block is a sequence of little-endian uint32 counts and tightly specified
arrays in this order: planes (`float32[4]`, with the fourth float storing
internal `idPlane::d` and therefore negated when exported as PC text
distance), vertices (`float32[3]`), edges
(`int32[2]`), edgeIndex (`int32`), faces (`uint16 plane, uint16 flags, int32
numEdges, int32 firstEdge, int16 areas[2]`), faceIndex (`int32`), nodes
(`uint16 plane, two padding bytes, int32 children[2]`), portals (five int16
fields plus one uint16 cached travel-time field), portalIndex (`int32`) and
clusters (`int32 numAreas, numReachableAreas, numPortals, firstPortal`). The PC
text exporter restores the official field order where memory order differs.

The official GPL `idAASFileLocal::Load` accepts only the standard top-level
sections, so leaving `xboxData` in place is not PC-compatible. On the first map,
all eleven recovered section counts exactly equal independent PC `dmap` output,
and native Doom 3 successfully loaded the recovered AAS48. This establishes
parser compatibility, not AI route or co-op gameplay fidelity.

## Checkpoint 003 PROC.X findings

PROC.X retains `mapProcFile003` textual structure while replacing selected
arrays with `# ... #` binary records. Model-surface vertices are 24 bytes:
five little-endian float32 values (XYZ and ST) followed by one NV2A
`D3DVSDT_NORMPACKED3` word. The normal word stores signed X/Y/Z in 11/11/10
bits, normalized by 1023/1023/511 with the unused negative extrema clamped to
-1. Surface indices are little-endian uint16.

BSP nodes are 28 bytes: plane float32[4], child int32[2], then a zero int32
padding word. Shadow blocks begin with float32 minimum/maximum bounds, followed
by 8-byte vertices (`uint16 x,y,z,w`) and uint16 indices. XYZ reconstructs as
`minimum + q * (maximum-minimum) / 65535`; observed `w` values are 0 or 1 and
the PC textual shadow representation omits them.

Native PC regeneration independently confirms model identity, visible-surface
counts, index counts, area/portal graph and BSP node counts. Xbox shadow data is
more compact than PC regeneration and must remain comparison evidence rather
than being silently substituted when evaluating shadow fidelity.

## Checkpoint 002 retail findings

The retail XDVDFS volume descriptor is at byte `0x10000`, with 2,048-byte
sectors. Its root directory sector is 264 and its root table is 4,188 bytes.
Directory child links are little-endian 16-bit offsets in four-byte units;
extent sectors and sizes are little-endian 32-bit values.

The image contains 20 co-op archives whose names begin `xc_`. Their generated
map members use `.map.x`, `.proc.x`, `.cm.x` and one or more `.aas*.x` names.
MAP.X is a hybrid format: ordinary Version-2 MAP text surrounds `# ... #` binary
records. Brush-side records contain ten little-endian float32 values: four plane
values and two three-value texture rows. PatchDef2 records contain two float32
integer dimensions followed by width*height vertices of five float32 values.
PatchDef3 adds two float32 integer subdivision values before the same vertex
matrix. Rows are width-major and each row contains `height` vertices.

PROC.X is likewise hybrid text/binary and identifies itself as
`mapProcFile003`; CM.X begins with a binary collision representation; AAS.X is
text beginning `DewmAAS "1.07"`. These facts do not yet establish PC runtime
compatibility. The conversion milestone covers MAP.X only.

Authentic GOB blocks have `STBL`, a codec byte, the stored/zlib body, then the
four-byte footer `ENBL`. The exact footer is accepted and any other bytes after
the zlib stream remain an error. This supersedes checkpoint 001's statement
that all zlib unused data is rejected.

Checkpoint 001, requested October 13, 2026 (America/Denver).
Every claim below is either a source-code observation, a tool implementation
contract, or an explicitly open recovery task. No retail campaign payload was
available for a new field-level investigation in this pass.

## 1. Archive container: existing extraction contract

The reconstruction repository already contains `tools/extract_vv_gob.py`, blob
`c1d1d5701f5a3f7cbedf2dcfa52bc9eae50918d5`, at source baseline
`833379c9920403fdfcc9f460042ca1b7ff205808`.
Its format description attributes the GFC/GOB layout to Luigi Auriemma's
`over_the_hedge.bms`. This pass read the existing implementation. Attempts to
fetch the original BMS were unsuccessful; neither an independent BMS comparison
nor a new retail-archive validation is claimed.

The implemented GFC index contract uses big-endian unsigned 32-bit words.
Let B be block_count and F be file_count:

| Offset | Length | Interpretation used by the tool |
| --- | --- | --- |
| 0 | 4 | Magic `0x00008008` |
| 4 | 4 | Declared GOB length |
| 8 | 4 | B |
| 12 | 4 | F |
| 16 | 12*B | Block records: stored length, GOB offset, flags |
| 16+12*B | 4*B | Auxiliary words; preserved, not interpreted |
| 16+16*B | 12*F | File records: name hash, expanded length, first block |
| 16+16*B+12*F | 264*F | Name records: 256-byte name area plus 8 opaque bytes |

The minimum index size is `16 + 16*B + 276*F` bytes. Additional bytes are retained
as opaque tail data. Original name records are retained in hex; the decoded name
is the Latin-1 byte sequence before the first NUL. Empty names are not invented
or renamed automatically. Flags, auxiliary words, name-hash semantics, trailer
semantics and unconsumed tail bytes remain uninterpreted.

Each supported block begins with ASCII `STBL`, followed by a codec byte:
`z` consumes one complete zlib stream; `0` copies the stored body. Unknown codec
or envelope, incomplete streams, and trailing compressed-stream data are
rejected. The earlier extractor has a non-STBL heuristic branch; this new strict
tool deliberately does not implement it without separately established evidence.

Files begin at their first expanded block and consume the declared byte count
across successive blocks, matching the existing extractor's contract. The
manifest records every block contribution and unused final-block suffix. It
does not assert that such suffixes are padding, that block flags are irrelevant
to every title, or that corrupted record overlaps are semantically valid.

**Do not transfer the index's endianness to the map payload.** Container parsing,
block decompression and inner-map decoding are three different obligations.

## 2. PC destination: official reader contracts

Primary source: id Software's official DOOM-3 repository, commit
[`a9c49da5afb18201d31e3f0a429a037e56ce2b9a`](https://github.com/id-Software/DOOM-3/tree/a9c49da5afb18201d31e3f0a429a037e56ce2b9a).

[RenderWorld.h](https://github.com/id-Software/DOOM-3/blob/a9c49da5afb18201d31e3f0a429a037e56ce2b9a/neo/renderer/RenderWorld.h)
defines the PC render-world identifier `mapProcFile003`.
[RenderWorld_load.cpp](https://github.com/id-Software/DOOM-3/blob/a9c49da5afb18201d31e3f0a429a037e56ce2b9a/neo/renderer/RenderWorld_load.cpp)
contains separate readers for `model`, `shadowModel`, `interAreaPortals` and
`nodes`. A model surface identifies its material, vertex count and index count;
its vertex records have eight float components: XYZ, ST and normal XYZ.
Shadow records have their own cap-index counts and position layout. These are
**PC format facts**, not evidence of the Xbox stored layout.

[RenderWorld_local.h](https://github.com/id-Software/DOOM-3/blob/a9c49da5afb18201d31e3f0a429a037e56ce2b9a/neo/renderer/RenderWorld_local.h)
defines positive BSP children as node indices, zero as solid, and negative
children as `-1-areaNumber`. The loader's area entities look up `_areaN` render
models. The new parser checks references, required area models and cycles,
including unreachable cycles, before reporting a structurally decoded PROC.

[MapFile.cpp](https://github.com/id-Software/DOOM-3/blob/a9c49da5afb18201d31e3f0a429a037e56ce2b9a/neo/idlib/MapFile.cpp)
uses a separate MAP entity/brush/patch parser. It disables string-escape
interpretation for map strings. The new structural inspector retains raw
ordered epairs and exact primitive byte spans/hashes; it deliberately does not
emulate geometry construction, origin transforms, idDict duplicate handling,
entity inheritance or script execution. `decoded` remains false for this
partial MAP representation.

The new PROC parser is stricter than the complete engine lexer and should not
be advertised as accepting every file the engine accepts. Float values are
normalized to float32; structural comparisons retain signed-zero differences.
Order is retained, not canonicalized by geometric similarity.

## 3. Using converted multiplayer maps correctly

First establish provenance: the original Xbox MP file and the PC conversion
must represent the same map and revision. Record all known manual edits,
regeneration steps and replacement assets. Do not use a remake or a merely
similar map as a bit-exact reference.

The reference probe searches Xbox-candidate bytes for exact PC material strings
and float32 XYZ/eight-float vertex sequences, separately in both endians. It
records offsets, source vertex identity, pattern bytes and capped hit lists.
All-zero XYZ is excluded as weak evidence. A hit proves only that the bytes
occur. A miss does not prove absence: compression, quantization, swizzling,
packing, transforms or editing can defeat exact matching.

Promotion from a candidate to an established layout requires independent
constraints: a bounded record region, sensible counts and offsets, consistent
stride, valid index ranges, multiple distinct vertices/materials, known
transform rules, consumption accounting and confirmation from additional maps
or the actual Xbox reader. The official PC reader can suggest counterparts in
the retail executable; it is not a retail PDB or proof that structure layouts
match. This pass did not have the retail executable and resolved no such reader.

Keep MP evidence scoped to shared format elements. It does not establish co-op
triggers, second-player spawns, encounters, checkpoint logic or campaign transitions.

## 4. Open Xbox-map work

The inner file identifiers, versions, compression layers, field endianness,
vertex/index encoding, brush/patch representation, compiled collision, portal
ordering, navigation representation, entity serialization, script linkage and
campaign registry relationships are **unestablished by this checkpoint**.
No candidate offsets were obtained from actual Xbox maps. Do not fill these
unknowns from memory, guessed C structures, PC defaults or file extensions.

For each established field, record source hash, byte range, type, endian,
reader evidence, meaning, transformation, output location and counterexamples.
Retain unexplained spans. Separately label recovered editable source geometry,
recovered compiled geometry and newly reconstructed geometry; they are not
interchangeable forms of evidence.

