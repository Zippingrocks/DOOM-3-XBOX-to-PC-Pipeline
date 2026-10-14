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

## Current checkpoint: 001

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
