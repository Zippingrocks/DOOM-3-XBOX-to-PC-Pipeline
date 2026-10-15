# Reproducibility correction plan and next-AI handoff

Updated 2026-10-15. **Read this before continuing checkpoint 084.**

## What the user actually needs

Recover the original Xbox co-op campaign first, then all solo maps, with
repeatable conversion and eventual high-fidelity PC play. Preserve the original
Xbox presentation. Research already performed must become durable code,
recipes and evidence, so another AI does not have to rediscover it.

**Git synchronization is not the same as a portable reconstruction.** Git
contains the converters, tests and substantial findings. The latest replay
commands still consume previous local overlays and recovered resource folders.
A clean-machine rebuild using only these repositories plus legitimate original
inputs has **not been demonstrated**. That is a delivery/reproducibility gap,
not evidence that the map decoding must be thrown away or repeated from scratch.

This handoff is bounded triage, not an exhaustive audit of ignored files,
every recipe, every archive or all local knowledge. No new gameplay,
Steam, dmap, xemu, corpus rebuild or long validation run was performed here.
No private asset backup was created. Do not tell the user that everything on
this device is saved merely because both Git working trees are clean.

## Read first and pin the right history

1. This document and [the bounded triage inventory](../evidence/checkpoint-084-reproducibility-triage.json).
2. [Checkpoint 084 stop/resume state](CHECKPOINT_084_HANDOFF.md).
3. [Checkpoint 084 evidence](../evidence/checkpoint-084-offline-corpus-review.json)
   and [historical warning inventory](../evidence/checkpoint-084-historical-warning-summary.json).
4. [Format findings](FORMAT_FINDINGS.md), [reproduction recipes](REPRODUCE.md)
   and [acceptance boundaries](ACCEPTANCE.md).
