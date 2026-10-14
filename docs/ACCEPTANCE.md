# Recovery order and acceptance

## Checkpoint 006 acceptance state

The first co-op segment now passes the source-runtime spawn gate. A complete
Win32 `gamex86.dll` build and the 103-test recovery suite pass in CI. The exact
CI DLL, loaded through Doom 3's executable-directory development path, spawns
all 940 map entities with no inhibited entities and no missing Xbox-only
spawnclass. The bounded load exits normally.

This moves the acceptance boundary to dynamic navigation and actual co-op
behavior. Five unique NPC/path-corner failures remain even though the recovered
AAS contains directed walk routes for every pair. Investigate actor bounds,
door/obstacle enablement, AAS obstacle removal and script timing before editing
or regenerating navigation.

The next runtime gate is two simultaneous peers: initial spawn selection,
trigger synchronization, Turkey Puncher score/event replication, checkpoint
advance, death/respawn and segment transition. Direct CM.X recovery and matched
Xbox visual/gameplay comparison remain separate fidelity obligations.

## Previous checkpoint: 005 acceptance state

The first co-op segment has crossed the dependency-resolution and stock-loader
boundary: decoded geometry/AAS, selected models/animations, HUD images, sounds,
language data and script callbacks load together. The exact skeleton alias is
natively confirmed. This is still below source-runtime acceptance because the
retail PC DLL cannot instantiate the reconstructed Xbox-only classes.

The next acceptance gate is a Windows build of the implementation PR followed
by the same bounded load. It must prove registration and behavior of GUI sync,
door sync, spawn-level, enable-GUI and Turkey Puncher entities and then revisit
the five dynamic AI path failures. Only after that gate should two-peer spawn,
death/rejoin, synchronized progression and segment transition testing begin.

Static AAS routes exist for every warned pair, so regeneration or hand-editing
reachabilities is not currently justified. Dynamic obstacle/door state must be
measured first. Collision remains PC `dmap` output; direct CM.X recovery remains
a separate fidelity obligation.

## Deliverable, not a substitute

The target is the original-Xbox campaign content on the PC source host, with
co-op first and solo ultimately complete. The existing PC-map co-op runtime is
a useful host baseline; it does not count as ported Xbox campaign content.
Converted Xbox MP maps are calibration/reference inputs only.

Do not change or relabel accepted historical engine/frontend profiles. Future
Xbox-map selection belongs in an isolated successor profile that fails clearly
when its required Xbox map is absent. Stock-PC map alias fallback must not hide
failed conversion in that profile. The current tooling commit makes no runtime
selection change.

## Ordered work

Start with the complete archive inventory and exact build identity. Recover
actual co-op/solo registry entries and dependencies before assigning map counts
or announcing coverage. Establish a matched original/converted MP pair, recover
one genuine co-op map through every data layer, then generalize to additional
maps and the solo campaign. Keep original segment boundaries and transitions
until evidence establishes whether and how they can be combined faithfully.

For each payload family, document fields and unknown spans before implementing
conversion. Bind recovered values to source hash/offset and generated output.
Require consistent counts, ranges and cross-references, then independent
comparison. MP-derived format assumptions must survive checks against actual
campaign files before being accepted as shared.

Do not reconstruct original brushes from triangle soup and call them recovered
source. Exact editable-source recovery and faithful compiled-runtime recovery
are separate deliverables; track both and label reconstructed data explicitly.

## Per-map evidence matrix

Create rows only from the actual campaign inventory. There are no fabricated
map rows or estimated retail map counts in checkpoint 001. Each real row must
bind the source hashes, output hashes and producing tool/engine commits.

| Layer | Required evidence |
| --- | --- |
| Identity | Correct Xbox build, campaign mode, map/segment registry and dependencies |
| Render geometry | Complete surfaces, positions, UVs, normals, winding, index ranges and transforms |
| Materials/models | Correct resolved resources and shader behavior; no silent defaults |
| Visibility | Area models, portals, BSP leaves/links and authored portal controls |
| Collision | World and entity collision, clips, contents/surface flags, movers and trigger volumes |
| Navigation | Valid walk/fly data and reachability or explicitly verified regeneration |
| Entities/scripts | Names, transforms, targets, definitions, script entry points, timing and state transitions |
| Co-op | Both players, spawn/respawn placement, synchronized encounters, death/rejoin and shared progression |
| Campaign flow | Correct starts, exits, segment changes, persistent state, checkpoints/save-load where applicable |
| Fidelity | Matched Xbox observations plus PC solo and two-peer results, with declared tolerances |

A row can be observed, partially decoded, decoded, exported, statically checked,
loader-checked, or fidelity-accepted. Do not collapse these into one percentage.
An unsupported field is not complete because a default lets the engine run.

## Near-final test readiness

Before a substantial user playtest, finish the defined offline obligations for
the intended test slice: established layouts, deterministic export, complete
asset resolution, collision/nav availability, valid entity/script references,
co-op spawn and progression wiring, and no known critical conversion blocker.
Retain all unresolved noncritical differences and explain why they are outside
the slice or acceptable for this test.

Cheap unit/parser checks should run during implementation. They prevent bad
assumptions spreading to every map without demanding repeated user playtests.
A focused engine load then checks the real loader boundary. Only after that
should the user be asked to spend time on a meaningful co-op fidelity test.
Doing substantial work first is compatible with this ordering; claiming 95%
without measured obligations is not.

## Final acceptance

Static checks alone cannot establish exact gameplay, contact/collision behavior,
visibility, lighting, timed scripts or two-peer progression. Final acceptance
requires actual Xbox-reference comparison and PC execution for the complete
agreed corpus, including every co-op and solo map/transition in scope.

Bind every run to exact binaries, data manifests and inputs. Compare equivalent
camera/state/timing conditions and distinguish renderer differences from wrong
content. Keep separate tolerances for positions, normals, UVs, timing and images;
do not introduce an undocumented global tolerance just to make a comparison
pass. Any intentionally different PC-host behavior requires an explicit waiver,
not a silent fidelity claim.

Checkpoint 001 completes none of these retail per-map acceptance rows. It adds
recovery instruments and reproducibility documentation, with 46 synthetic
checks and no retail campaign files. The next substantive milestone is a
source-bound decode of an actual co-op map, not another menu milestone.

