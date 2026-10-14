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

## Current checkpoint: 004

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
- [Checkpoint receipt](evidence/checkpoint-001.json): source hashes, validation
  scope and explicit incomplete obligations.

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

