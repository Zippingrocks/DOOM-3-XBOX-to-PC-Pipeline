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

## Start on another machine

[Next-machine quickstart](docs/NEXT_MACHINE_QUICKSTART.md) provides exact clone,
pin, verification and original-input recovery commands. It requires licensed
originals, not these device-local ports. No converted assets are uploaded.

**Newer checkpoint:** [087 original-input reconstruction](docs/CHECKPOINT_087_RAW_RECONSTRUCTION.md)
adds deterministic numeric output, exact shared-resource and audio/texture
recipes, and checked runners. Use its newer resource toolchain lock. Authentic
fresh reconstruction is in progress; do not interpret Git synchronization as
final-overlay or gameplay acceptance.

## Checkpoint 086: verify and run the portable recovery kit

[Start here: portable recovery verification](docs/CHECKPOINT_086_PORTABLE_RECOVERY.md).
The pipeline now pins every recovery tool/profile and supplies one asset-free
checkout verifier, Windows/Linux CI, and an opt-in raw structural runner in
the source repository. The runner defaults to read-only preflight, accepts no
old ports, and checks available output witnesses. No game data is uploaded.
Fresh GitHub clones pass 553 source and 6 pipeline tests locally. Cloud CI
currently needs an owner-configured read token for the private reconstruction
repository; its initial checkout failure is documented, not reported as a pass.

This strengthens the 61-map recovery path; it does not yet complete the shared
resource/initial-overlay composition or prove final payload equivalence on a
fresh machine. See the checkpoint for exact commands and remaining boundaries.

## Checkpoint 085: asset-free recovery for another machine

[Preserved metadata and raw-input recipes](docs/CHECKPOINT_085_ASSET_FREE_RECOVERY.md).
The user cannot transfer the old converted ports. Git now preserves a
1,660-file metadata lock (1,480 sanitized receipts), all nine local diagnostic
sources, exact solo/co-op raw-input recipes and 525 structural-plan steps for
all 61 maps / 90 AAS files. No game assets are included. Source portability
fixes pass 501 offline tests.

The plan runs from metadata alone and does not require predecessor ports.
Executing its conversion steps still requires licensed original inputs.
Final overlay composition and end-to-end clean-machine equivalence remain
unfinished; this is not a 100% reproducibility or gameplay claim.

## Device transition: reproducibility is not yet proved

Read the [next-AI correction plan](docs/REPRODUCIBILITY_RECOVERY_PLAN.md) before
resuming. Tracked checkpoint work is pushed, but the current replay recipes
still require device-local predecessor overlays and recovered asset roots.
A Git clone plus original inputs has not yet been proved sufficient for a
clean-machine rebuild. No private asset backup is claimed.

The handoff lists preservation priorities, exact known dependencies, remaining
defects and acceptance gates. Five formerly local-only diagnostic sources are
now archived in the source repository; no game or long rebuild was run for
this documentation/preservation step.

## Current review: 084 — broader offline checks, explicit host blockers

The complete 41-map solo and 20-map co-op historical logs have now been
inventoried with their recorded hashes verified. Broad warning classification
exposes defects missed by earlier focused warning filters; zero error/fatal
lines did **not** mean zero missing actors, callbacks or navigation problems.
No game, Steam, dmap or xemu process is launched during this review.

**The current reconstructed source branch is not a validated co-op host.**
Its normal game-type enumeration/resolver cannot select COOP, despite containing
a paired-spawn branch. Historical loader configurations actually selected a
stock multiplayer mode. The older source repository `main` lineage contains
the broader COOP implementation, but it does not contain every new map-host
fix; neither tree can safely replace the other wholesale. Integration and
later two-peer acceptance remain mandatory.

The new companion-checksum gate also identifies one source-authored mismatch:
Comm Outside 1's AAS96 checksum differs from its MAP/CM/AAS48 checksum. It is
retained, not masked by stamping a new checksum onto potentially stale routes.
All 20 co-op maps pass this particular identity gate. A matching checksum is
still not proof of navigation or progression fidelity.