5. Source repository `docs/CAMPAIGN_MAP_PORTING.md` and
   [archived diagnostic sources](https://github.com/Zippingrocks/doom3-gpl-xbox-reconstruction/tree/3db16ab0eba778ee2f3fb4b3499d7942978e9002/docs/checkpoint-084-diagnostics).

| Repository / ref | Recorded identity and meaning |
| --- | --- |
| Pipeline `main` and `checkpoint-002-retail-mapx` | Checkpoint 084 baseline `22da24992c339c5b7ae7bb0bed1eb7632b952cef` was verified pushed to both. This handoff is a successor; inspect its commit and verify remote refs again. |
| Reconstruction `master` | Functional code/test baseline `c61e370365ecabd826594947afcc82ec2cfb236f`; 460 offline tests passed at that revision. |
| Reconstruction `master`, preservation successor | `3db16ab0eba778ee2f3fb4b3499d7942978e9002` adds documentation and five non-executable diagnostic snapshots only. Pushed and remote-verified. No new functional-test result is claimed. |
| Reconstruction `main` | Preserved older COOP lineage `51d0a78bb19b6b4716726a6afc089ea57fe5741c`, structurally different and using `vendor/doom3-gpl`. Do not overwrite it with master or replace master wholesale with it. |

Solo v40 was built at `a23d1a9062abfc4fe5a1cfcd57ecd83c572fd5c8`;
co-op v20p at `c61e370365ecabd826594947afcc82ec2cfb236f`. Keep execution
provenance separate from later preservation commits. Do not infer an older
receipt's imported-module revision from the currently checked-out source.

The local source `master` had no upstream configured despite its verified
push. Compare explicit remote refs with `git ls-remote`, not just tracking
labels. Use normal fast-forward pushes: source changes to `master`, pipeline
handoffs to both `main` and `checkpoint-002-retail-mapx`. Never force-update
the older source `main` to make branch names match.

## First priority: do not strand the device-only state

Local layout used in the recipes:

- `GAME`: the user's Doom 3 installation directory.
- `DEV`: `GAME/Work files/campaign-port-dev`.
- `PIPELINE`: `DEV/pipeline-repo`.
- `SOURCE`: `DEV/work/upstream-doom3-gpl-src/DOOM-3-master`.
- Unless explicitly marked GAME-relative, the paths below are DEV-relative.

Before wiping, replacing or losing access to this device, obtain a user-approved
**private** backup destination and preserve the inputs, derived roots,
manifests/receipts, original local diagnostics and historical counterexamples.
No destination has been selected or backup verified by this handoff.
Ask for one if needed; do not upload game content to public GitHub.

A backup is complete only after checking a content manifest against the
destination and restoring representative files. Preserve root structure,
source/archive membership, case, relevant timestamps and lookup order.
Do not delete old generations until their role in replay/provenance is resolved.
A private backup protects continuity but does not replace a raw-input recipe.

Separate what may be published:

- Public: our source/tools, synthetic fixtures, algorithms, commands, source
  hashes, archive/member identifiers, sanitized structural metadata and failures.
- Private: retail archives/disc images, decoded or converted maps/assets,
  extracted scripts, generated packages/trees, raw logs/captures and minidumps.
- Audit before publishing: local notes, diffs, receipts and diagnostic output.
  They can contain absolute paths, game text or memory data. Never upload
  credentials, private dumps, or blindly stage the whole work directory.

### Known dependencies that a Git clone alone does not supply

This is a starting inventory, **not** a complete minimal backup or dependency
closure. Expand it from actual manifests and the pinned drivers.

| Dependency | Role and required follow-up |
| --- | --- |
| `work/solo-overlays-nativefix-v39` | Immediate input to solo v40: 41 manifests plus MAP/PROC/CM/AAS, DEFs and selected resources. Trace its own generators/predecessors back to original inputs; copying v39 is not cold-start reproducibility. |
| GAME-relative `xbox_coop_port_strict_*_mergeguard_v20m` | Immediate input for all 20 co-op v20p overlays. Preserve explicit `--input-suffix mergeguard_v20m` and verify map identities, not just a count. |
| `work/solo-structural/maps/*/{core,decoded,reports,resources,models}` | Structural and resource recoveries, including original Enpro data and all AAS classes. Retain inventories and provenance receipts, not just final converted MAP files. |
| `work/retail-archives`, `work/shared-archives`, `work/shared-assets-extracted` | Original archive inputs and shared extraction products. Shared DEF catalog and `english.lang` / `english_vv.lang` are replay dependencies. Preserve GFC/GOB pair identity and extraction manifests. |
| `work/checkpoint-084-af-assets/base`, `work/checkpoint-084-enpro-af-assets/base`, `work/hazmat-runtime-assets/base` | Recovered authored ragdoll definitions and actor resources. Exact AF member extraction commands/hashes are in checkpoint 084/083 recipes. |
| `work/checkpoint-069-hellhole1-pc-cyber/retargeted/base`, `work/checkpoint-071-hellhole1-pc-cyber-pain/retargeted/base` | Derived Cyberdemon compatibility tracks, not raw decoded Xbox animations. Preserve the three retarget reports and reconstruct their exact inputs/settings. |
| `work/static-model-x-v1`, `work/static-model-x-solo-v1`, `work/static-model-x-solo-v2` | Extracted compiled Xbox static-model inputs (including `.lwo.x`) and extraction manifests. The overlay builder decodes these into ASE. Preserve per-member extraction and downstream decode recipes, versions and map-specific selection. |
| `work/runtime-deps-all`, `work/runtime-deps-xc_mars_city1_1`, `work/decoded-mdv-xc_mars_city1_1-v2` | Earlier decoded/extracted co-op resource roots. Determine exactly which emitted files still resolve here. |
| `work/npc-runtime-assets`, `work/player-runtime-assets`, `work/assets-materials`, `work/d3t-hud*` | Actor, material and texture roots. The wildcard is an inventory hint, not a reproducible selection rule. Enumerate exact directories and generators. |
| XACT roots | Preserve the solo driver's `XACT_ROOTS` in order, checkpoint 019–033 audio recoveries, `xact-first-map`, `solo-xact-audio`, and `xact-coop-xc_mars_city2_1-direct`, `xact-coop-xc_mars_city2_2-direct`, `xact-coop-xc_mcu-direct`. Read both pinned drivers for the full ordered list. |
| GAME-relative `base/*.pk4` | Licensed PC fallback/retarget inputs. Record edition, language, patch, exact PK4 hashes and virtual-filesystem precedence. This local base is not pristine: it also contains `z_doom3_xbox_mappack.pk4` and `z_doom3_xbox_mappack_menu_previews.pk4`. Do not delete them or silently treat their contributions as stock. |
| Prior profile paths and DEV tool mirror | Solo predecessor manifests reference 12 profile paths by absolute local path. Inventory and map each to its tracked source/hash. Moving machines otherwise breaks replay; verify the DEV mirror matches the pinned canonical tools. |
| Final and rejected artifacts | Preserve solo v40, co-op v20n/v20o/v20p, their receipts and earlier accepted outputs as distinct evidence. v20n and v20o must never be relabeled as accepted v20p packages. |

**Resource root order is semantic.** The accepted Cyberdemon retargets must
precede incompatible raw 50-joint inputs. Original Enpro 2 resources must
precede older overlays. Co-op Delta 2b part 2 must select its source-bound
50-joint ZCT family ahead of a prior PC-retargeted public family. Preserve
per-map ordered resolution; flattening folders can silently change results.

The known shared archive hashes are:

- GFC: `1fc9ba77a9e54589171d83d06bc14e6ae9feee10794401d6ffccff8dbb35f14f`
- GOB: `5c4395024835c42add37db51dfd74ca4ba3d160d81c20f106fb5294199ebc040`

These two hashes do not inventory all required original campaign/PC inputs.

## Preserve research instead of repeating it

Five local-only checkpoint diagnostic sources are now archived in the source
repository as `.py.txt`, with original names/hashes and LF-pinned checkout
attributes. All five snapshot hashes matched the original local files before
commit. They preserve independent Lantern bind math, actual AF consumers,
emitted-DEF resource demand and all-map geometry/provenance checks.

They are historical reference material, not portable executable tools.
Do not import them: all execute at module scope. They use version-specific
paths, mutable canonical imports and assertion-only gates. Never run them
with `python -O`. When promoting a check into supported tooling, parameterize
inputs, pin imports, fail explicitly, add synthetic regressions, and preserve
the independence of the countercheck.

Four other local helpers are hash-inventoried but **not archived** by this task:
`analyze_minidump.py`, `capture_crash.cpp`, `pdb_lookup.cpp`,
`collision_digest_snippet.cpp`. They are diagnostics/instrumentation, not
identified production conversion generators. Audit/private-backup them as
needed. `capture_crash.cpp` actively launches a debugger/EXE and overwrites a
dump; it is not offline-safe. Its window flag does not guarantee that a GUI
game stays in the background. Minidump analysis can expose private memory.
The collision snippet's command symbols were not found in current tracked
`neo/game`; do not assume the installed DLL implements them.

The bounded top-level helper inventory found **no missing production asset
generator**. That does not prove every manual step or ignored script has been
captured. Review local notes/diffs/history without indiscriminate publication.

## Work order for the next AI

Preservation comes first. After that, the existing v20p offline acceptance in
step 4 may proceed independently of steps 1–3; do not make it wait for the
longer clean-machine reproducibility project. Both tracks retain the same
no-gameplay/no-xemu boundary and must not modify each other's input artifacts.

### 1. Close the dependency graph before rebuilding everything

Start from every final file in all **41 solo + 20 co-op map identities** and
walk backwards through manifests, resource resolution and transform receipts.
For each dependency record:

- Logical input ID, exact relative/member path, bytes and SHA-256; original
  archive/disc identity, member offset/length where relevant, edition/language.
- Producer tool, source commit, exact arguments, ordered roots/profiles and
  toolchain versions; record an unresolved recipe explicitly if not located.
- Source-to-output mapping, every compatibility transform, expected output
  paths/hashes and independent validation; retained unknown bytes/failures.
- Whether the item is original input, generated intermediate, manually edited
  derivative, stock fallback, synthetic fixture or private diagnostic.

No derived v39/v20m directory may be treated as an unexplained terminal input.
Locate its existing recipe first; only recover missing steps after a documented
search. Use historical commits and receipts rather than guessing transforms.

Existing entry points already cover much of this:

- [Disc/archive extraction](REPRODUCE.md#disc-and-archive-extraction):
  `xdvdfs.py`, `doom3_campaign_port.py inventory/extract`, `gfc.py`.
- [Compiled map forms](REPRODUCE.md#decode-mapx-procx-aasx-and-cmx):
  MAP.X/PROC.X/CM.X/AAS.X decoders and offline `map_geometry_crc.py`.
- [Solo structural selection](REPRODUCE.md#xbox-single-player-structural-gate):
  all 41 archives and retained AAS classes.
- [Runtime assets](REPRODUCE.md#runtime-asset-conversion-and-overlay):
  model corpus/MDV/static-model decoders, retarget tools, `d3tfull.py`,
  `xact_audio.py`, `recover_solo_audio_corpus.py` and overlay assembly.
- [Current corrections](REPRODUCE.md#checkpoint-084-offline-only-corpus-review):
  AF extraction, actor-family checks, replay/package/audit stages.

Historical instructions describe old launch tests and may contain obsolete
counts/aliases. They are evidence, not permission to run those tests now.
Older CM instructions mentioning dmap are not required for the documented
offline geometry-CRC calculation.

### 2. Make that graph portable and fail closed

Deliver a versioned, metadata-only input lockfile and stage/recipe manifest,
then an orchestrator/preflight that consumes explicit root arguments.
These are required future deliverables, **not claimed to exist already**.

Preflight must report all missing or mismatched inputs before conversion.
Eliminate dependence on this drive/user, absolute predecessor-profile paths,
folder modification time and ambient untracked assets. Co-op discovery still
uses latest-manifest scanning even with explicit replay suffix selection:
verify the full identity set and replace nondeterministic discovery deliberately.

Record Python and dependency versions; the current offline tools generally use
Python 3.10+ and the standard library, with optional Capstone for XBE work.
Native MSBuild/v145 compilation is a separate stage, not a converter requirement.
Record case handling, line endings, PK4 precedence and resource-root ordering.

Convert any genuinely manual edits into narrowly scoped, hash/expected-count
guarded, idempotent transforms with synthetic tests. Preserve source data and
counterexamples; do not “fix” warnings by deleting entities, animations,
navigation or checksum evidence.

### 3. Prove a clean, offline reconstruction

In a fresh isolated output workspace, use only pinned repositories and
authenticated original licensed inputs. No copied accepted overlays, prior
decoded roots, unnoticed DEV mirror, hidden cache or existing installed mod
may supply outputs. Run documented stages for all 61 map identities.

Compare output payload hashes/ledgers against preserved baselines. Receipt
bytes may differ because of absolute paths or timestamps; separate normalized
provenance fields from payload identity. Investigate every payload difference
and record the reason; do not normalize away content differences.

Run structural, resource, actor/AF, script/GUI reference, merge, MD5 and
MAP/CM/AAS identity gates. Preserve known failures explicitly. A reproducible
known defect is still a defect, but its reproduction does not require inventing
a fake success. At completion another machine/AI should need execution of saved
recipes, not rediscovery of binary formats or recovery decisions.

### 4. Finish checkpoint 084's pending offline acceptance

On this device, after preservation, the shortest resume path starts at the
**v20p co-op overlay audit**, not another v20p rebuild into existing directories.
Verify all 20 selected suffixes and identities. Then make fresh co-op package,
separate tree, strict-tree/merge/MD5/CRC receipts using the saved commands.

At stop, `work/coop-pkg-mg20p` and
`work/campaign-coop-test-tree-v32` did not exist; recheck before writing.
The completed v20p rebuild and independent geometry proof do not substitute
for those missing gates. Solo v40's strict tree and MD5 checks passed, but its
separate Comm Outside 1 AAS96 identity gate remains failed.

Keep solo/co-op packaging separate: shared virtual paths can have different
payloads. Do not combine both modes into one mod by copying over conflicts.

### 5. Correct real remaining defects, without overstating evidence

| Open item | Required next action / boundary |
| --- | --- |
| Current master cannot select COOP normally | Audit/integrate the older COOP lineage's game-type enum/cvar/resolver, paired player definitions and dependent AI/network/checkpoint behavior with the new map-host classes. A label-only patch or stock deathmatch loader run is insufficient. |
| Comm Outside 1 AAS96 | Original header CRC 2127086718 differs from MAP/CM/AAS48 1317835462. Determine which component/variant is stale. Never stamp the AAS header to conceal the mismatch. |
| Enpro head | Required copy destination `eyecontrol` is absent from the selected head family. Body/AF success does not close this head compatibility issue. |
| Five declared jumpsuit clips | `influence_eats_arm`, `influence_shake`, `influence_shake_random`, `startchainsaw3`, `thrownbyhk` remain absent. Establish exact source availability/reachability; do not fabricate substitute acceptance. |
| Script/GUI/resource warnings | Resolve unsupported time/Off events, missing GUI transition destinations, dangling Delta 4 callback, `sonicips.ips`, and source-absent `recycwallight_broken.ase` from recorded cases. Distinguish absent sources from conversion bugs. |
| Delta 4 Hazmat | Complete source-bound skeleton/AF work is recorded; runtime disappearance of all warnings and cinematic behavior is not proved. Do not undo the family repair to silence remaining unrelated warnings. |
| CPU 2 Sabaoth | Complete 50-joint mesh/13-animation family is recorded. Bounds-search routes to areas 23/36 from 10 do not prove tracedown, dynamic obstacles or full `WalkPathToGoal`. |
| Whole-campaign acceptance | Physics, scripts/progression, save/load, audio/visual fidelity and two-peer play remain separate unaccepted gates. No offline-only “100% working” claim. |

Use the 38-family historical warning inventory across 61 maps, not only
error/fatal lines or the two originally requested warning families.

### 6. Later work requires the user's test decision

The current instruction remains **no gameplay tests or xemu comparisons**.
Do not launch Doom, Steam, dmap or crash-capture helpers during this handoff.
Do not restart the older one-minute-per-level plan without renewed permission.
Window minimization is not proof that a launch will not steal the user's focus.

When the user authorizes tests, propose a controlled test window and isolate
save/config/output state. Loader survival, two-peer functionality, complete
playthrough and matched-reference visual comparisons are distinct gates.

Preserve the user's later research requests without mixing them into the
original port:

- First, a read-only Xbox-versus-PC map/event difference catalog, including
  split-map layout and timing, shotgun trap timing, the Z-sec/scientist scene,
  Campbell/Archvile BFG scene and any further unique scenes found. These user
  examples are research leads, not equivalence claims.
- An optional PC-quality asset mode with exact mapping, skeleton/animation
  compatibility and explicit unsupported substitutions. Keep original Xbox
  assets/presentation available and unmodified. Document unavoidable fallbacks.
- Transferring co-op logic into larger PC maps is a separate future project,
  initially investigation only; do not silently replace original Xbox geometry.

## Definition of a defensible handoff

- [x] Recorded tracked checkpoint commits were pushed and verified.
- [x] Current resume state and known failures are public metadata.
- [x] Five unique local diagnostic sources are preserved byte-for-byte.
- [x] Known incremental dependencies and correction work are explicitly listed.
- [ ] Complete local-only knowledge/dependency inventory finished.
- [ ] User-approved private backup copied and restore-verified.
- [ ] Every derived input has an exact versioned raw-input recipe.
- [ ] Fresh-machine offline reconstruction demonstrated for all 61 identities.
- [ ] Final v20p co-op package/tree acceptance finished.
- [ ] Remaining functional defects corrected and their evidence recorded.
- [ ] User-authorized gameplay/two-peer/fidelity acceptance completed.

If only the checked items are true, report **“documented and source preserved;
clean-machine reproducibility and gameplay acceptance remain unproved.”**
Do not report “all local work backed up,” “perfect re-port guaranteed,” or
“100% complete.”
