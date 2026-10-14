# Doom 3 Xbox to PC: campaign-map recovery

## Goal

Recover and translate the **original-Xbox Doom 3 co-op campaign maps first**, then
complete both the original solo and co-op campaigns on the GPL PC host. Preserve
Xbox layouts, collision, visibility, materials, entities, encounters, scripts,
progression and co-op-specific behavior. Already-converted Xbox multiplayer maps
are format/comparison references, not replacements for campaign recovery.

This repository preserves findings, evidence boundaries, commands and handoffs.
Map-related implementation lives in
[doom3-gpl-xbox-reconstruction](https://github.com/Zippingrocks/doom3-gpl-xbox-reconstruction).
Changes there are limited to recovering, converting, loading or validating Xbox
campaign maps. Existing accepted engine/frontend/co-op profiles remain intact.

## Current checkpoint: 014

**The second co-op segment now crosses the MAP/PROC/CM/AAS loader boundary,
and its first native spawn blocker is isolated to a specific reconstructed
instant-hit AI null dereference.**

`xc_mars_city2_1` has a direct 219-model authored CM export bound to MAP CRC
`3219770337`. Independent PC `dmap` output contains all 219 authored models;
its 93 additional models correspond exactly to MAP entities marked
`noclipmodel 1`. The authored CM, decoded PROC and decoded AAS48 all load on
the PC host.

The unmodified runtime faults while spawning `monster_zsec_machinegun_9`.
Disassembly and a captured minidump identify the chain precisely:
`idAI::CreateProjectile` returns null for an Xbox projectile with
`net_instanthit 1`, then `idAI::Spawn` calls `GetPhysics()` on that null value.
Changing only that projectile flag in a temporary local diagnostic advances
to `monster_zsec_shotgun_2` and the identical fault; suppressing all selected
instant-hit flags lets all 1,110 entities spawn with zero inhibited and exit 0.
That data edit is diagnostic only and is not an accepted conversion. The
required fix is a narrow source guard that preserves instant-hit combat. An
isolated binary control-flow diagnostic implementing only that guard, with the
original Xbox flags restored, independently produced the same 1,110/0 result
and exit 0. The original DLL was restored and hash-verified afterward; a normal
source rebuild is still required for acceptance.

The second-map overlay is still provisional: the clean diagnostic run exposes
missing co-op-player resources and a player skeleton error that must be added
to the closure before acceptance. Full receipts and evidence boundaries are in
[`evidence/checkpoint-014.json`](evidence/checkpoint-014.json).

## Previous checkpoint: 013

**The runtime-overlay builder now selects the direct Xbox-authored CM as a
reproducible, source-bound payload instead of relying on a manual post-build
swap.**

`build_runtime_overlay.py --authored-cm <decoded-map.cm>` retains the complete
PC-compiled map set as an independent structural cross-check, validates that
the authored file has the exact map filename and PC `CM "1.00"` text form,
and requires its embedded map CRC to equal the generated CM. It replaces only
the staged CM and records both inputs' sizes and SHA-256 hashes plus the
selected `direct-authored-cm` source. Invalid headers, filenames, encodings or
CRCs fail closed and publish no overlay. Generated material-closure receipts
are also independent of absolute versus relative resource-root spelling.

The finalized `xc_mars_city1_1` authored-CM overlay contains 374 files with
zero unresolved resources or classnames. Its 183,787-byte manifest hashes to
`97a07d80b1071d79a96bff5e85e729fdefdb8654f1a8f2d369928459ca532315`.
The staged 3,320,995-byte CM is byte-exact to the direct CM.X export and shares
map CRC `2410032894` with the independent PC-`dmap` CM. A true `COOP` native
smoke load spawned all 940 entities, inhibited none, and emitted no error,
fatal or missing-resource line. The local Python suite passes all 147 tests.

This accepts the reproducible overlay-selection mechanism and first-map loader
boundary, not a whole-map playthrough, two-peer progression, mover/trigger
behavior, original-Xbox runtime equivalence, or any of the remaining 19 co-op
CMs. Full machine-readable receipts are in
[`evidence/checkpoint-013.json`](evidence/checkpoint-013.json).

## Previous checkpoint: 012

**Live spawned-entity collision now proves that PC-`dmap` output is not a
fidelity-equivalent substitute for direct Xbox-authored CM.X.**

The hidden collision oracle can now target `@entity`. It resolves the spawned
entity's clip model, origin, axis, absolute bounds, contents and linked/enabled
state, then queries the collision manager at that real runtime placement. The
input digest binds all of that context while intentionally excluding numeric
collision handles, whose ordering differs between generated and authored CMs.

Three first-map live entities were compared with 4,096 point and 4,096
player-hull samples per CM: `doorClip_1`,
`trigger_coop_enablegui_2` and `func_static_53167`. All targets were linked
and enabled at the recovered MAP origins. All 24,576 record pairs used identical
inputs and agreed on hit/no-hit outcomes. Nevertheless, they contain 3,393
gameplay mismatches: 3,367 contact-manifold differences, one stopping-trajectory
difference and 97 material-selection differences. The live static also has 11
point start-contents disagreements. Door and trigger point results and stopping
trajectories are exact, but their swept player-hull contact manifolds are not.

This promotes direct decoded CM.X from a candidate to the required
fidelity-preserving collision payload for the PC overlay. It does not yet prove
door motion over time, trigger side effects, rotated clip axes, original-Xbox
runtime behavior, two-peer behavior or the remaining 19 co-op map CMs. Full
machine-readable receipts are in [`evidence/checkpoint-012.json`](evidence/checkpoint-012.json).

## Previous checkpoint: 011

**The native collision oracle now covers explicit gameplay masks, exact hulls
and named collision models. Direct authored CM.X remains required even where
broad blocking outcomes agree.**

The hidden diagnostic now accepts a collision-model name, numeric contents mask
and six optional hull-bound floats. It rejects unresolved model names instead
of silently falling back to world model zero. The run input digest binds the
resolved model identity, mask, hull, model bounds, seed, count and every raw
coordinate bit. The comparator fails closed on missing summaries or different
input digests and separates stopping trajectory from contact-manifold geometry.

Five generated-versus-authored profiles were run at 4,096 point and 4,096 box
samples each: world monster-solid with an actor hull, world shot collision with
the recovered rocket hull, named `doorClip_1` player clipping, named
`trigger_coop_enablegui_2` trigger contents, and solid collision against
polygon-only `func_static_52977`. All 40,960 records pair with identical input
digests, coordinates and hit/no-hit outcomes. Point geometry matches throughout.

The authored data is still observably different. Across the matrix there are
121 stopping-trajectory mismatches, 2,741 contact-geometry mismatches, 875
material/contents mismatches and 3,507 total gameplay mismatches. The two world
profiles contribute 47 trajectory, 313 contact and 875 metadata mismatches.
The named door and trigger have exact stopping trajectories and metadata but
different swept-box contact manifolds in 1,065 and 767 rows. The polygon-only
static model differs in 74 trajectories and 596 contact manifolds.

All ten true-`COOP` runs spawn 940 entities, create the local player, emit
8,192 trace rows and exit 0 without an error or fatal. The test CM and DLL were
restored to their exact prior hashes. The suite has 142 passing tests and the
complete Win32 game DLL builds. Licensed trace logs stay local; their hashes and
the comparison receipts are recorded in the evidence file.

This closes static first-map world-mask and representative named-model
measurement, not live door motion, trigger dispatch, actor/projectile
orientation, an original-Xbox runtime oracle, the remaining 19 co-op maps,
two-peer progression or whole-campaign fidelity.

See [checkpoint 011](evidence/checkpoint-011.json).

## Previous checkpoint: 010

**PC `dmap` collision is now proven to be a cross-check, not a fidelity
substitute for the direct Xbox-authored CM.**

A hidden map-port diagnostic fed the same seeded coordinates into the PC
collision engine twice: once with the independently generated CM and once with
the direct CM.X export. Each run emitted 8,192 lossless records: 4,096 point
queries and 4,096 player-sized box queries. World bounds and the complete input
digest match exactly, every record pairs, both files execute the same traces,
and hit/no-hit outcomes match.

The contact results do not. At strict but practical tolerances (0.01 map units
for positions/plane distance, 0.001 for normals, and 1e-6 for fractions), 650
records differ. All 4,073 executed point traces agree geometrically, but 265
player-box contacts differ in geometry. Across both shapes, 501 contacts select
different material or contents metadata; 385 of those are metadata-only
differences. Fifty-four movement fractions/endpoints differ beyond tolerance,
with a maximum endpoint delta of 416 units. This is direct evidence that
regenerating collision can change player motion, clip behavior, impact
materials and contents classification even when the map loads and broad hit
counts agree.

Both bounded true-`COOP` runs spawn all 940 entities, join the local player
and exit 0 with no error or fatal. The generated CM and prior verified DLL were
then restored byte-for-byte. The paired log SHA-256 values are
`729193a3d9614f1041bfa9300398ad25484f497d7f736e860fe195348a5d8e3d`
and
`e66776c4cb2c8e9962e6431ade61afa7969994e2bb568947ef1d6110d1856712`;
the comparison report SHA-256 is
`8a2d6b9028717a189097555e759772686760cc52456a817550f189e46749d577`.
The recovery suite now has 141 passing tests and the complete Win32 game DLL
builds.

This establishes that the direct authored CM is required for fidelity. It does
not yet establish an Xbox-runtime trace oracle, entity/mover/trigger collision,
remaining-map native trace closure, two-peer progression or whole-campaign
fidelity.

See [checkpoint 010](evidence/checkpoint-010.json).

## Previous checkpoint: 009

**The first co-op segment now loads the original Xbox-authored collision model
on PC, and the complete extracted CM.X corpus is structurally decoded.**

Private implementation head `cf08a48e961467b9ef1a77a96f93b949035892e6`
adds a strict CM.X decoder, deterministic corpus auditor, regression fixtures
and handoff documentation. The Python suite now has 138 passing tests. The
decoder expands model headers, vertices, edges, shared planes, brushes,
polygons and preorder BSP nodes to standard PC CM 1.00 text; it converts
internal Xbox plane `d` to PC `idPlane::Dist() == -d`.

All 1,200 extracted CM.X members parse with complete byte consumption,
representing 391 unique payloads. The audit covers 4,813 models, 428,453
vertices, 792,130 edges, 294,185 planes, 50,693 brushes, 356,793 polygons and
381,933 nodes. Every polygon and brush is referenced by the Xbox BSP and no
node contains a duplicate primitive reference. The corpus receipt SHA-256 is
`838535f1924ffa89f15bfbfb8397b705fe1178cc74ac01e88a46e6bbc974762f`.

All 20 top-level co-op map CMs also export deterministically in memory using
geometry CRCs computed from their paired converted MAPs. The audit binds
43,791,272 bytes of CM.X to 71,372,306 bytes of would-be PC CM across 3,633
models; its MAP/CM.X/output manifest digest is
`3a27835c398b2d5c9bd280a29c397efe47868ea965ae4d9f9900fa2755cf0603`.
No licensed CM outputs are published or retained by that audit.

The first map's 2,003,187-byte CM.X expands to a 3,320,995-byte PC CM with
SHA-256
`35a8ebff563a9d449995c02a90f1e822aa9dfeb42ec289b0128b8b1132cd8931`.
Its 243 authored model names are a complete subset of the independent PC
`dmap` CM. Every one of the 34 generated-only names belongs to a recovered MAP
entity marked `noclipmodel 1`; there are no authored-only or unexplained names.
A bounded native run loads it directly in 29 ms as 243 models, 15,146 vertices,
25,468 edges, 10,005 polygons, 2,784 brushes and 7,167 BSP nodes. The map then
spawns all 940 entities, joins the local player and exits 0. The native log
SHA-256 is
`c56451c2e4bff8cbfc6185504baa9a98a08d71c8a16ea4bdeafe2eed09dd6d08`.
The prior PC-generated collision file was restored and verified byte-for-byte
after the test.

This is direct authored-collision loader acceptance, not collision fidelity
acceptance. The PC loader reconstructs all 9,237 Xbox brush-node references but
21,999 polygon-node references versus 22,341 stored by Xbox. Matched trace
sampling, native loading for the remaining maps, two-peer progression, all-map
runtime closure and Xbox visual/gameplay comparison remain open.

See [checkpoint 009](evidence/checkpoint-009.json).

## Previous checkpoint: 008

**The first co-op segment now has working recovered Xbox navigation on PC, with
the former five NPC route failures eliminated at the format boundary.**

Private implementation head `0181311c92681e09d05adfcd104d9ed9e10117f7`
contains the corrected AAS converter, matching route auditor, exact inventory-
icon compatibility transforms, 116 passing Python tests and updated handoff
documentation. The DLL used for the native receipt was built from source commit
`a60a42a07152fc77ca47f2b2de920aff85372636` by Actions run `38531204632`.
Artifact `11877622996` has ZIP SHA-256
`70d1c1b7af5655c881940eebeebd019e26014ffc23cd68a2038b41de9387aec2`;
its 2,723,328-byte DLL has SHA-256
`1eb641d6869cf70bf947e4bc10208949f0a8344953bf1055ded7cf3b3ef74e34`.

The root cause was a serialization-contract mismatch. Xbox `xboxData` stores
the in-memory `idPlane` tuple `(normal, d)`, but standard PC AAS text stores
`(normal, idPlane::Dist())`, and `Dist() == -d`. Emitting raw `d` caused the
PC loader's `SetDist()` to flip every BSP plane. The offline route auditor had
the same sign mistake, masking the defect. Both implementations now have
nonzero-distance regression tests, and all 26 co-op AAS.X members were
regenerated with the corrected conversion.

The clean first-map overlay has 374 hashed payload records, 336 copied runtime
resources, one generated empty EFX, zero unresolved resources/classes and
manifest SHA-256
`f2b9787ef8ec8823022de2bf6f502d08c3ec74c2a7dc6787b5f2975f7a24889e`.
Three Xbox weapon `inv_icon` references name textures absent from both the map
and shared retail GFC inventories; exact path-scoped transforms disable only
those lookups while retaining the Xbox gameplay declarations.

A bounded true-`COOP` native run spawns 940 entities with zero inhibited,
observes the local player joining, and exits 0. It has zero missing images,
models, animations or sounds; zero `Could not spawn`; zero unknown GUI/material
tokens; zero path-corner failures or AAS diagnostic failures; and zero errors
or fatals. The log SHA-256 is
`f3c849a836ca6964a60ffeb6358cc4268c1423ddff8ff4a64bbf831edae3b8da`.
Two-peer progression, direct CM.X recovery, all-map runtime closure and matched
Xbox visual/gameplay fidelity remain open.

See [checkpoint 008](evidence/checkpoint-008.json).

## Previous checkpoint: 007

**The first co-op segment now runs as a true PC `COOP` listen server with a
joined player and a complete first-map HUD/material closure.**

Private implementation head
`7f35412a6cf8c238ca4ca6b91e6df3fce75ce6af` contains the checkpoint tools,
tests and documentation. The exact runtime DLL was built from source commit
`243dbafe867d9c89ab48cb56e17bdc05c69ab704` by GitHub Actions run
`38527277656`. Artifact `11876766170` has ZIP SHA-256
`76e80fe9a5bbb9b3f4cf5661a0916a46f87b279ebe0ce73f03d5d87131606ed8`;
its 2,721,280-byte `gamex86.dll` has SHA-256
`815c4a2238bb49dc52e5090913d6d216d898d0fe5d007fe9246424ae3bc6c011`.

The prior true-COOP crash was traced with exact symbols to `idPlayer::DrawHUD`.
Xbox calls a `uiManager->DrawText` virtual slot that the stock PC executable
does not expose at the same ABI position. The map-port branch now writes the
status through HUD state and an injected GUI window, avoiding any executable
ABI extension. Four Xbox-only HUD icon commands are translated to the matching
stock-PC GUI visibility assignments.

Six previously missing HUD/Xbox-Live images were recovered selectively from
`global.d3tfull`. Retail texture type `0x83f3` is evidence-backed as DXT5.
The overlay builder now resolves selected material roots and strips the
Xbox-only `dxt5` storage hint while retaining DXT5 in each DDS header. A
bounded native run starts `xc_mars_city1_1` as `COOP`, spawns all 940
entities with zero inhibited, logs `Server: Player joined the game.`, emits no
missing-image, unknown-GUI-command, unknown-material-token, error or fatal line,
and exits with code 0. The final log SHA-256 is
`618a4760af9645928c5a090195e5da08e4b36ccc5481f975f2154878f3776675`.

Five dynamic NPC/path-corner warnings remain. Static analysis proves a directed
walk route for every pair, so the next work is runtime nearest-area selection,
actor bounds, dynamic obstacles/doors and script timing. This is not yet
two-peer progression, direct CM.X recovery, all-map closure or fidelity
acceptance.

See [checkpoint 007](evidence/checkpoint-007.json).

## Previous checkpoint: 006

**The first co-op map now crosses the reconstructed source-DLL boundary with
every Xbox-only spawn class instantiated.**

Private implementation head
`9ebe3701c7e1ab28ee4483477ee071a2fe8cca1a` adds a Windows validation
workflow. GitHub Actions run `38525058861` passed both gates: all 103 Python
recovery tests and a complete v143 Win32 build of `gamex86.dll`. The published
artifact ZIP matches SHA-256
`3650517235dd1fb787c8bbde903a3314aa1aa546ca0e3e6fc9d1add861948ac8`;
the DLL is 2,721,280 bytes with SHA-256
`5c5fb61a0163d70db57dcfc1c098bdfe6a4a093f2e5f280e2ec711c5a1b58e9a`.

Doom 3 checks for a development DLL beside `Doom3.exe` before extracting the
stock DLL from `base/game03.pk4`. Using that loose-DLL path with the existing
provenance-recorded overlay loads `xc_mars_city1_1` in 2.598 seconds, spawns
940 entities with zero inhibited entities, runs the restored callback and exits
normally. All prior `idGuiSyncEntity`, `idGuiSyncDoor`,
`idTarget_IncreaseSpawnLevel`, `idTrigger_Coop_EnableGui` and
`idTurkeyPuncher` spawn failures are gone. There are zero `Could not spawn`
warnings.

Five unique NPC/path-corner failures remain. Each corresponding start/goal pair
has already been proven connected in the recovered AAS by a walk-only directed
route, so the remaining investigation is dynamic actor bounds, obstacle/door
state and script timing. This checkpoint does not suppress those warnings or
claim co-op progression, direct CM.X recovery, all-map closure or fidelity
acceptance.

See [checkpoint 006](evidence/checkpoint-006.json).

## Previous checkpoint: 005

**The first co-op map now has a reproducible runtime-asset overlay and reaches
a clean, fully loaded native PC state apart from source-DLL-only behavior.**

The recovery toolset now includes Xbox MDV mesh/animation decoding, packed
MD5ANIM.X decoding, world-space skeleton retargeting, D3TFULL DXT texture
extraction, XACT/Xbox-IMA sound recovery, a fail-closed dependency overlay
builder, a read-only XBE analysis helper and an offline AAS route auditor. The
synthetic suite contains 103 passing tests on Python 3.11/Windows.

For `xc_mars_city1_1`, 21 MDV meshes, 234 MDV animations and 55 MD5ANIM.X
animations decode. Eight selected D3TFULL records produce valid DXT DDS files,
and eight selected XACT cues resolve through XSND/INDEXLIST/XSB/XWB to PCM WAV.
Whole Xbox DEF files shadow stock VFS paths only where declarations materially
differ. Every generated overlay records input/output hashes and exact
PC-compatibility transforms.

Two host differences are now explicit and reproducible. The co-op map retains
one unqualified callback plus one qualified call but omits the callback body;
the overlay restores the exact matching Xbox solo function and qualifies both
references. Xbox MDV pruning removes the identity-only body joint
`neckcontrol`; its retained parent `loneckcontrol` has the same bind transform,
so the PC head copy uses that exact alias. Native validation confirms the
callback runs and the prior copy-joint warning is gone.

The map again loads 940 entities with no missing recovered HUD DDS, selected
WAV, EFX, AF-joint, script-compile, callback or copy-joint warning. The private
source branch reconstructs the five first-map Xbox-only spawnclass families,
including the networked two-score Turkey Puncher contract recovered from the
retail XBE. The stock retail DLL cannot instantiate those new classes; a source
build is therefore the next required runtime boundary.

Five NPC path warnings remain in the stock-DLL harness. Offline BSP/route
auditing maps every involved origin and goal to reachable AAS areas and finds
walk-only paths of 4 to 13 areas. This rules out lost reachability records but
does not model the dynamic door/obstacle state, including the missing Xbox
door-sync class. No warning is silently suppressed or declared fixed.

See [checkpoint 005](evidence/checkpoint-005.json).

## Previous checkpoint: 004

**The complete co-op geometry/navigation corpus now decodes, and the first map
loads through the native PC runtime with its recovered Xbox AAS.**

All 20 co-op MAP.X and all 20 PROC.X members decode without failure. Every
decoded PROC passes the independent structural inspector. Corpus totals include
313,418 brush sides, 32,066 patches, 930,756 visible vertices, 2,391,825 visible
indices, 5,647 models, 1,159 areas, 1,183 inter-area portals and 97,387 BSP
nodes. These totals are coverage evidence, not a fidelity percentage.

All 26 AAS.X files also decode. The files retain ordinary textual settings,
areas and reachabilities while packing planes, vertices, edges, faces, nodes,
portals and clusters in a final `xboxData` block. Expanding those little-endian
arrays produced standard PC AAS text. On `xc_mars_city1_1`, all eleven section
counts exactly match independent PC `dmap` regeneration. Native Doom 3 accepted
the recovered AAS48, loaded the map in 3.034 seconds and spawned 940 entities.

The smoke load exposed the next concrete blockers: ten missing co-op classname
families, four map-script functions, nine GUIs, six language strings and three
sounds. Collision still comes from PC `dmap`; direct CM.X decoding remains open.
Two-peer progression and visual/gameplay fidelity have not been accepted.

See [checkpoint 004](evidence/checkpoint-004.json).

## Previous checkpoint: 003

**The first genuine co-op map now compiles through the native PC toolchain.**

`xc_mars_city1_1.proc.x` was decoded into structurally valid PC
`mapProcFile003` text, including NV2A 11:11:10 packed normals, 16-bit indices,
quantized shadow vertices and padded BSP nodes. All 59 synthetic and structural
tests pass on Windows/Python 3.11. Native Doom 3 `dmap` then compiled the decoded
MAP without a leak and generated PC PROC, CM and AAS48 files.

Independent comparison between decoded Xbox PROC.X and PC regeneration found
the same 356 model names, 42,128 surface vertices, 99,651 indices, 80 areas,
80 portals and 4,872 BSP nodes. Three Xbox surfaces were split into six PC
surfaces while retaining material and aggregate geometry. Maximum paired-value
deltas were 0.000412 units for position, 0.000061 for UV and 0.000978 for
normal components, consistent with source float/normal packing. Runtime assets,
script loading, co-op progression and visual/gameplay acceptance remain open.

See [checkpoint 003](evidence/checkpoint-003.json).

## Previous checkpoint: 002

**The authenticated retail disc is now inventoried and the first genuine co-op
MAP.X has been deterministically decoded to PC MAP text. This is a source-bound
conversion milestone, not a playable-map or fidelity milestone.**

The USA/Asia Limited Collector's Edition XDVDFS image (SHA-256
`444460aab24b6df9e4cf7bd9bc442f2c95d675f44d1022f0242818813eb7d20e`)
contains 377 filesystem entries and 20 `xc_` co-op GFC/GOB archive pairs. Across
those co-op archives, the inventory identifies one campaign MAP.X/PROC.X/CM.X
set per pair plus AAS data and map scripts. `xc_mars_city1_1.map.x` was extracted
with full block provenance and decoded from its hybrid text/binary representation
to ordinary Doom 3 Version-2 MAP syntax: 17,210 brush sides, 637 patchDef2
primitives and 988 patchDef3 primitives. The output remains local licensed data.

