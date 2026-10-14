# Recovery order and acceptance

## Checkpoint 016 third-segment status

`xc_mars_city2_2` passes the same structural and bounded loader/spawn gates as
the preceding segment. Direct CM.X is bound to the MAP CRC, every authored
model is present in independent PC `dmap`, and all 42 PC-only models are
explained by `noclipmodel 1`. Corrected AAS48 is used.

The shared player profile closes inherited player dependencies. The sole new
map dependency, `lights/nofalloff`, is recovered by logical name from the Xbox
global D3TFULL and placed beneath the already-existing stock PC material. The
276-file overlay has zero unresolved resources or classnames. A bounded true
`COOP` run produces 516/0, joins the player, and has no missing-resource,
skeleton, path, error or fatal line.

This accepts third-segment packaging and the loader/spawn boundary only. It
still uses the isolated null-guard diagnostic; a reviewed source change and
normal DLL rebuild remain mandatory. Dynamic combat, scripted progression,
segment transition, two peers and original-Xbox comparison remain open.

## Checkpoint 015 second-map closure status

The second-map packaging and bounded loader/spawn gates now pass. The accepted
navigation payload is the corrected plane-distance AAS48, not the obsolete
checkpoint-014 copy. The diagnosed zsec route resolves offline through areas
`41→39→38→37→35→34`, and the corresponding native warning disappears.

The shared player profile closes all inherited model, animation, AF, skeleton
and HUD dependencies without pulling in first-map NPC or cinematic data. The
only nonexistent requested image is the armor-shard inventory icon; archive
inventories prove it was not shipped, and an exact receipt-bearing transform
removes only that presentation epair. The final local overlay has 279 file
records, zero unresolved resources/classnames, and passes all 148 tests.

Under the isolated null-guard control-flow diagnostic with original
`net_instanthit` declarations, true `COOP` spawns all 1,110 entities, inhibits
none, joins the player, and emits zero missing-resource, skeleton, AI-path,
error or fatal lines. This accepts the resource and navigation closure, not the
game DLL: the next hard gate remains a reviewed `AI.cpp` null guard, normal
rebuild, and repetition of the same result. Combat, whole-segment progression,
transition and two-peer behavior remain unaccepted.

## Checkpoint 014 second-map status

The second co-op segment has passed structural export and the native compiled-
map loader. Direct CM.X expands to 219 authored collision models at the exact
MAP CRC, and independent PC `dmap` contains all of them. The 93 PC-only models
are exactly the entities carrying `noclipmodel 1`, so the model-set difference
has a complete MAP-authored explanation.

Runtime acceptance is not yet granted. The original declarations trigger a
deterministic source bug: the reconstructed instant-hit path makes
`idAI::CreateProjectile` return null while `idAI::Spawn` unconditionally probes
that projectile's physics. A temporary flag-only diagnostic proves the boundary
by spawning all 1,110 entities with zero inhibited, but changing Xbox
`net_instanthit` semantics is not a fidelity fix. Acceptance requires a rebuilt
DLL with the narrow null guard and the original declarations unchanged.
An isolated binary control-flow diagnostic has now exercised exactly that guard
with the original declarations and also produced 1,110/0 plus exit 0. This is
strong fault-boundary evidence, not a replacement for a reviewed source change
and normal build receipt.

The current 50-file closure is also incomplete despite reporting no unresolved
map-root dependency. Native loading identifies inherited player dependencies:
the ladder animation, seven HUD item images, `model_sp_marine`, and the player
skeleton needed for `bone_hips`. The next gate is: original instant-hit values,
source-guarded DLL, complete player dependency closure, 1,110/0 spawn result,
local player creation with zero errors, and no missing resource lines. Combat,
whole-map progression and two-peer behavior remain later gates.

## Checkpoint 013 runtime-overlay status