See [the offline-review findings](docs/FORMAT_FINDINGS.md#checkpoint-084-broader-offline-review)
and [acceptance boundaries](docs/ACCEPTANCE.md#checkpoint-084-no-runtime-acceptance).
**Stopped for the user's immediate handoff request.** All 460 offline tests
pass; the source fixes are pushed through `c61e370`. Solo v40 passes its strict
41-map tree audit (994 files) and 244 loose-MD5 checks. All 20 final co-op v20p
overlays rebuilt, and independent geometry/resource-scope checks pass, but its
final package/tree audit chain was stopped before completion. Do not treat
that final package as accepted. No 100% or warning-free runtime claim is made.

See [the resume handoff](docs/CHECKPOINT_084_HANDOFF.md),
[checkpoint evidence](evidence/checkpoint-084-offline-corpus-review.json), and
[reproduction commands](docs/REPRODUCE.md#checkpoint-084-offline-only-corpus-review).

## Earlier checkpoint: 083 — offline warning-family repairs

**Delta 4 Hazmat and CPU 2 Sabaoth now have complete source-bound skeleton
families, verified offline.** Hazmat uses its 48-joint Xbox mesh, matching
inherited animation slots/channels and two recovered Xbox ragdoll definitions.
Sabaoth uses its 50-joint Xbox mesh and all 13 animations, including four pain
tracks absent from PC data. Public PC families are left intact.

The review also fixed GUI metadata being precached as numeric filenames,
unchecked package receipt hashes, a script-include audit false pass, and native
soak exit/resume integrity bugs. A new independent MD5-family auditor checks
exact animation hierarchy and engine-compatible AF/actor joint lookup rules.
All 364 offline tests pass. The 41-map solo corpus was rebuilt and audited;
the unchanged 20-map co-op tree was reaudited. The source DLL compiles in an
isolated output directory without replacing either installed or accepted DLL.
See [`evidence/checkpoint-083-offline-warning-families.json`](evidence/checkpoint-083-offline-warning-families.json)
and [reproduction instructions](docs/REPRODUCE.md#checkpoint-083-offline-only-review).

**No Doom 3, Steam or xemu launch, gameplay test, or Xbox comparison was
performed for this checkpoint.** Runtime warning disappearance is not yet
accepted. Sabaoth's separate path-corner warnings, Xbox GUI distance/zoom
behavior, progression, two-peer behavior and visual fidelity remain open.
Solo/co-op remain separate mod trees: their packages are individually mergeable
but eleven shared paths differ between modes. GitHub synchronization requires
working authentication; the local commits and evidence are preserved.

## Earlier checkpoint: 082

**The source-bound Xbox Sentry and maintenance-zombie skeleton families are
now coherent on the PC host.** The Xbox families each use 50 joints, while the
stock PC Sentry and maintenance-zombie meshes at the same public paths use 55
and 90. Publishing only the previously missing Xbox animations therefore
created deterministic joint-count failures. The accepted overlays instead
place complete Xbox mesh/animation families beneath private runtime prefixes
and rewrite only the Xbox declarations that select them. Communications also
routes its two map-specific Sentry loader clips into that private family.

The isolated v36 tree contains all 41 solo maps, 910 files and 744,464,216
bytes. It has zero missing compiled companion, duplicate declaration/material,
untracked file or reparse point. All 336 offline tests pass. The nine affected
maps pass minimized direct-host focus loads with zero missing Sentry/zmaint
animation, defaulted model, missing model, unknown look joint, joint-count
mismatch, failed spawn, error or fatal line. The rejected public-path v33 and
incomplete-private-family v35 candidates are retained as counterexamples. See
[`evidence/checkpoint-082-private-actor-families.json`](evidence/checkpoint-082-private-actor-families.json).

This closes the observed loader/model-definition warnings for these two
families. It does not replace visual, animation-event, progression, save/load
or full playthrough acceptance.

## Earlier checkpoint: 081

**All Xbox texture-separator entities now survive on the GPL PC host, and the
complete 61-map route is clean under the rebuilt DLL.** The Xbox maps use
`info_textureseparator` to open or close client-local texture-streaming flow
through a portal. The GPL PC renderer has no corresponding portal-streaming
API, so the source reconstruction registers the exact Xbox spawnclass,
preserves every entity/name/target relationship, and consumes activation as an
intentional no-op. It does not delete the entities or invent renderer state.

The new Dedicated Release `gamex86.dll` hashes to
`cd85078bf3f5ce8cd4937baae48e70049a8056db59c95033bf76ee122d9ca774`.
On the minimized direct host, all 41 v32 solo segments and all 20 v30 co-op
segments spawned and idled for at least ten seconds: 61 passed, zero failed,
zero error/fatal line and zero abort. A separate full-log audit finds zero
`info_textureseparator`, `idTextureSeparatorEntity` or `Could not spawn` line;
the prior v30 solo baseline contained 276 failed separator spawns. The invalid
Dedicated Release `map` invocation is retained as counterevidence; accepted
automation uses `spawnServer`. See
[`evidence/checkpoint-081-texture-separator-host.json`](evidence/checkpoint-081-texture-separator-host.json).

This closes the observed separator spawn/runtime gap, not matched-Xbox texture
residency behavior: PC loads textures through its native renderer rather than
emulating the removed Xbox streaming boundary. Visual, progression, save/load
and two-peer acceptance remain open.

## Earlier checkpoint: 080

**Sixteen more exact Xbox static models close every source-present solo
missing-render warning.** Full per-map GFC inventories recovered the Alpha Labs
maggot-room cuts, both Comm Outside terrain models, Monorail's no-glass tram
and pillow, and all ten warned Hell 1 part-3 pieces. Together with checkpoint
078, 27 unique compiled Xbox static models now have source-bound PC ASE routes.

The decoder now covers two authenticated edge cases without weakening its
fail-closed structure checks: an exporter label such as `material #97`, and an
authored empty material surface carrying the canonical +1e30/-1e30 bounds
sentinel. Empty slots remain in the ASE material table and decode report but
do not become empty `GEOMOBJECT`s, which the stock PC ASE reader rejects.

The isolated v32 solo tree has 41 maps and zero unresolved dependency, missing
compiled companion, duplicate declaration/material, untracked file or reparse
point. Alpha Labs 1, Comm Outside 1/2, Monorail 1/2 and Hell 1 part 3 all load
on the minimized direct GPL host with zero error/fatal or missing-model line.
The five non-Hell maps passed the first candidate; Hell 1 exposed and verified
the empty-surface rule before all six passed v32. The only campaign-wide warned
static path still known absent from both Xbox and stock PC is
`recycwallight_broken.ase`. See
[`evidence/checkpoint-080-solo-static-model-closure.json`](evidence/checkpoint-080-solo-static-model-closure.json).

## Earlier checkpoint: 079

**The final isolated v30 trees pass a fresh 61/61 one-minute native sweep.**
All 41 solo segments and all 20 co-op segments spawned on the minimized direct
GPL host, idled for at least 60.046 seconds, and recorded zero error/fatal line,
failed map, premature-exit classification or abort. The recovered static-model
paths and ASE bitmap-path warnings remain zero across the full logs.

The co-op log is now narrow: its only missing-render warning is the three
instances of stock/source-absent `recycwallight_broken.ase`; it has no missing
class, skeleton mismatch, unknown-joint or no-model warning. Solo is loader
clean but not warning clean: its remaining missing render models, texture
separators, sentry/monster modelDefs/joints and empty-key warnings are the next
porting queue before visual acceptance. See
[`evidence/checkpoint-079-full-native-soak.json`](evidence/checkpoint-079-full-native-soak.json).

## Earlier checkpoint: 078

Eleven exact Xbox compiled static models are now decoded to PC ASE, and all
eight affected solo/co-op focus loads are clean.** Full GFC inventory corrected
checkpoint 077's selective-extraction conclusion: the archives do contain the
renderer-compiled `.lwo.x`/`.ase.x` payloads for the keycard, co-op Caverns,
Site 3 and Hellhole props plus four additional solo-only Site 3/Hellhole props.
A strict decoder preserves surfaces, materials, indexed geometry, UVs, normals
and RGB vertex colors while hash-binding renderer-derived opaque spans.

The isolated v30 trees contain 41 solo and 20 co-op maps with zero unresolved
dependency, missing compiled companion, duplicate declaration/material,
untracked file or reparse point. Comm1, Site 3, Caverns 1 and Hellhole pass in
both corpora on the minimized direct GPL host: 8/8 spawned, idled at least ten
seconds and produced zero error/fatal lines. Targeted missing-model and ASE
bitmap-path warnings are zero. All 330 offline tests pass. The previously clean
v26 41/41 solo and 20/20 co-op minute soaks remain the broad baseline; fresh
v30 one-minute sweeps are the next gate before visual/two-peer acceptance. See
[`evidence/checkpoint-078-static-model-decoder.json`](evidence/checkpoint-078-static-model-decoder.json).

## Earlier checkpoint: 077

Checkpoint 077 completed the fresh 20/20 co-op one-minute native soak and
closed the remaining observed Commando and Guardian joint warnings. Its claim
that eight render paths were absent is superseded by checkpoint 078: that claim
described the earlier selective extraction, not the full GFC inventory.

## Earlier checkpoint: 076

**The six Xbox-only co-op gameplay classes that were missing from the GPL PC
DLL are reconstructed, source-built and clean across the complete 20-map
route.** The source implementation restores paired spawn-level progression,
networked static-GUI and door-GUI state, the all-active-player GUI trigger,
collision-safe repeatable teleport selection, and per-player Turkey Puncher
score replication. The exact source delta is committed locally as `d1ae7b2`
on a pristine GPL archive baseline.

The rebuilt 32-bit Dedicated Release `gamex86.dll` hashes to
`cc9455c2fbe3ce54120a452eb19b2fda62db273e17f4f2a3937a591b872fcd68`.
With that DLL, all 20 co-op segments loaded in minimized direct-host runs,
reached entity spawn, idled at least 60 seconds, and exited with zero errors,
fatals or premature exits. A second audit over every log finds zero `Could not
spawn` line and zero missing-class line for the six reconstructed types. All
319 offline tests still pass. This closes source registration and loader
survival, not two-peer progression or visual/gameplay fidelity. See
[`evidence/checkpoint-076-coop-gameplay-classes.json`](evidence/checkpoint-076-coop-gameplay-classes.json).

## Earlier checkpoint: 075

**The complete original-Xbox co-op route now clears the native loader-soak
gate: 20/20 map segments each loaded and remained alive for at least 60
seconds.** One current v21 tree and one host/DLL pair ran route rows 42-61
without a premature exit, abort, error line or fatal line. Minimum observed
idle was 60.054 seconds and maximum load time was 5.074 seconds.

The accepted static input remains the 20-map v19b corpus and isolated v21 tree:
all 20 CMs are direct-authored, dependency audits are closed, and the tree has
no missing compiled companion, duplicate declaration/material, untracked file
or reparse point. All 319 offline tests pass. This is loader survival, not final
gameplay acceptance: warning-only Xbox co-op classes and remaining skeleton and
resource mismatches are now the active source-level gate before a meaningful
two-peer playthrough. See
[`evidence/checkpoint-075-coop-native-soak.json`](evidence/checkpoint-075-coop-native-soak.json).

## Earlier checkpoint: 074

**Every co-op map that exposed a native loader failure now passes on one current
audited tree.** MCU, Delta 2B part 2 and Hellhole each spawned on the minimized
direct GPL-dedicated host, idled at least ten seconds and exited with zero
error/fatal lines. Hellhole now keeps its Imp and 50-joint cinematic Cyberdemon
families private and coherent. Its missing four-part ending camera is recovered
from the Xbox DEF's exact export ranges over the same stock retail Maya take;
camera, Cyberdemon and player segments align at 104/32/120/252 frames.

The v19b corpus contains 6,122 payload files, all 20 direct-authored CMs and
zero unresolved dependency or untracked file. The isolated v21 tree has 1,015
files and no missing companion, duplicate declaration/material or reparse
point. All 319 offline tests pass. This closes the observed loader blockers,
not the route: one fresh 20-map run with at least 60 seconds idle per map is
now underway, after which warned Xbox-only spawnclasses remain a source-level
gameplay gate. See
[`evidence/checkpoint-074-coop-loader-closure.json`](evidence/checkpoint-074-coop-loader-closure.json).

## Earlier checkpoint: 073

**The two confirmed co-op crash families are now source-bound fixes with clean
focused native loads; the final observed loader blocker is patched and queued
for rebuilt validation.** MCU now rebuilds inherited animation channels after
selecting a private Xbox NPC mesh, preventing stale numeric joint indices from
walking beyond its 48-joint animation. Delta 2B part 2 now always reconstructs
its private ZCT alias from the authenticated public-source-bound 50-joint Xbox
family rather than replaying a contaminated 63-joint generated alias.

MCU and Delta 2B part 2 each spawned on the minimized direct GPL-dedicated host,
idled at least ten seconds and exited with zero error/fatal lines. Hellhole then
exposed a stock `map_hellhole.def` child declaration that inherited the private
41-joint Xbox Imp mesh while retaining the public 71-joint cyber-wakeup track.
The builder now shadows only that source and retargets `hellhole_imp` to the
coherent private animation family; all 316 offline tests pass. The v16 static
corpus has all 20 direct-authored CMs and zero unresolved dependency, and its
isolated tree has 1,000 files with no missing companion, duplicate declaration
or material, untracked file or reparse point.

This is a truthful loader-blocker checkpoint, not co-op acceptance. Hellhole
still needs its rebuilt native focus run, followed by one current 20-map sweep
with at least 60 seconds idle per map and then source-level closure of remaining
Xbox co-op spawnclass warnings. See
[`evidence/checkpoint-073-coop-loader-blockers.json`](evidence/checkpoint-073-coop-loader-blockers.json).

## Earlier checkpoint: 072

**The complete original-Xbox solo campaign now clears the native loader-soak
gate: 41/41 map segments each loaded and remained alive for at least 60
seconds with zero error/fatal lines and no premature exits.** The authoritative
v26 run uses the minimized source-built GPL dedicated host directly, never
Steam or the retail foreground executable.

The preceding v21 whole-campaign sweep was essential: although its focused
predecessors were clean, merging all map closures exposed three shared-path
collision families. CPU 1's 47-joint Campbell resources now live only under a
private runtime prefix; ordinary 50-joint Xbox ZCT resources are private while
Monorail's seated cinematic deliberately retains its coherent stock-PC mesh
and animation pair; and Hellhole uses the accepted 78-joint Cyberdemon pain
retargets ahead of raw Xbox tracks. Replay also filters the obsolete public
resources recorded by older manifests so they cannot return during rebuild.

The v26 overlay has 2,307 files totaling 816,923,492 bytes, all 41 direct
authored collision files and zero unresolved class/resource/string. Its
isolated test tree has 841 files, all 41 maps and zero missing companions,
duplicate declarations/materials, untracked files or reparse points. All 297
offline tests pass. This accepts solo loader survival, not visual, audio,
progression, transition, save/load or matched-Xbox fidelity. The 20-map co-op
60-second sweep is the next native gate. See
[`evidence/checkpoint-072-solo-native-soak.json`](evidence/checkpoint-072-solo-native-soak.json).

## Earlier checkpoint: 071

**Every failure family exposed by the first complete solo native sweep now has
a source-bound correction and a clean focused loader pass.** The original
41-map/60-second discovery run passed 29 maps and identified twelve failures.
The final candidates preserve the Xbox script behavior while adding the PC-host
`runCommand` event, qualifying the split Comm Outside lift entrypoint, and
isolating Lantern, Hazmat, Campbell/ZCT, Vagary and other map-local skeleton
families instead of mixing Xbox animations with incompatible stock-PC meshes.

The v17 overlay contains 2,095 payloads totaling 802,031,692 bytes, selects
direct authored collision for all 41 maps and has zero unresolved class,
resource or string. Its v21 isolated runtime tree has 839 files and zero
missing companion, duplicate declaration/material, untracked file or reparse
point. All twelve maps that failed the discovery sweep subsequently spawned,
idled at least five seconds and exited with zero error/fatal lines on the
minimized direct GPL-dedicated host. All 294 offline tests pass.

This closes the known solo loader blockers, not the authoritative soak or
gameplay boundary. A fresh v21 pass of all 41 maps with a full 60-second idle
per map is still required, followed by the 20-map co-op soak and later visual,
audio, progression and two-peer acceptance. See
[`evidence/checkpoint-071-solo-loader-blocker-closure.json`](evidence/checkpoint-071-solo-loader-blocker-closure.json).

## Earlier checkpoint: 070

**The first two failures found by the replacement solo sweep are now fixed as
source-bound compatibility families and pass focused native loading.** Mars
City 2 part 2 embeds an Xbox-only `map_marscity1` block in addition to its own
principal namespace. The builder now preserves that block under
`xbox_solo_mars_city2_2_marscity1` and retargets its two GUI callbacks, avoiding
stock `doom_main` redeclarations without deleting Xbox behavior.

Admin proved that the pipe and railing cinematics cannot be repaired by
copying isolated animations onto the 72-joint PC Pinky. Five solo maps now
package the complete authenticated 22-file, 45-joint Xbox Pinky family; Admin
also packages its matching 45-joint `pinkyrailing` cinematic. The rebuilt
41-map overlay has 2,050 payloads, direct authored collision everywhere and
zero unresolved class/resource/string. Its isolated 811-file test tree has no
missing companion, duplicate declaration, untracked file or reparse point.
Focused GPL-dedicated smokes of `mars_city2_2` and `admin` both spawned, idled
five seconds and exited with zero errors/fatals. All 285 offline tests pass.
The authoritative 41-map, 60-second sweep remains required, so this is loader
progress rather than gameplay or fidelity acceptance. See
[`evidence/checkpoint-070-solo-namespace-pinky.json`](evidence/checkpoint-070-solo-namespace-pinky.json).

## Earlier checkpoint: 069

**The first native solo sweep has been turned into source-bound fixes for every
failure family observed so far, and a replacement 41-map candidate closes those
dependencies without weakening the corpus boundary.** The fixes retain
Xbox-only principal scripts, preserve coherent animation skeleton families,
reuse the co-op reconstruction's audited 50-to-63-joint commando retarget, and
scope recovered assets only to maps that instantiate them.

The replacement overlay corpus contains 1,887 files and all 41 direct-authored
collision files, with zero unresolved class, resource or string dependency. Its
isolated runtime tree contains 741 files with zero missing compiled companion,
duplicate declaration/material, untracked file or reparse point. All 283 offline
tests pass. The discovery sweep is still running; the replacement has not yet
completed a clean 41-map native pass, so no all-map or fidelity claim is made.
See
[`evidence/checkpoint-069-solo-native-resource-families.json`](evidence/checkpoint-069-solo-native-resource-families.json).

## Earlier checkpoint: 068

**The campaign now has a source-built GPL dedicated diagnostic host and
corpus-isolated native-test trees.** A first hidden load of Xbox
`vv/mars_city1_1` spawned 1,054 entities, idled 60.067 seconds and produced no
ERROR or fatal line without launching through Steam or taking foreground focus.

Native loading then exposed two real packaging defects. The unified merge had
removed Xbox-only principal script includes along with scripts already compiled
by stock PC `doom_main`; the corrected rule removes only the exact stock include
set. Admin also proved that one absent `glassbreak_idle.md5anim` member causes
Doom to reject the complete Pinky modelDef, hiding the valid shipped
`glassbreak` cinematic. The compatibility transform removes only that unshipped
idle member. A fresh 41-map solo tree independently audits 714 files with zero
missing companions or duplicate declarations; the separate 20-map co-op tree
audits 973 files. All 281 offline tests pass. The complete native sweeps remain
in progress and no all-map or gameplay-fidelity claim is made. See
[`evidence/checkpoint-068-headless-native-host.json`](evidence/checkpoint-068-headless-native-host.json).

## Earlier checkpoint: 067

**The 61-map native soak now has a fail-closed, resumable runner, and the first
attempt has been correctly separated from map evidence.** Thirty-one direct
retail-executable invocations exited with Steam-wrapper code 4 before creating
a log or reaching a spawn marker. A Steam launch also produced no Doom process
while another Steam game was active. No campaign map received a native verdict.

The replacement runner detects an active Steam game before launch, uses Steam
for the retail executable, records executable/game-DLL/plan/log hashes, requires a real
spawn marker plus the full 60-second idle, supports bounded/resumed batches and
aborts immediately on launcher/bootstrap failure. Its non-game smoke test proves
that one bootstrap failure attempts no later map. The accepted 61-map tree
still rehashes to `7e524166...fe60979`, and all 274 offline tests pass. Native
map loading remains pending until Steam is free; no user process was terminated.
See [`docs/NATIVE_TEST_PLAN.md`](docs/NATIVE_TEST_PLAN.md) and
[`evidence/checkpoint-067-native-soak-runner.json`](evidence/checkpoint-067-native-soak-runner.json).

## Earlier checkpoint: 066

**The accepted 61-map tree now has a fail-closed native test itinerary and a
noncontaminating local `fs_game` handoff.** The solo transition graph is one
41-map route from `mars_city1_1` to a linked `endOfGame` in `hellhole_2`; the
co-op graph is one 20-map route from `xc_mars_city1_1` to a linked `endOfGame`
in `xc_hellhole_1`. Two apparent co-op exits to solo paths have zero incoming
links and remain preserved dormant residue rather than test-route edges.

Local `xbox_campaign_test_v2` points to the immutable accepted tree, while a
separate `fs_savepath` receives DoomConfig/log state. Rehashing after staging
still yields ledger `7e524166...fe60979`. All 274 offline tests pass; no Doom
process was launched. Offline work is now at the native loader boundary. See
[`docs/NATIVE_TEST_PLAN.md`](docs/NATIVE_TEST_PLAN.md) and receipt
[`evidence/checkpoint-066-native-test-handoff.json`](evidence/checkpoint-066-native-test-handoff.json).

## Earlier checkpoint: 065

**All 61 recovered campaign segments now coexist in one deduplicated local test
tree.** A cross-package audit found 1,572 unique virtual paths and proved all
115 solo/co-op shared paths byte-identical. Only three per-map paths varied:
the solo/co-op language closures and the co-op runtime DEF. Their 101 strings,
47 strings and 25 declarations union without semantic conflict.

The first independent tree audit caught five declarations duplicated between
the co-op supplemental DEF and complete DEF files pulled in by other maps. The
accepted v2 builder removes those five only after normalized bodies match, and
fails closed on any difference. Its 1,572 files (1,009,071,410 bytes) include
61 MAP/PROC/CM triplets, 1,500 unique runtime declarations and 249 unique
materials, with no untracked file or reparse point. All 272 offline tests pass;
Doom 3 and `dmap` were not launched. Receipt:
[`evidence/checkpoint-065-unified-campaign-test-tree.json`](evidence/checkpoint-065-unified-campaign-test-tree.json).

## Earlier checkpoint: 064

**The 20-map Xbox co-op campaign now has an exact manifest-only portable test
package.** The packager selects the named final `soundguard_v3` generation
instead of relying on mutable-directory timestamps, verifies every source and
copied payload, copies each manifest byte-for-byte, and publishes only after
the full staged corpus closes.

The package contains 6,080 payloads totaling 545,522,554 bytes, with zero
untracked files and zero reparse points. Its independent audit reproduces the
accepted payload ledger `e90511d6...7504cad` and manifest ledger
`0b412c1f...d777528` exactly. All 259 offline tests pass; Doom 3 and `dmap` were
not launched. The package remains local retail-derived test data and is not
committed or redistributable. Receipt:
[`evidence/checkpoint-064-coop-portable-package.json`](evidence/checkpoint-064-coop-portable-package.json).

## Earlier checkpoint: 063

**The complete 41-map Xbox single-player test corpus is now materialized as a
portable ordinary-file package.** The accepted final audit view contains 39
NTFS junctions, which are useful for deduplicated development but unsafe as a
release/test handoff. The new fail-closed packager copies only the 1,792
manifest-listed payloads, verifies every source and destination byte/hash, and
copies each signed manifest into a new tree without junctions or symlinks.

The 782,089,007-byte package has zero reparse points and re-audits to the exact
accepted file ledger `629cc7d...43eecf0c` and manifest ledger
`ee6959f0...0997178`. Untracked development files cannot enter it. All 256
offline tests pass; Doom 3 and `dmap` were not launched. The local package is
retail-derived test data and is not committed or redistributable. Receipt:
[`evidence/checkpoint-063-solo-portable-package.json`](evidence/checkpoint-063-solo-portable-package.json).

## Earlier checkpoint: 062

**All 61 recovered campaign segments now have a fail-closed final-audit coverage
matrix.** It cross-checks each final report's map set rather than trusting
aggregate counts: 41 solo maps pass 12 applicable gates each, and 20 co-op maps
pass ten each. The result is 692 green per-map cells backed by 24 hashed reports
and the complete 60-file solo/30-file co-op AAS corpora, with no missing row or
failure record.

Green means static coverage only. Existing source-residue/attention records
remain explicit, and native loading, collision traces, visibility, timing,
networking, save/load and visual parity remain outside this claim. All 253
offline tests pass; Doom 3 and `dmap` were not launched. Receipt:
[`evidence/checkpoint-062-campaign-static-matrix.json`](evidence/checkpoint-062-campaign-static-matrix.json).

## Earlier checkpoint: 061

**The 41-map Xbox single-player corpus now has source-bound player-start and
teleport topology.** Every segment contains exactly one `info_player_start`,
and every player entity is identical to the decoded MAP selected by its overlay
manifest hash. The corpus retains 42 teleport destinations: 38 are MAP-linked,
one is directly script-referenced, and three are unreferenced in both static
paths. Monorail 2 also retains one authenticated `info_player_deathmatch`.

The three unreferenced teleports and deathmatch entity are Xbox-authored
residue, not conversion loss. They remain in place pending native observation;
deleting or wiring them would be speculative. All 250 offline tests pass, with
zero player-topology regression. Doom 3 and `dmap` were not launched. Receipt:
[`evidence/checkpoint-061-solo-spawn-topology.json`](evidence/checkpoint-061-solo-spawn-topology.json).

## Earlier checkpoint: 060

**Every co-op segment now has source-bound paired spawn topology.** Across the
20 final maps, all 50 player-one starts have a player-two counterpart at the
same level, all levels are contiguous from one, every map retains exactly one
stock start, and all 22 spawn-level advancement targets have at least one MAP
link (31 links total). The complete 141-entity spawn/advance subset is exact to
each manifest-bound decoded Xbox source.

Three maps authentically omit a safe-spawn entity, and six paired placements
use different facing angles. Those are explicit native-test observations, not
conversion loss; the port does not invent safe points or rotate authored
starts. All 249 offline tests pass, with zero spawn-topology regression. Doom 3
and `dmap` were not launched. Receipt:
[`evidence/checkpoint-060-coop-spawn-topology.json`](evidence/checkpoint-060-coop-spawn-topology.json).

## Earlier checkpoint: 059

**The apparent shared resurrection path is now classified across all 20 co-op
maps without inventing missing gameplay.** The bytecode decoder now covers
`OP_THREAD` as well as `OP_CALL`: 51 thread statements exist, but none directly
enters `Coop::initCoop`, `Coop::resurrect_player`, `player1Death` or
`player2Death`. Active recovered source likewise contains no player-death call
expression, no map has a reachable resurrection initializer, and the retail XBE
contains none of the six exact helper/state names searched.

Only the two Hell splits retain resurrection callbacks. Hell 1-1's relay has no
incoming MAP link or script reference. Hell 1-2's relay is reachable only from
a hidden GUI; its pad is also hidden, no reveal path exists, and neither map
contains a `resurrect_point_0`. These records are present in the hash-bound Xbox
sources, so the port preserves them as dormant retail residue instead of
synthesizing a destination or silently enabling a broken path. All 246 offline
tests pass; Doom 3 and `dmap` were not launched. Receipt:
[`evidence/checkpoint-059-coop-resurrection-topology.json`](evidence/checkpoint-059-coop-resurrection-topology.json).

## Earlier checkpoint: 058

**The 20-map co-op corpus now has complete active script-sound closure.** The
new co-op audit found only `mset3_movement` and `mset3_stop`, one call each in
`xc_mcu.script`. As in the solo split, the authenticated Xbox sound metadata
ships no third machinery set and the stock-PC third howitzer uses `mset2`.
The fail-closed builder now corrects those exact two literals and records the
input/output hashes in the MCU manifest.

Repeated rebuilds also exposed four disabled `setupCoop` epairs whose comment
prefix was not byte-idempotent. The builder now collapses only those exact,
already-disabled lines to one stable guard. The final soundguard-v3 corpus was
rebuilt directly from the accepted scriptguard-v2 inputs so its manifests
record both corrections. It closes 6,080 payloads, 4,654 links, 63 callbacks,
21 transitions, 639 AI requirements, 30 AAS files and 226 active script sound
calls with zero port regression. All 243 offline tests pass; Doom 3 and `dmap`
were not launched. Receipt:
[`evidence/checkpoint-058-coop-script-sound-closure.json`](evidence/checkpoint-058-coop-script-sound-closure.json).

## Earlier checkpoint: 057

**All script-named sound shaders in the 41-map solo overlay corpus now resolve
against a shipped declaration.** A new active-source audit found four
map/event records, representing six calls and only two shader names:
`mset3_movement` and `mset3_stop` in the MCU split scripts. The authenticated
Xbox `global.xsndshd` ships only the first two machinery sets, and the stock-PC
MC Underground script assigns its identical third howitzer to `mset2`.

The builder now makes that exact, fail-closed `mset3` to `mset2` correction in
`map_mcu_1.script` and `map_mcu_2.script`, with input/output hashes and counts
in each manifest. No audio asset or declaration was invented. The rebuilt
strict-v11 audit view contains 1,792 payloads, closes 746 active script sound
references, all 409 callbacks, 14,700 entity links, 2,739 direct WAV pairs,
1,479 AI requirements and all 60 AAS files with zero unresolved port record.
All 241 offline tests pass. Doom 3 and `dmap` were not launched. Receipt:
[`evidence/checkpoint-057-solo-script-sound-closure.json`](evidence/checkpoint-057-solo-script-sound-closure.json).

## Earlier checkpoint: 056

**All 60 functional co-op MAP callback records are now accounted for across
the two Xbox script-loading paths.** A co-op `script.bin` is the compiled image
of its sibling `*_main.script` compilation unit and its explicit includes; it
is not necessarily a complete compiled map script. Six callback records are
present in those startup programs. The other 54 are in the already audited
map-load source that worldspawn compiles for the loaded map. Three exact retail
warning/no-op records remain excluded.

All 20 compilation-unit sources were matched to their binaries. Across
4,591,834 bytes, 217,103 statements, 5,239 function records and 589 compiled
calls, there are zero bad statement bases, duplicate callback definitions,
missing compilation units or contradictory resolutions. This closes the
apparent gap without inventing bytecode or falsely rejecting valid map-load
functions. All 238 offline tests pass; Doom 3 and `dmap` were not launched.
Receipt:
[`evidence/checkpoint-056-coop-callback-bytecode-boundary.json`](evidence/checkpoint-056-coop-callback-bytecode-boundary.json).

## Earlier checkpoint: 055

**All 20 co-op map scripts now have source-bound entity lookup and entrypoint
reachability audits, and one concrete PC-host progression hazard is fixed.** In
`xc_mars_city2_1`, `connect_sarge_speaker` called two speaker entities absent
from the split Xbox MAP before triggering `trigger_relay_111`. A required null
entity argument terminates the PC script thread, so the overlay now guards only
those two missing audio calls and preserves the wait, monitor actions and later
progression relay.

The rebuilt corpus still closes all 6,080 payloads, 4,654 named links, 63 MAP
callbacks, 21 transitions, 639 AI requirements and 30 navigation files with
zero port regression. Reachability covers 216 functions, 99 of them reachable,
and classifies all remaining script-entity residue. The 65 attention records
are source-authored: 63 belong to EnPro 2 machinery deliberately disabled with
`vv_` names, and two are shared Hell resurrection-point lookups whose external
C++ entry path remains unproven. All 236 offline tests pass; Doom 3 and `dmap`
were not launched. Receipt:
[`evidence/checkpoint-055-coop-script-reachability.json`](evidence/checkpoint-055-coop-script-reachability.json).

## Earlier checkpoint: 054

**The compiled-script audit now covers every one of the 41 original-Xbox solo
maps, and every functional MAP callback has a shipped bytecode definition.**
The solo corpus contains 487,257 statements, 11,940 function records and 1,654
compiled calls. All 41 binaries independently resolve to the same 4,100 base
statement index.

The prior source-level semantic gate contains 403 namespaced callback records
and two object-method records. All 405 resolve in the corresponding compiled
program; the object witnesses are `char_sentry::flashlight_on` and
`char_sentry::flashlight_off`. The four documented retail-PC warning/no-op
records remain deliberately excluded rather than being given invented code.
The co-op bytecode audit was rerun unchanged and remains clean. All 235 offline
tests pass; Doom 3 and `dmap` were not launched. Receipt:
[`evidence/checkpoint-054-solo-script-bytecode.json`](evidence/checkpoint-054-solo-script-bytecode.json).

## Earlier checkpoint: 053

**All 20 original-Xbox co-op `script.bin` files now have a structural
function/call audit, resolving the apparent `Coop::initCoop` contradiction.**
The format carries length-prefixed source metadata, a global-data image,
serialized function records and a tail array of 8-byte statements. Every map
uses the same recovered statement-index base of 4,100. The official GPL opcode
enum identifies `OP_CALL` as 96; known `initCoop -> showResurrectors` and
`resurrect_player -> getNearestLocation` calls validate the decoded operands in
all 16 binaries that include `coop.script`.

The corpus contains 217,103 statements and 589 compiled calls. It contains no
compiled `setupCoop` function and no compiled call to `Coop::initCoop` in any
map. The earlier string hits were function definitions supplied by the shared
include, not call sites. This supports the narrow checkpoint-052 treatment of
stale MAP callbacks without inventing the block-commented functions. All 233
offline tests pass; Doom 3 and `dmap` were not launched. Receipt:
[`evidence/checkpoint-053-xbox-script-bytecode.json`](evidence/checkpoint-053-xbox-script-bytecode.json).

## Earlier checkpoint: 052

**All 20 co-op maps now rebuild through one source-bound toolchain with closed
script-callback, transition, entity-link, direct-audio and navigation gates.**
The final overlays contain 6,080 uniquely receipted payloads and zero unresolved
classname, resource or string. The callback audit resolves 51 global and nine
namespaced calls; the remaining three are byte-matched retail-PC admin no-ops.
The 20-map chain is closed from `xc_mars_city1_1` through `xc_hellhole_1`, whose
external destination is the stock solo finale `vv/hellhole_2`.

The rebuild restored 22 exact PCM files from the authenticated Xbox XACT banks,
including three co-op-only radio lines. Only `sound/evolvers/airhymn_03.wav`,
which is absent from all recovered Xbox and PC inventories, is made inert. All
20 map scripts explicitly include the recovered shared `script/coop.script`.
Site 3's case-insensitive duplicate entity name was a real PC load blocker:
the referenced co-op exit keeps its retail name while the unreferenced solo
residue receives a path-scoped name. Entity closure now has zero duplicates and
zero port-introduced unresolved links. All 231 offline tests pass; Doom 3 and
`dmap` were not launched. Receipt:
[`evidence/checkpoint-052-coop-semantics-audio.json`](evidence/checkpoint-052-coop-semantics-audio.json).

## Earlier checkpoint: 051

**No named entity link or binding from the decoded Xbox co-op sources is lost
in the latest 20 overlays.** A source-hash-bound audit covers 15,703 entities
and 4,654 link spawnargs. It resolves 3,985 to local named entities, recognizes
two engine/empty values, and proves all 667 remaining dangling links are
already present in the exact decoded source MAP. There are zero port-introduced
unresolved links.

Site 3 contains one source-authored case-fold collision:
`target_endlevel_1`/`target_endLevel_1`. Checkpoint 052 proves this is fatal on
the PC host and applies the narrow, receipted correction. All 225 offline tests
passed at this checkpoint. Doom 3 and `dmap` were not launched. Receipt:
[`evidence/checkpoint-051-coop-entity-links.json`](evidence/checkpoint-051-coop-entity-links.json).

## Earlier checkpoint: 050

**The latest 20 co-op overlays now have a complete one-path/one-receipt corpus
audit.** All 6,046 manifest payloads (535,777,192 bytes) were rehashed from
disk, every manifest path is unique, all 20 maps retain direct authored
collision, and classname/resource/string closure is empty.

This caught a manifest-only duplication in the two checkpoint-049 rebuilds:
18 direct WAVs already supplied by runtime profiles were recorded again by the
direct-audio pass. The builder now treats an existing staged WAV as satisfied;
the clean rebuilds are payload-identical and only their manifests changed. The
navigation requirement and 30-file structural audits remain clean. One local,
untracked nested TGA is explicitly excluded from the manifest/package and was
not deleted because its ownership is unknown. All 223 offline tests pass. Doom
3 and `dmap` were not launched. Receipt:
[`evidence/checkpoint-050-coop-overlay-corpus.json`](evidence/checkpoint-050-coop-overlay-corpus.json).

## Earlier checkpoint: 049

**Every effective co-op AI navigation requirement is now packaged in the
latest 20-map overlay set.** The same inheritance-aware audit used for solo
covers 639 direct MAP, entityDef-valued and literal-script AI requirements:
638 have their requested AAS class, one deliberately disables AAS, and none
are missing.

The audit exposed three shared-archive files omitted by the earlier co-op
builds: Guardian and Mancubus navigation for `xc_hell1_2`, and Cyberdemon
navigation for `xc_hellhole_1`. Rebuilt overlays preserve every prior payload
byte-for-byte and add only those files. Across the latest overlays, all 30 AAS
files parse with complete nonzero BSP/area coverage: 20 AAS48, six AAS96, two
Mancubus, one Guardian and one Cyberdemon. All 220 offline tests pass. Doom 3
and `dmap` were not launched. Receipt:
[`evidence/checkpoint-049-coop-aas-requirements.json`](evidence/checkpoint-049-coop-aas-requirements.json).

## Earlier checkpoint: 048

**Every solo AI navigation class required by the final entityDefs is now
present and structurally valid.** An inheritance-aware audit covers 1,479
direct MAP AI instances plus literal script and entityDef references. It finds
1,471 requirements backed by the exact packaged AAS class, eight deliberate
empty `use_aas` values, and zero missing requirements.

This exposed five authored files omitted by the former AAS48/AAS96-only core
selection. The files were recovered from the source-bound shared Xbox archive,
decoded with the established plane-distance correction, and added to strict
v10: Sabaoth in CPU 2, Mancubus in Hell 1 part 2 and Recycling 2 part 2,
Guardian in Hell 1 part 3, and Cyberdemon in Hellhole 1. The final corpus has
60 structurally valid files, 47,352 areas and 230,620 reachabilities. All other
payloads are byte-identical to strict v9, all offline gates remain closed, and
218 tests pass. Doom 3 and `dmap` were not launched. Receipt:
[`evidence/checkpoint-048-solo-aas-requirements.json`](evidence/checkpoint-048-solo-aas-requirements.json).

## Earlier checkpoint: 047

**The complete solo navigation corpus now passes the standard-PC structural
and coverage audit.** Strict v9 contains every shipped navigation class: 41
AAS48 files and 14 AAS96 files. All 55 parse with valid paired planes and
complete nonzero BSP/area coverage, totaling 44,109,766 bytes, 45,857 areas,
226,989 reachabilities and 158,002 nodes. No file has an unreachable nonzero
node or an unreferenced nonzero area.

This closes the corpus-wide decoded-AAS structure gate; actor bounds, dynamic
obstacles and encounter routes still require native progression. All 215
offline tests remain green. Doom 3 and `dmap` were not launched, and
`gamex86.dll` remains unchanged. Receipt:
[`evidence/checkpoint-047-solo-aas-corpus.json`](evidence/checkpoint-047-solo-aas-corpus.json).

## Earlier checkpoint: 046

**Every gameplay command emitted by every in-world GUI instance is now
accounted for across all 41 solo overlays.** The audit binds 1,700 MAP GUI
instances to their overlay or installed-package GUI source and checks 1,107
relevant commands. All 128 localized/dynamic script callbacks resolve, all 63
explicit entity operations resolve locally, and 893 implicit activations feed
the owning entity's already-audited target graph. Twenty unset dynamic script
parameters emit no function token and are explicit no-ops.

Three explicit GUI activations name entities already absent from their decoded
Xbox split-map sources: `com_walk1` in CPU and `trigger_cranemaint` in both MCU
segments. They remain visible native-attention records. There are zero missing
GUIs, unresolved language IDs, functions, or port-lost entity targets. All 215
offline tests pass. Doom 3 and `dmap` were not launched, and `gamex86.dll`
remains unchanged. Receipt:
[`evidence/checkpoint-046-solo-gui-commands.json`](evidence/checkpoint-046-solo-gui-commands.json).

## Earlier checkpoint: 045

**Every manifest-selected animation frame command is now accounted for across
all 41 solo overlays.** The engine-scoped audit covers 539 commands: 330 global
script calls, one namespaced call, 172 object-method calls and 36 entity
triggers. All callable symbols that the port is expected to supply resolve,
and every source-present trigger entity survives the conversion.

Twelve triggers were already absent from their decoded Xbox split-map source
and remain explicit native-attention records. One selected retail Vagary
animation names `sonic_attack`, a method absent from both the stock PC and
decoded Xbox Vagary scripts; the retail declaration is preserved rather than
inventing boss behavior. There are zero port-introduced unresolved records and
all 213 offline tests pass. Doom 3 and `dmap` were not launched, and
`gamex86.dll` remains unchanged. Receipt:
[`evidence/checkpoint-045-solo-frame-commands.json`](evidence/checkpoint-045-solo-frame-commands.json).

## Earlier checkpoint: 044

**Reachable computed entity names and the last apparent nonterminal script-
exit cases are now resolved offline across all 41 solo maps.** Function-scoped
argument domains prove all 39 reachable Comm Outside airlock names local. The
MCU scripts set `NUM_BRIDGES = 4`, so their pair functions return before the
profiled 5/7 cases; the 16 reachable 1/3 names are local. These 55 lookups are
now proven rather than left in a conservative superset.

Monorail 2's `main2` selects train state 3, whose branch returns before four
first-half direct references. The only MAP callback is a disabled, bound,
unreferenced trigger, so those records have exact control-flow witnesses. The
remaining 275 reachable source-residue records are VM-safe receiver/nullable
uses except one Comm 1 callback whose absent required argument is its final
statement after the door-bang actions. There are zero unresolved records and
zero potential nonterminal thread exits. All 211 offline tests pass. Doom 3
and `dmap` were not launched, and `gamex86.dll` remains unchanged. Receipt:
[`evidence/checkpoint-044-solo-reachable-script-domains.json`](evidence/checkpoint-044-solo-reachable-script-domains.json).

## Earlier checkpoint: 043

**The solo PC bridges now preserve the retail worldspawn startup contract
without running map initialization twice.** Official GPL `idWorldspawn::Spawn`
first schedules a global `main`, then independently schedules every worldspawn
`call*` function. Forty Xbox solo maps already carry the exact namespaced
initializer in their worldspawn. Their strict-v8 bridges duplicated that call;
strict v9 includes the recovered sources but deliberately emits no global
dispatcher. `delta4` is the sole map without a worldspawn call and keeps a
generated global fallback to `map_alphalabs4::main()`.

All 1,746 non-bridge, non-manifest payloads are byte-identical to v8. Strict v9
retains 1,787 payload records, direct authored collision on all 41 maps, the
closed 41-stage transition chain, complete direct-audio coverage, and zero
unresolved structural, resource, string, callback, entity-link or script-
entity record. Removing the 40 duplicate wrapper functions leaves 1,025 script
functions, 524 call edges and 652 reachable functions; the same 334 reachable
source-authored residue uses remain explicit attention items. All 209 offline
tests pass. Doom 3 and `dmap` were not launched, and `gamex86.dll` remains
unchanged. Receipt:
[`evidence/checkpoint-043-solo-worldspawn-dispatch.json`](evidence/checkpoint-043-solo-worldspawn-dispatch.json).

## Earlier checkpoint: 042

**The two Xbox solo second-segment scripts now enter their exact retail
initializers, and the complete 41-map corpus has been rebuilt and re-audited.**
The PC bridge for `alphalabs1_2` now calls
`map_alphalabs1::main2()` and the bridge for `monorail_2` calls
`map_monorail::main2()`. Both functions are present in the recovered retail
scripts. The former bridge generator called `main()` for every segment, which
silently initialized the first half of these two split stages.

Only those two generated bridge scripts and their two manifests changed from
strict v7; the other 1,824 files are byte-identical. Strict v8 contains 1,787
payload records totaling 780,869,120 bytes, selects direct authored collision
for all 41 maps, and has zero unresolved structural, resource, string,
transition, callback, direct-audio, entity-link or script-entity record. A
reachability pass starts from each corrected bridge and all MAP callbacks: 691
of 1,065 functions are reachable, 374 are unreachable, and 334 reachable
source-authored residue references remain explicit attention items rather than
being mislabeled as conversion defects. All 208 offline tests pass. Doom 3 and
`dmap` were not launched, and the installed `gamex86.dll` is unchanged.
Receipt:
[`evidence/checkpoint-042-solo-script-entrypoints.json`](evidence/checkpoint-042-solo-script-entrypoints.json).

## Earlier checkpoint: 041

**Direct `$entityName` script references are now closed against conversion
loss across all 41 solo maps.** The parser ignores comments and string literals
and audits 8,492 active references representing 2,627 unique map/name pairs.
7,167 point to map entities and 325 to engine-created entities such as the
world and player.

The remaining 1,000 references are absent from both the decoded source map and
the PC overlay, predominantly because the recovered retail scripts are shared
across Xbox split segments. None names an entity present in source but lost in
the port. They remain reachability work, not assumed no-ops. Combined with the
225 `sys.getEntity` sites, the script entity report has zero port-introduced
unresolved records. All 202 offline tests pass; Doom 3 remains closed. Receipt:
[`evidence/checkpoint-041-solo-direct-script-entities.json`](evidence/checkpoint-041-solo-direct-script-entities.json).

## Earlier checkpoint: 040

**Every solo-script `sys.getEntity` call now has a static accounting.** The 41
overlays contain 225 calls: 44 literal lookups and 181 computed expressions.
The computed expressions have explicit conservative domains derived from loop
bounds, function arguments, crane slots, bridge pairs, airlock combinations,
lift paths and monorail grids. No expression is left unprofiled.

The profiles expand to 1,532 call/name references across 871 unique map/name
pairs. Every name that existed in the decoded source still exists in the PC
overlay: there are zero port regressions. Twenty-two literal calls and 408
unique profiled names are absent from both source and overlay, chiefly shared
scripts spanning Xbox split segments; they remain reported as source-authored
residue pending reachability analysis, not declared harmless. All 201 offline
tests pass, and Doom 3 remains closed. Receipt:
[`evidence/checkpoint-040-solo-script-entities.json`](evidence/checkpoint-040-solo-script-entities.json).

## Earlier checkpoint: 039

**The solo entity-link gate now covers every static entity-reference spawnarg
identified in the stock PC game source.** Beyond `target*`, bind and camera
targets, this includes elevator doors/status GUIs, binary-mover buddies and
open/close/block triggers, objective cameras, teleporter views, attachments,
spring endpoints, synchronized locks and ownership.

The expanded 41-map audit covers 14,700 links. 13,084 resolve to local named
entities, 16 are engine/empty sentinels and 1,600 are fingerprinted unchanged
in the decoded Xbox source. There are still zero case-insensitive duplicate
names and zero port-introduced unresolved links. The 95 newly covered values
comprise 84 local resolutions and eleven source-authored split-map remnants.
All 196 offline tests pass, and Doom 3 remains closed. Receipt:
[`evidence/checkpoint-039-solo-runtime-links.json`](evidence/checkpoint-039-solo-runtime-links.json).

## Earlier checkpoint: 038

**All 41 retail Xbox single-player overlays now also close the PC entity-name
and explicit entity-link gates.** The audit parses 38,769 entities and 14,605
`target*`, bind and related links. It reports zero case-insensitive duplicate
names and zero port-introduced unresolved links.

Official PC source uses `idStr::Icmp` for `FindEntity` and rejects a second
case-insensitive name during `AddEntityToHash`. That exposed three Xbox name
pairs unsafe on PC. Two unreferenced Alpha Labs 2 vacuum markers now have exact,
origin-witnessed suffixes. Delta 2A keeps both independent exits while its
second exit and matching trigger target receive one distinct name. These edits
are path-scoped, fail-closed and manifest-recorded.

The audit separately fingerprints 1,589 dangling links as byte-authored in the
decoded retail split-map sources. They are preserved and reported rather than
guessed at or counted as port regressions. All checkpoint-037 structural,
semantic, transition and audio gates remain closed. The rebuilt corpus has
1,787 payload records totaling 780,869,118 bytes, and the complete offline
suite is 195 tests. Doom 3 and `dmap` were not launched, and root `gamex86.dll`
remains unchanged. Receipt:
[`evidence/checkpoint-038-solo-entity-links.json`](evidence/checkpoint-038-solo-entity-links.json).

## Earlier checkpoint: 023

**The tenth co-op segment, `xc_delta2b_1`, now has direct authored collision,
corrected AAS48, complete archive-local model recovery and a portable PC overlay
candidate.**

The decoded 912-entity MAP binds to geometry CRC `4216080146`. Direct CM.X
exports 238 models; independent PC `dmap` contains all 238 plus 57 models,
every one explained by `noclipmodel 1`. Corrected AAS48 has 698 areas, 3,361
reachabilities, 2,532 nodes and complete nonzero BSP/area coverage. All 437
selected model files decode.

The one Xbox-only ZCT animation cannot be copied directly onto the stock
63-joint PC mesh: its source skeleton has 50 joints. A deterministic retarget
preserves every shared joint's world-space motion, restores 13 PC-only bind
joints, and produces a 63-joint `head_butt.md5anim`. The last loader-confirmed
overlay spawns 912/0 and joins player 0 with no missing resource, invalid-joint,
AF/IK, error or fatal line.

Two location warnings in that run are now explained by one stale retail entity
origin. Xbox geometry moved the applicable portal from `y=-608` to `y=-557`,
51 units away, while the engine searches only a 16-unit box. The exact
fail-closed transform moves only `info_locationseparator_19` to the decoded and
independently dmap-confirmed Xbox portal. The resulting portable 278-file
candidate has zero unresolved names and all 160 tests pass. It has deliberately
not been launched while another Steam game is active; one bounded validation,
progression, transition, two-peer and Xbox-reference acceptance remain open.
Full receipts are in
[`evidence/checkpoint-023.json`](evidence/checkpoint-023.json).

## In progress: checkpoint 024 offline preflight

`xc_delta2b_2` is structurally decoded without launching Doom 3. Its 843-entity
MAP has geometry CRC `3474151774`; direct CM.X exports 229 models; corrected
AAS48 has 849 areas, 3,558 reachabilities and complete nonzero BSP/area
coverage. The decoded PROC contains 91 areas and 101 portals. All 343 selected
model files decode.

Three commando entities select the same Xbox-only 50-joint `head_butt`
animation found in checkpoint 023. Its raw payload is byte-identical, so the
same hash-bound 63-joint PC retarget is reused. Four direct MAP samples absent
from stock PC packages recover through the segment INDEXLIST/XSB and original
global XWB. Two stale `inner1.wav` epairs are corrected to the `inner_1.wav`
name carried by both Xbox XSND and stock PC. The 276-file offline candidate
preserves the retail map script and its single MAP callback, covers all 67
direct sample paths, and has zero unresolved names. All 161 tests pass.
Retail flags predict 843/0 entities on default medium; the preserved co-op exit
GUI targets `vv/xbox_coop/xc_delta4` through one `target_endlevel`.

This is an in-progress receipt, not loader acceptance. Independent PC `dmap`,
bounded native loading, XACT sound selection, progression and two-peer work are
deferred until testing will not interrupt another Steam session. Evidence is in
[`evidence/checkpoint-024-offline.json`](evidence/checkpoint-024-offline.json).

## Checkpoint 025: Delta 4 offline preflight

The retail transition from `xc_delta2b_2` has been followed into `xc_delta4`.
Its 394-entity MAP, 17-area/15-portal PROC and direct 92-model CM decode. Both
AAS48 and AAS96 have complete nonzero BSP/area coverage, and all 283 selected
model files decode. The three MAP callbacks have definitions in the preserved
script closure. Of 35 direct MAP sample paths, 34 are present in stock PC data;
the remaining `sound/foley2/pipes/airgen_04.wav` is recovered through the
source-bound Delta 4 INDEXLIST/XSB/global-XWB chain. The 273-file portable
overlay has zero unresolved class, resource or string names. Retail flags
predict 394/0 entities on default medium and the exit targets
`vv/xbox_coop/xc_hell1_1`.

No Doom 3 executable or `dmap` was run for this checkpoint. Independent PC
collision generation, native loader acceptance, progression and two-peer
behavior remain deliberately deferred until the campaign-wide offline pass is
complete. Receipt:
[`evidence/checkpoint-025-offline.json`](evidence/checkpoint-025-offline.json).

## Checkpoint 026: Hell 1 part 1 offline preflight

`xc_hell1_1` now has source-bound MAP, PROC, AAS48, AAS96 and direct CM
exports, plus all 308 selected model members decoded. Both navigation graphs
have complete nonzero BSP/area coverage. All 50 direct MAP sample paths are
closed: 35 through stock PC data and 15 through the segment's own
INDEXLIST/XSB/original-XWB routing. The 286-file portable overlay reports zero
unresolved names and preserves all 11 callback references plus the transition
to `vv/xbox_coop/xc_hell1_2`. Retail flags predict 866/0 entities on default
medium. No executable or `dmap` was run. Receipt:
[`evidence/checkpoint-026-offline.json`](evidence/checkpoint-026-offline.json).

## Checkpoint 027: Hell 1 part 2 offline preflight

`xc_hell1_2` now has a complete offline structural and dependency pass. Its
735-entity MAP, PROC, AAS48 and 101-model direct CM export are source-bound;
the navigation BSP covers every nonzero node and area, and all 301 selected
model files decode. All 40 direct MAP samples are covered after 15 source-bound
XACT recoveries. The 285-file portable overlay has zero unresolved names,
preserves all three unique callbacks, and transitions to
`vv/xbox_coop/xc_delta5_1`. Medium predicts 735/0 entities. No executable or
`dmap` was run. Receipt:
[`evidence/checkpoint-027-offline.json`](evidence/checkpoint-027-offline.json).

## Checkpoint 028: Delta 5 part 1 offline preflight

`xc_delta5_1` now has decoded MAP, PROC, AAS48, direct CM and all 333 selected
model members. Its 63 direct MAP samples are closed after 12 source-bound XACT
recoveries. Because the retail archive intentionally has no map-script member,
the builder now emits a receipt-bearing empty PC host main, matching the
existing Admin/Delta 2B treatment. The 284-file overlay has zero unresolved
names, predicts 893 spawned / one inhibited on medium, and preserves the
transition to `vv/xbox_coop/xc_site3_1`. No executable or `dmap` was run.
Receipt: [`evidence/checkpoint-028-offline.json`](evidence/checkpoint-028-offline.json).

## Checkpoint 029: Site 3 part 1 offline preflight

`xc_site3_1` now has source-bound MAP, PROC, AAS48/AAS96, direct CM, all 345
selected models and a dependency-closed 288-file overlay. Thirteen of 65 direct
MAP samples were recovered through the segment XACT routing; nothing remains
unresolved. Medium predicts 839/0. The MAP retains both a co-op Caverns 1 and a
solo Caverns 1 end-level value, so the activated route remains an explicit
gameplay-test item. No executable or `dmap` was run. Receipt:
[`evidence/checkpoint-029-offline.json`](evidence/checkpoint-029-offline.json).

## Checkpoints 030-033: remaining-map offline closure

The four remaining co-op archives—`xc_caverns1_1`, `xc_caverns2`,
`xc_hellhole_1`, and `xc_comm1_1`—now all have decoded MAP, PROC, every shipped
AAS class, direct authored CM, complete model corpora, direct-sound closure and
zero-unresolved portable overlays. The four maps recover 19 Xbox-only WAVs.
Communications applies the same exact two-door `inner1` correction proven in
Delta 2B, while Caverns 1 disables one callback absent from its complete retail
script closure.

A campaign-wide integrity pass selected the latest overlay for all 20 co-op
maps and rehashed all 5,878 payload records: 20/20 passed, with no missing or
changed files, no unresolved names, and direct-authored CM selected everywhere.
No executable or `dmap` was run. Final offline receipt:
[`evidence/checkpoint-030-033-structural.json`](evidence/checkpoint-030-033-structural.json).

## Checkpoint 034: complete Xbox solo structural corpus

The retail disc contains 41 single-player GFC/GOB pairs, including the Xbox
split stages. All 82 archives are now extracted from the identified retail ISO,
and all 41 maps have decoded MAP, PROC, every shipped AAS class, direct authored
CM, and retained source scripts. Each CM export is bound to the exact GPL
geometry CRC computed from its own decoded MAP.

The offline integrity pass rehashed 296 extracted core records and 178 decoded
outputs (594,563,894 bytes): no file was missing, no hash differed, and no
MAP/CM CRC differed. This closes structural decoding, not resource fidelity;
model, dependency, XACT, script and final overlay closure remain. No executable
or `dmap` was run. Receipt:
[`evidence/checkpoint-034-solo-structural.json`](evidence/checkpoint-034-solo-structural.json).

## Checkpoint 035: complete Xbox solo model corpus

All portable Xbox model formats embedded in the 41 single-player archives are
now extracted and decoded with per-file source/output receipts: 14,180 MDV
animations, 670 MDV meshes, and 3,555 hybrid MD5 animations (18,405 files,
872,862,190 decoded bytes). The corpus decoder stages atomically, rejects
case-insensitive output collisions, and uses a short Windows staging path for
legitimate long retail member names.

A second pass reopened and rehashed all 18,405 raw inputs and all 18,405
decoded outputs: 36,810 reads, zero missing files and zero hash mismatches. The
offline suite is 164 tests. Resource, XACT, script and final overlay closure
remain. No executable or `dmap` was run. Receipt:
[`evidence/checkpoint-035-solo-models.json`](evidence/checkpoint-035-solo-models.json).

## Previous checkpoint: 022

**The ninth co-op segment, `xc_recycling2_1`, now has direct authored
collision, corrected player and Mancubus navigation, complete model/XACT
recovery and a bounded true-`COOP` spawn closure.**

The decoded 882-entity MAP binds to geometry CRC `1305987032`. Direct CM.X
exports 105 models; independent PC `dmap` contains all 105 plus 104 models,
every one explained by `noclipmodel 1`. Corrected AAS48 and AAS Mancubus both
have complete nonzero BSP/area coverage. All 341 selected model files decode,
and 29 runtime sounds recover through the segment INDEXLIST/XSB and original
XWB banks. The 305-file overlay has zero unresolved names. All 156 tests pass.

Under the isolated null-guard diagnostic, true `COOP` spawns 880 entities,
inhibits exactly two retail pickups gated out on medium/hard, and joins the
player. All warned sounds and Mancubus path failures are closed. Remaining
notices are source-authored absences: stock Recycling 2 reproduces the broken
light-model and GUI-surface notices. The exact 64x128 diffuse gutter image is
recovered from Xbox D3TFULL; only its referenced normal and specular stages are
absent from both Xbox D3TFULL and stock PC packages. No replacement art is
guessed.
Normal rebuilt-DLL, progression, two-peer and Xbox-reference acceptance remain
open. Full receipts are in
[`evidence/checkpoint-022.json`](evidence/checkpoint-022.json).

## Previous checkpoint: 021

**The eighth co-op segment, `xc_enpro_2`, has direct authored collision,
corrected AAS48, complete model/XACT recovery and a clean bounded true-`COOP`
spawn closure.**

The decoded 579-entity MAP binds to geometry CRC `2033356009`. Direct CM.X
exports 163 models; independent PC `dmap` contains all 163 plus six models,
all explained by `noclipmodel 1`. All 321 selected model files decode, and 11
runtime sounds recover through the segment INDEXLIST/XSB and original XWB
banks. The 285-file overlay has zero unresolved names. All 156 tests pass.

Under the isolated null-guard diagnostic, true `COOP` spawns 579/0 and joins
the player with no map-specific warning, missing resource, callback, class,
path, error or fatal line. Normal rebuilt-DLL acceptance remains open. Full
receipts are in [`evidence/checkpoint-021.json`](evidence/checkpoint-021.json).

## Previous checkpoint: 020

**The seventh co-op segment, `xc_enpro_1`, now has direct authored collision,
corrected AAS48, complete model and XACT-audio recovery, and a clean bounded
true-`COOP` spawn closure.**

The decoded 709-entity MAP binds to geometry CRC `2226283201`. Its 5,495,477-
byte direct CM.X export contains 182 models; independent PC `dmap` contains all
182 plus 26 models, every one explained by `noclipmodel 1`. Corrected AAS48 has
1,112 areas, 5,319 reachabilities and full nonzero node/area coverage. This
archive contains no AAS96.

All 10 meshes and 305 animations in the selected map-local model set decode.
Sixteen missing runtime sounds are recovered through the EnPro INDEXLIST/XSB
and original global/memory XWB banks. Exact receipts also disable one callback
whose only retail body is commented out and one sound shader absent from the
Xbox audio index, correct the retail `grenadeExplosion.ips` typo to the shipped
`.prt`, and select the previously recovered exact `lights/nofalloff` DDS.

The resulting 292-file overlay has zero unresolved resources, classnames or
strings, and all 156 implementation tests pass. Under the isolated instant-hit
null-guard diagnostic, true `COOP` spawns 709/0, joins the player, and emits no
map-specific warning, missing-resource, invalid-joint, callback, class,
path-diagnostic, error or fatal line. The sole unique map-run warning is the
stock PC `mpmain.gui` reference to undefined cvar `s_driver`. Final engine
acceptance still requires the normal source rebuild of the instant-hit guard.
Full receipts are in
[`evidence/checkpoint-020.json`](evidence/checkpoint-020.json).

## Previous checkpoint: 019

**The sixth co-op segment, `xc_alphalabs2_2`, now has direct authored
collision, corrected AAS48, a complete 299-file map-local model set and a clean
bounded true-`COOP` spawn closure.**

The decoded 766-entity MAP binds to geometry CRC `3745531086`. Its 5,784,631-
byte direct CM.X export contains 147 models; independent PC `dmap` contains all
147 plus 114 models, every one explained by `noclipmodel 1`. The corrected
672,630-byte AAS48 crosses the native loader boundary; this archive contains no
AAS96 payload.

All eight meshes and 291 animations selected from the map archive decode with
per-file receipts. The 48-joint skeleton is byte-identical across three
independently recovered co-op segments. No new map-specific compatibility
transform is required: the overlay reuses only the eight already evidenced
shared player/HUD/material/AF transforms.

The resulting 274-file overlay has zero unresolved resources, classnames or
strings, and all 154 implementation tests pass. Under the isolated instant-hit
null-guard diagnostic, true `COOP` spawns 764 entities and deliberately inhibits
two player-two pickups whose retail entities set both `not_medium 1` and
`not_hard 1`. The local player joins with no map-specific warning,
missing-resource, invalid-joint, callback, class, path-diagnostic, error or
fatal line. The sole unique map-run warning is the stock PC `mpmain.gui`
reference to undefined cvar `s_driver`. Final engine acceptance still requires
the normal source rebuild of the instant-hit guard. Full receipts are in
[`evidence/checkpoint-019.json`](evidence/checkpoint-019.json).

## Previous checkpoint: 018

**The fifth co-op segment, `xc_mcu`, now has direct authored collision,
corrected AAS48, its complete 410-file Xbox MDV set and a clean bounded
true-`COOP` spawn closure.**

The decoded 811-entity MAP binds to geometry CRC `2327495450`. Its 3,537,686-
byte direct CM.X export contains 212 models; independent PC `dmap` contains all
212 plus 16 models, every one explained by `noclipmodel 1`. The corrected
466,213-byte AAS48 crosses the native loader boundary; this archive contains no
AAS96 payload.

All 19 meshes and 391 animations in the map GFC decode. Their pruned skeletons
require three exact, path-scoped stock-AF endpoint aliases. Two stale references
in the Xbox security GUI are redirected to the window it actually declares,
and one redundant same-area location entity is made inert while preserving its
effective sibling. `lights/spot08` is recovered by logical name from the retail
D3TFULL rather than substituted.

The resulting 540-file overlay has zero unresolved resources, classnames or
strings, and all 154 implementation tests pass. Under the isolated instant-hit
null-guard diagnostic, true `COOP` spawns 811/0, joins the player, and emits no
map-specific warning, missing-resource, invalid-joint, callback, class,
path-diagnostic, error or fatal line. The sole unique map-run warning is the
stock PC `mpmain.gui` reference to undefined cvar `s_driver`. Final engine
acceptance still requires the normal source rebuild of the instant-hit guard.
Full receipts are in
[`evidence/checkpoint-018.json`](evidence/checkpoint-018.json).

## Previous checkpoint: 017

**The fourth co-op segment, `xc_admin`, now has direct authored collision,
both corrected AAS families and a clean bounded true-`COOP` asset/skeleton
closure.**

The decoded 883-entity MAP binds to geometry CRC `25560181`. Its 1,929,264-byte
direct CM.X export contains 199 models; independent PC `dmap` includes every
one plus 39 models, all explained by `noclipmodel 1`. Corrected AAS48 and AAS96
both cross the native loader boundary.

The admin profile recovers 37 Pinky/zjump/combo MDV files, the Xbox chainsaw AF
and three D3T images. Exact receipt-bearing transforms handle an undeclared inert
`func_spawner`, an absent callback/map script, an exporter-stale Pinky joint and
four material stages whose images are absent from both Xbox and PC retail data.
No surrogate textures or invented entity behavior are used.

The resulting 322-file overlay has zero unresolved resources, classnames or
strings. All 151 implementation tests pass. Under the isolated instant-hit
null-guard diagnostic, true `COOP` spawns 883/0, joins the player, and emits no
missing-resource, invalid-joint, callback, class, path-diagnostic, error or
fatal line. The one no-AAS warning belongs to a prone retail NPC that explicitly
clears `use_aas` on both platforms. Final engine acceptance still requires the
normal source rebuild of the instant-hit guard. Full receipts are in
[`evidence/checkpoint-017.json`](evidence/checkpoint-017.json).

## Previous checkpoint: 016

**The third co-op segment, `xc_mars_city2_2`, now has direct authored
collision, corrected navigation and a clean bounded true-`COOP` spawn.**

The decoded MAP contains 516 entities and binds to geometry CRC `2356338129`.
Its 1,526,425-byte direct CM.X export contains 129 models. Independent PC
`dmap` output contains all 129 plus 42 models, and every additional model maps
exactly to a `noclipmodel 1` entity; there are no unexplained or authored-only
names. The overlay uses the corrected AAS48 with SHA-256
`bf118f9643843b369c6de0c371356aa4150b1509c6c5c2baf951c7ec4bba8657`.

The first bounded run exposed only `lights/nofalloff`. The named texture was
recovered from Xbox `global.d3tfull` as a 296-byte DDS with SHA-256
`1d632a0e7b695186ed6462ff026215fe4bf217c6a57370a5bb9c9dfdd775e11b`.
The stock PC material already declares it, so the finalized closure copies the
DDS only and does not create a duplicate material declaration.

The resulting 276-file direct-authored-CM overlay has zero unresolved names.
The bounded run spawns all 516 entities, inhibits none, joins the player, and
emits no missing-resource, skeleton, AI-path, error or fatal line. Its manifest
SHA-256 is
`53e8f9022d5b399de4a14709cde49497aafaac7143d3865da8928e56f83d567b`.
As in checkpoint 015, final engine acceptance still requires the normal source
rebuild of the instant-hit guard. Full receipts are in
[`evidence/checkpoint-016.json`](evidence/checkpoint-016.json).

## Previous checkpoint: 015

**The second co-op segment now has a complete bounded loader/spawn closure:
all 1,110 entities spawn, none are inhibited, the co-op player joins, and the
run has no missing-resource, skeleton, AI-path, error or fatal line.**

Checkpoint 014 accidentally staged an obsolete pre-plane-fix AAS48. At the
diagnosed zsec route it returned area zero for both endpoints. The corrected
691,857-byte export hashes to
`6e9f0b2cbd8981c3117cb20e029d390c4aa792fd449aad64ae3d241f0f70338e`
and resolves areas `41→39→38→37→35→34`; the native path warning disappears.

A reusable 229-entry co-op-player resource profile now supplies only shared
AF, HUD, player-model, animation, weapon-animation and loop dependencies. It
excludes the first map's NPC, dialogue, ambient and cinematic payload. The one
remaining requested image, `armor_shard.tga`, does not exist in any recovered
campaign/MP or shared Xbox GFC. An exact manifest-recorded transform comments
only those 15 map `inv_icon` epairs, matching the stock PC item's deliberate
omission while preserving pickup gameplay.

The resulting direct-authored-CM overlay has 279 file records, zero unresolved
resources or classnames, and a 137,760-byte manifest with SHA-256
`dd71366abf46be7cc3caa1139cfd50e99938dde726509fe8e3083f01ec24c465`.
The 148-test local suite passes. This bounded run still uses the isolated
instant-hit null-guard diagnostic, so final acceptance requires the equivalent
reviewed `AI.cpp` change and a normal DLL rebuild. Full receipts are in
[`evidence/checkpoint-015.json`](evidence/checkpoint-015.json).

## Previous checkpoint: 014

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
- [Checkpoint receipt](evidence/checkpoint-054-solo-script-bytecode.json): current source hashes,
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