Retail STBL blocks carry an exact `ENBL` footer after both stored and zlib bodies.
Checkpoint 001's strict extractor rejected this authentic footer; the
implementation branch corrects the contract and adds XDVDFS and MAP.X tools.
PROC.X, CM.X, AAS runtime compatibility, dependencies, scripts, engine loading
and two-player progression remain open before a serious playtest.

See [checkpoint 002](evidence/checkpoint-002.json) for hashes and claim limits.

## Previous checkpoint: 001

**Offline recovery tooling delivered; no retail campaign map decoded or ported
in this checkpoint. Not ready for a near-final campaign playtest.**

Implementation commit:
[`51d0a78bb19b6b4716726a6afc089ea57fe5741c`](https://github.com/Zippingrocks/doom3-gpl-xbox-reconstruction/commit/51d0a78bb19b6b4716726a6afc089ea57fe5741c).
It adds only four files: an isolated recovery tool, synthetic tests, tool usage
and the map-porting successor scope. No existing file is modified.

The tool supports GFC inventory; strict, traceable STBL extraction from GOB;
PC PROC structural inspection/comparison; raw Version-2 MAP epairs and opaque
primitive spans; and candidate-byte probing against a converted MP PROC.
**46 synthetic unit tests passed on Python 3.13.5/Linux.** Native Windows,
retail archive compatibility, Xbox binary-map decoding, PC map loading and
actual two-player fidelity were not tested in this pass.

The accessible source repository excludes retail assets. The Library and
working-container checks did not locate a complete Xbox campaign corpus or a
matched original-Xbox/converted-PC MP reference pair. Therefore there is no
claimed retail map count, recovered payload layout, campaign coverage percentage
or completed conversion. The immediate next input-dependent task is the real
archive inventory followed by a matched MP pair and one real co-op map.

## Read in this order

- [Reproduce the checkpoint](docs/REPRODUCE.md): exact commands, paths, outputs,
  error interpretation and source identities.
- [Format findings](docs/FORMAT_FINDINGS.md): established PC/archive contracts,
  unknown Xbox payload fields, and how to use MP reference evidence.
- [Acceptance and recovery order](docs/ACCEPTANCE.md): per-map obligations,
  pre-playtest readiness and final solo/co-op acceptance.
- [Checkpoint receipt](evidence/checkpoint-010.json): current source hashes,
  validation scope and explicit incomplete obligations.

## Working rule

Do substantial decoding, conversion and offline checking before asking for a
serious playtest. Cheap parser/unit checks continue during development so a bad
field assumption cannot spread through every map. A later focused engine-load
check and actual solo/two-peer campaign validation are required before claiming
fidelity. Passing synthetic tests, finding strings, extracting an archive or
rendering a room is not campaign completion.

Do not silently substitute stock PC maps, guessed brushes/collision, fabricated
spawns, default materials or skipped scripts for unknown Xbox content. Preserve
unrecognized byte spans, explicit assumptions and unresolved dependencies.
Never conflate recovery of a playable map with recovery of its original editable
source; establish and label each independently.

## Asset boundary

No retail archives, extracted maps, textures, scripts, executable bytes, keys,
converted-map packages or private captures belong in this public repository.
Keep source inputs and generated game data local under the reconstruction
repository's ignored `game/` tree. Publish research descriptions, provenance,
hashes and reproducible tools/recipes, not licensed game content.