The first-map runtime overlay now stages the direct Xbox-authored CM through a
reproducible builder option rather than an undocumented manual swap. Acceptance
requires the complete PC-generated map set, an exact authored filename, ASCII
PC CM syntax, and equal embedded MAP CRCs. The manifest identifies
`direct-authored-cm` and retains byte/hash receipts for both the generated and
authored inputs. Malformed or mismatched input must leave no output overlay.

`xc_mars_city1_1` passes this gate: its 374-file overlay has no unresolved
resources or classnames, the authored CM is byte-exact to the direct export,
and a true-`COOP` native load spawns 940 entities with none inhibited and no
error, fatal or missing-resource warning. The 147-test local suite also passes.

This is runtime packaging and loader acceptance only. Collision acceptance
still requires equivalent native coverage for all remaining co-op maps plus
moving/rotated clips, trigger side effects, actor/projectile hulls and two-peer
progression. It does not establish a playthrough or original-Xbox behavioral
equivalence.


## Checkpoint 012 collision status

The first-map collision gate now includes actual spawned entity clip placements,
not only model-zero and named-model queries. Generated and authored runs resolve
the same door clip, co-op trigger and brush static at identical origins, axes,
bounds, masks and sample coordinates. All 24,576 hit outcomes match.

This still rejects PC-`dmap` collision for fidelity acceptance. The live
profiles expose 3,367 contact-manifold mismatches, one trajectory mismatch, 97
material-selection mismatches and 11 point start-contents differences. Matching
hit counts are insufficient: player movement, response points, trigger contact
and surface-dependent behavior can observe the remaining differences.

For the PC overlay, the accepted implementation direction is now direct decoded
CM.X, with PC `dmap` retained as a diagnostic comparison only. The collision
gate is not complete until the same native evidence covers every co-op CM and
exercises moving/rotated clips, trigger dispatch, representative actor and
projectile hulls, and two peers. Original-Xbox runtime comparison remains the
highest-confidence reference when it becomes available.

## Checkpoint 011 collision status

The first-map static collision gate now covers world player, monster and rocket
semantics plus representative named door, trigger and polygon-only static
models. The oracle binds model identity, mask, hull, bounds and coordinates;
all 40,960 paired records have matching input context and hit outcomes.

This advances acceptance in three ways:

- direct CM.X is confirmed as the required world payload under player,
  monster-solid and shot masks;
- named CM identity, bounds and broad blocking are measured rather than inferred
  from matching model names;
- trajectory, contact manifold, material/contents and stable topology are
  reported separately, so contact-only divergence cannot be hidden by equal hit
  counts.

It does not accept PC-`dmap` collision. The five profiles contain 3,507
gameplay mismatches: 121 stopping trajectories, 2,741 contact geometries and
875 metadata results. Door and trigger trajectories happen to match, but their
contact manifolds do not; the complex named static differs in both. Direct
authored CM remains the runtime candidate.

The next collision gates are live mover transforms and trigger dispatch,
actor-specific monster hulls and rotated projectile hulls, then identical native
coverage for the remaining 19 co-op map CMs. An original-Xbox runtime oracle
and two-peer contact/trigger outcomes remain required for fidelity acceptance.


## Checkpoint 010 collision status

The first map now passes a deterministic authored-versus-generated world-trace
comparison gate, but the result is deliberately a non-equivalence finding:
PC-`dmap` collision cannot be accepted as the Xbox fidelity payload.

The comparison controls for bounds, seed, query coordinates, PC collision
algorithm and trace shape. It proves equal record coverage and equal hit/no-hit
counts. It also finds 265 player-box geometry differences and 501
material/contents differences. Therefore:

- the direct CM.X export is the required runtime candidate;
- PC `dmap` remains an independent parser/geometry cross-check only;
- matching broad counts or hit totals is insufficient acceptance;
- contact material/contents are fidelity fields because they drive clip masks,
  impact effects and surface behavior;
- point-ray agreement does not waive player-hull testing.

