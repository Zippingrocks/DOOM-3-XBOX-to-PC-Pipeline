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

## Current checkpoint: 006

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
- [Checkpoint receipt](evidence/checkpoint-006.json): current source hashes,
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