First-map world collision is now source-bound and natively measured, but it is
not fully accepted. The next collision gates are shared named collision models,
monster/projectile masks, movers and triggers, then the same deterministic
ledger on the remaining co-op maps. Original-Xbox runtime evidence and two-peer
contact outcomes remain required before final fidelity acceptance.



## Checkpoint 009 collision status

Direct Xbox collision is now structurally decoded across the complete extracted
co-op corpus and loader-checked on the first segment. That advances collision
from PC-regenerated fallback to authored-data loader acceptance for
`xc_mars_city1_1`; it does not yet advance that map to collision-fidelity
acceptance.

A map's collision gate requires all of the following:

- the CM.X input and exported CM are bound to exact hashes and the converted
  MAP geometry CRC;
- all models, vertices, edges, planes, brushes, polygons and BSP nodes parse
  with complete byte consumption and valid cross-references;
- every polygon and brush is reachable from the authored BSP;
- the native PC loader accepts the direct CM without regeneration or fallback;
- representative world, clip, trigger, mover, projectile and actor traces are
  compared against an Xbox reference or another source-bound oracle;
- multiplayer host/client contact and trigger outcomes agree for the co-op
  slice.

The first map satisfies the first four bullets. Native trace equivalence,
two-peer contacts and all-map loading remain open. The 342-reference difference
between stored Xbox and PC-reconstructed polygon-node lists is explicitly
tracked; it may be acceleration-only, but must not be silently declared
irrelevant before trace testing.

## Checkpoint 008 acceptance state

The first co-op segment now passes the bounded single-host navigation,
dependency and true-`COOP` startup gate. The corrected AAS48, exact
runtime-tested source DLL and manifest-bound overlay start a listen server,
create the local player, load all 940 entities and shut down cleanly. The
bounded log contains zero missing images, models, animations or sounds; zero
spawnclass, GUI-command or material-token failures; zero AI path warnings; and
zero error or fatal lines.

The five checkpoint-007 path failures were caused by AAS plane serialization,
not missing reachability chains or dynamic obstacles. Xbox `xboxData` stores
the internal `idPlane` fourth component, while standard PC AAS text stores
`Dist() == -d`. Negating that component during export restores native
point-to-area lookup. The matching auditor correction and nonzero-distance
fixtures prevent the earlier decoder/auditor sign errors from masking one
another.

This accepts first-map navigation only for the observed bounded startup slice.
It does not yet accept a second peer, encounter progression, doors throughout
the playable segment, death/rejoin, checkpoint behavior, transition behavior,
direct CM.X collision recovery, Xbox visual parity or the remaining co-op and
solo corpus. The next scalable gate is corpus-wide corrected-AAS validation
and all-map dependency closure, followed by a focused two-peer progression run
once the offline obligations for that slice are complete.

## Previous checkpoint: 007 acceptance state

The first co-op segment now passes the single-host true-`COOP` startup gate.
The exact checkpoint DLL starts a listen server, creates the local networked
player, loads all 940 entities, reports zero inhibited entities and exits
cleanly. No missing spawnclass, HUD image, GUI script command, material token,
engine error or fatal error remains in the bounded log.

This gate also establishes a PC-safe rendering path for the Xbox co-op status
message and a selective HUD/material closure. It does not establish a second
peer: `Server: Player joined the game.` in this run is the local listen-server
player. Initial player-one/player-two spawn selection, remote snapshot exchange,
death/rejoin and synchronized progression remain unaccepted until two distinct
peers are observed.

Five NPC/path-corner warnings remain. Every pair has a static directed route in
the recovered AAS48, so navigation edits are not justified yet. The next
diagnostic gate must capture the runtime start/goal area chosen with the actor's
actual bounds and travel flags, plus dynamic door/obstacle state at the warning
time. After that, run two peers through the first segment's spawn, GUI sync,
Turkey Puncher event, checkpoint, death/respawn and transition sequence.

Direct CM.X recovery, all-map dependency closure, matched Xbox
visual/gameplay comparison and the solo campaign remain separate obligations.

## Previous checkpoint: 006 acceptance state

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

