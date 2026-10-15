# Format findings and unknowns

## Checkpoint 086 reproducibility safeguards

An empty GFC include list means extract everything, not extract nothing. The
structural planner now rejects empty core/resource selections and duplicate
member identities. AAS witnesses must have canonical mode-specific paths and
unique identities; CRC witnesses must be uint32 and bind the exact decoded MAP.
The authentic checkpoint-085 plan remains byte-identical under these checks.

Model-corpus staging must be on the output volume for its final atomic rename.
The new explicit temporary-root option rejects an incorrect volume before
decoding; the runner supplies the new output parent. Neither this portability
fix nor toolchain hash verification establishes retail conversion acceptance.
See [checkpoint 086](CHECKPOINT_086_PORTABLE_RECOVERY.md).

## Checkpoint 085 reconstruction provenance

The pinned ISO's campaign GFC/GOB pairs are disc-root members, not
`base/xc_*.gfc`. Exact GFC extraction selectors retain the original leading
`./`; removing it before matching changes selection semantics.

Receipt ancestry establishes the solo v12-to-v40 and 22-edge co-op chains,
but does not establish every early producer revision or a cold-start build.
Current solo source-MAP hashes match all 41 original structural decode reports.
Nine special AAS outputs originate in the shared assets archive and are now
explicit in the 90-AAS raw structural plan. Raw filename-record hex in
extraction JSON must be discarded before public metadata preservation.

See [solo/raw recipes](RAW_INPUT_RECIPES.md),
[co-op/shared recipes](COOP_RECOVERY_RECIPES.md) and
[checkpoint 085 preservation evidence](../evidence/checkpoint-085-asset-free-recovery.json).

## Checkpoint 084 broader offline review

### Host lineage is part of the input, not a filename assumption

The source imported from the pristine GPL archive and extended on `master`
still registers only stock `si_gameType` values. `idInternalCVar::UpdateValue`
rejects unknown enumerated strings; the game-type enum/server resolver and
paired player-definition branch also lack COOP. Adding a string comparison to
checkpoint spawning did not make this branch reachable through normal mode
selection. Historical first-map configurations store `deathmatch`, and the
logs warn about absent deathmatch starts. Those receipts remain useful for
loader survival only, not paired spawning or cooperative campaign behavior.

`origin/main:vendor/doom3-gpl` contains the COOP cvar, enum, resolver, paired
player definitions, `_coop`/`not_coop` selection, peer limits and broader
player/AI/multiplayer behavior. It lacks some newly reconstructed map-host
classes, including `idTrigger_Teleport`. The next host integration must combine
the two proven source lines in an isolated successor, not replace either
accepted lineage or merely register another mode name. The new
`coop_host_source_audit.py` reports structural prerequisites and source hashes;
it deliberately does not certify a DLL or runtime behavior.

### Warning coverage and navigation identity

The new historical warning auditor checks the recorded bytes/hash of every
log before classifying warnings. It retains repeated summary occurrences,
unknown categories and explicit historical-only limits. Missing spawnclasses,
script callbacks and unsupported entity events cannot be excluded simply
because an earlier targeted skeleton filter did not count them.

Across 41 solo maps and 101 CM/AAS companions, the independent MAP geometry
checksum computation finds exactly one mismatch: `commoutside_1.aas96` stores
2127086718 while the MAP, CM and AAS48 identify 1317835462. The original
authenticated AAS96.X already carries the differing header, and the decoder
retained it. Twenty co-op maps and 50 companions pass the same check. Rewriting
the header alone would bypass a loader safeguard without proving that the
navigation describes the intended geometry; no such rewrite is performed.

Sabaoth's two path-corner warnings also do not justify changing authored AAS.
The direct point queries land in unwalkable leaves, but the GPL bounds-search
fallback can reach walkable areas 23 and 36, with directed authored routes
from area 10. This narrows the problem; it does not emulate trace-down,
dynamic obstacles or the complete `WalkPathToGoal` behavior.

### Additional offline correctness gates

The recorded `stock_pk4s` inventory includes the two pre-existing Xbox MP
add-on packages in this local base directory, not just retail `pak*.pk4`.
Historical duplicate-material warnings name their material file. They are not
new duplicate declarations in the generated campaign tree. A literal reference
scan of both baseline campaign trees finds no dependency on their 59
addon-only paths, but that does not prove their overrides are visually neutral.
Preserve the user's installed packages and record/isolate the base VFS before
future fidelity testing; do not silently delete those packages or call this a
pristine-stock runtime.

Mesh brace balancing was insufficient: `md5_family_audit.py` now checks every
vertex/triangle/weight index, finite coordinate, weight span/joint and weight
sum within decimal export precision. `md5_corpus_audit.py` checks every loose
MD5 individually; it explicitly does not infer compatible family selection.
The baseline solo/co-op trees pass all 838 loose-file checks (53 meshes and
785 animations). Selected family and AF checks are separate obligations.

Package validation now rejects unsafe or ambiguous Windows VFS paths, checks
declaration keys across distinct DEF files, and binds each generated recipe
uniquely to its recorded payload. Language entries are parsed as syntax instead
of quoted text scraped from comments; string IDs retain the case-sensitive
lookup semantics of `idLangDict`. Existing mode packages remain separately
mergeable, not interchangeable combined trees.

The first complete co-op rebuild exposed a Guardian DEF selected both by an
explicit runtime profile and the newly correct typed parent traversal. The
two transformed payloads agreed byte-for-byte, but the builder emitted two
manifest entries. The v20n candidate is retained as rejected. The full-DEF
shadow step now reuses a staged payload only after checking its unique receipt,
size, hash and exact transformed bytes; it retains both source witnesses.
Conflicting candidates fail, and a final case-insensitive duplicate-path gate
prevents any other double-write from publishing a manifest. Three synthetic
regressions raise the complete suite to 455 passing tests.

The next co-op candidate passed strict audits but still contained an unused
Lantern gib in every overlay. Automatic dependency demand had inspected the
global declaration catalog instead of the declarations actually emitted.
The scope is now the selected supplemental declarations plus whole DEF files
that will be shadowed. An unselected catalog entry cannot add that dependency;
explicit resource profiles remain authoritative. The valid-but-broad v20o
candidate remains preserved separately from the final scoped build. Five
additional scope/helper regressions bring the final offline suite to 460 tests.

Co-op GUI snapshots must compare the actual local GUI dictionary with the
authoritative value, not just the previous received value. Otherwise an
unchanged server zero cannot undo a client-side latch. Turkey Puncher score
synchronization likewise uses the actual restored GUI rather than an unsaved
cache. These bounded source repairs preserve snapshot/save field layout, but
cross-lineage save compatibility remains unaccepted: the earlier host already
introduced custom fields under the unchanged stock build number.

### Restored dependencies and selected skeleton families

Typed declaration traversal now distinguishes a model from an entityDef with
the same name, handles unquoted model inheritance and engine-supported
`inherit*` entityDef keys. This exposes the missing Enpro `char_npc` parents.
Both solo Enpro segments now recover exactly five hash-authenticated declaration
slices, not the whole shared `npcs.def`. Four parent declarations receive private
names; the bald-marine child inherits those private parents. The 49 resources
include three 48-joint body meshes, 37 body animations, one 42-joint head mesh,
seven head animations and the authored AF. Body hierarchy/AF checks and head
animation hierarchy pass. The inherited head `copy_joint_world eyecontrol`
destination still does not exist; no guessed replacement is applied.

Maintenance zombies, the actual 43-joint jumpsuit/chainsaw AF consumers, and
the Lantern scientist now select private copies of their exact Xbox AFs.
Only AF names are changed; authored physical values and joint selectors are
retained. Five declared jumpsuit clips remain absent from the inspected selected
resources (`influence_eats_arm`, `influence_shake`, `influence_shake_random`,
`startchainsaw3`, `thrownbyhk`); reachability has not been established. A
Sawyer-family comparison is not evidence for those actual AF consumers.

The generic Xbox skeleton gib and Lantern body both have 48 joints, but 20
ordered joints differ and 14 mismatching indices carry weights. A dedicated
Lantern-only derived gib uses exact joint-name correspondence and the selected
body's hierarchy/bind transforms. It preserves UVs, triangles, shaders, weight
spans/biases and world-space bind geometry within a 0.0001 game-unit tolerance.
All 444 weight coordinates are transformed and 122 indices change. The two
missing source joint names have no weight records, so no alias is invented.
An independent parser and quaternion calculation measured maximum bind vertex
coordinate drift of 0.0000020951 units. This is not motion or visual acceptance.
The existing generic gib alias remains unchanged for other actors.

Recursive literal GUI include closure recovers five missing Hellhole 2 news
`.pd` files. It follows relative-first/global lookup, records source hashes,
includes their language dependencies, and rejects unsafe paths, ambiguous
macro includes and cycles. No menus or compiled scripts are substituted.
Six Comm Outside 2 lift-panel callbacks now retain their authentic helper
namespace instead of being captured by the segmented map's private namespace.
Known `steamlinered`, `ceilingdust` and `longceilingdust` particle references use
the PC `.prt` route with hash-bound stock witnesses; `sonicips.ips` remains
unresolved. The floor-dust FX correction applies to solo Caverns 1 part 2,
solo Caverns 2 and co-op Caverns 2. These are offline dependency/source fixes,
not fresh evidence that historical warnings have disappeared at runtime.

## Checkpoint 083 Hazmat, Sabaoth and validation findings

Hazmat's public Xbox mesh has 48 joints, compared with the PC mesh's 62. Moving
only the mesh to a private path exposed another dependency: `delta4_hazguy`
inherits the PC `char_hazmat`/NPC animation slots and numeric channels. The
repair explicitly rebinds all 14 inherited animation slots, reconstructs
channels by joint name and retains the authored `runoutcough` cinematic/frame
commands. The cinematic Hazmat model already selects matching Xbox resources.
Its two MAP instances explicitly select `hkgrab`/`hkthrow`, so the unused
retail entity default `runoutcough` was not speculatively rewritten.

The shared assets GFC contains the exact matching `char_hazmat.af` and
`char_npc_base.af`. Their finger endpoints are `Rfings2/Lfings2` and
`Rfings1/Lfings1`, respectively; stock PC AFs reference pruned
`Rfings3/Lfings3`. Use the recovered AFs under private declaration names, not
guessed endpoint remaps. AF declaration/settings names are the only AF text
changes; physical values and endpoints remain authored. Replay must execute
this narrow idempotent transform before `static-only` returns, without
recursively re-enabling unrelated full-scope transformations.

CPU 2's first Sabaoth failure is a missing `pain_chest.md5anim`, followed by a
defaulted model and apparent missing look/focus joints. All four Xbox pain
tracks are absent from stock PC packages. The decoded mesh and 13 animations
share exactly 50 ordered joints; PC's public family has 73. Replaying the entire
private Xbox family closes that asset defect, and `mech_spine_1` and
`organic_head` remain present. The stock Sabaoth AF references only `origin` and
is compatible with the recovered skeleton. No joint suppression or authored
AAS alteration is justified by the defaulted-model cascade.

Joint comparison rules differ by use. `idMD5Anim::CheckModelHierarchy` requires
exact ordered names and parent indices. `idRenderModelMD5::GetJointHandle`
resolves actor/AF references case-insensitively. An initial auditor incorrectly
rejected valid lowercase Hazmat AF selectors such as `ruparm`; the regression
test now preserves the distinction. The rejected audit receipt is retained as
an auditor counterexample, not evidence of bad retail AF data.

Numeric GUI warnings originate in the host precache loop treating Xbox
`gui_distance`/`gui_zoom` spawnargs as filenames. Excluding those exact keys
preserves ordinary `gui`/`gui2` resources and all MAP metadata. It does not
implement Xbox interaction-distance/zoom semantics. The separate absolute-path
warnings originate in the stock parser's failed first relative-include probe,
followed by virtual-path fallback; inspected campaign scripts contain no
serialized `C:/Program Files` paths. Real mixed-case asset spelling remains a
separate portability concern.

Validation must examine bytes and evidence, not labels. The merge auditor used
manifest hashes without rehashing payloads, and the tree auditor compared full
include directives with bare removed filenames. Both could falsely pass. Native
soak resume also omitted idle-duration checks, and a non-aborted runtime failure
could return exit zero. Regressions now cover changed payloads, restored
includes, insufficient/invalid idle evidence and failure exit status. Offline
PowerShell tests extract and execute only pure report-validation functions;
they never execute the native runner body.

## Checkpoint 082 source-bound actor-family findings

An animation's existence is not enough to make it compatible. The decoded
Xbox Sentry and maintenance-zombie clips both use 50 joints, but the stock PC
meshes published at their public paths use 55 and 90. Adding only the missing
clip makes the declaration parse farther and then fail on joint count. The
portable unit is the whole selected skeleton family: mesh, every active
animation and every map-specific derived animation must move together beneath
a private runtime prefix.

Accepted-overlay replay is a separate transform path. It intentionally runs a
narrow idempotent scope so older host rewrites are not applied twice. A new
private-family transform that exists only in the full scope can copy all of its
assets while leaving replayed DEF text unchanged. Tests must therefore cover
both fresh and replay scopes and assert the output declaration, not merely the
resource manifest.

Derived declarations can extend the family. Communications adds
`wall_release_dummy` and `wall_release_idle` to the base Sentry model. The
first corrected family removed the original warnings but exposed a new
joint-count failure at that derived declaration. Dependency closure must trace
all inherited and added animations across map DEFs; a base modelDef alone is
not the complete runtime type.

## Checkpoint 074 split-cinematic reconstruction findings

The Xbox Hellhole DEF preserves exact Maya export ranges even though its four
camera files are absent as standalone recovered members. Those ranges map back
to the same retail PC take: Xbox B/C/D exactly equal PC F/H/I, while Xbox A is
frames 237-275 from PC D followed by PC E's 276-340. Camera samples can be
joined directly. The analogous player A segments use different sparse
component masks, so each pose must first be expanded to all six MD5 components
per joint before concatenation; copying component arrays would corrupt poses.

The recovered cinematic Cyberdemon animations are 50-joint Xbox data and must
not use the stock PC cinematic mesh. Mesh, bind pose and all four tracks now
live under one private Xbox prefix. The frame counts then align exactly across
camera, Cyberdemon and player: 104, 32, 120 and 252.

## Checkpoint 073 inherited-model and replay findings

Replacing an inherited model mesh is not sufficient on the PC host. Doom 3's
derived model declaration can retain the parent's already-resolved numeric
`channelJoints` arrays even when the child mesh has a smaller skeleton. The MCU
failure appeared inside `idMD5Anim::GetInterpolatedFrame`: a valid 48-joint
Xbox animation was indexed through inherited PC channel entries reaching joint
59. Any private Xbox NPC mesh override must therefore re-declare torso and legs
channels by joint name so the engine resolves them against the selected mesh.

A generated private alias is also not proof of provenance. Delta 2B part 2 had
a contaminated 63-joint ZCT under the desired private path; ordinary Xbox ZCT
is a 50-joint family. Source-bound aliases must be regenerated from the decoded
public source path ahead of prior-overlay fallbacks, even when the fallback
already has the requested destination name.

Finally, stock child declarations can reintroduce public resources after a
private base-family transform. Hellhole's stock child added the 71-joint public
`impcyberwakeup` animation to the private 41-joint Xbox Imp base. The compatible
solution shadows that one stock DEF and retargets only the affected child
animation, keeping the rest of the stock declaration behavior intact.

## Checkpoint 072 merged-campaign skeleton findings

Per-map loader success does not prove that its resources are safe in a merged
campaign tree. The first complete replacement sweep passed 31 maps but exposed
ten failures from only three shared-path families: Campbell, ZCT and
Cyberdemon. Older per-map manifests can preserve a now-obsolete public resource
in `copied_runtime_resources`; changing the new declaration is insufficient if
replay still republishes that old file. Rebuild must filter the public source
path when the family moves to a private prefix.

Skeleton isolation is also use-specific. Ordinary Xbox commandos require the
private coherent 50-joint ZCT mesh/animation family. Monorail's seated commando
cinematic instead uses the stock PC public mesh and stock cinematic animation;
pointing that declaration at the private Xbox mesh creates a new mismatch. A
logical character name therefore cannot determine the transform by itself:
the declaration's animation family and loading context are part of its type.

Finally, derived-resource root order is semantic. Hellhole's raw 50-joint Xbox
pain tracks and accepted 78-joint PC-host retargets have the same virtual
paths. The accepted retarget roots must precede raw structural model roots or a
reproducible rebuild silently selects the wrong skeleton despite clean static
dependency closure.

## Checkpoint 071 loader-closure findings

Script compatibility must preserve the Xbox action rather than merely make the
source compile. Site 3 calls `sys.runCommand` to issue a host command, but the
stock PC script event table has no such event. Adding a narrow string-taking
event to the reconstructed game DLL and buffering the command keeps the Xbox
script intact and crosses the PC loader boundary. A declaration-only shim or a
script no-op would hide the missing behavior.

Namespace isolation can also expose an intentionally external helper. Comm
Outside part 2 declares a map-local namespace while its two `lift_main` calls
belong to the stock `map_commoutside` helper. Renaming every identifier into the
private namespace is wrong; those two calls require an evidence-scoped
qualification after isolation.

Model compatibility is a family constraint, not a file-by-file dependency
problem. Lantern, Hazmat, Campbell/ZCT and Vagary failures all resulted from a
valid Xbox animation, AF or bind pose being paired with a different PC skeleton
under the same logical model family. The accepted method gives incompatible
Xbox families private runtime paths and closes every selected animation/mesh/AF
member coherently. This avoids global declaration collisions and prevents a
later map's stock definition from silently changing an earlier map's skeleton.

Finally, replaying a generated overlay is not equivalent to replaying its
authenticated provenance. A rebuild may use the old overlay as a late runtime
resource root, but original structural/script/model roots must remain earlier,
and an existing generated bridge must be recognized and regenerated rather
than mistaken for a retail-authored direct map script.

## Checkpoint 066 native-itinerary findings

Transition inventory alone overstates the playable graph. The co-op Site 3 map
retains a renamed solo `caverns1_1` exit, and `xc_hellhole_1` retains a
`hellhole_2` next-map target. Both have zero incoming MAP links. The actual
co-op terminal is the separately linked `target_endlevel_3` with `endOfGame 1`.
Similarly, solo `hellhole_2` ends through its linked `target_endlevel_2`.

Tracing only authenticated internal edges produces complete acyclic routes:
41 solo maps and 20 co-op maps, each exactly once. The plan records an explicit
map command for every segment rather than assuming that a successful first
load proves the rest. It also separates loader-only, route/progression,
two-peer and matched visual/audio phases so a failure has a precise boundary.

An `fs_game` alias alone is not an immutable test handoff because Doom writes
`DoomConfig.cfg` and `qconsole.log` beneath its save path. The plan therefore
uses a separate `fs_savepath`. The root alias may be a local junction for
convenience; the accepted tree behind it remains an ordinary-file artifact and
rehashes to its checkpoint-065 ledger. No native execution is claimed here.

## Checkpoint 065 unified-tree findings

Per-map closure does not imply whole-campaign merge safety. The 7,872 manifest
records reduce to 1,572 virtual paths. Within each campaign, 455 shared paths
are byte-identical; three paths legitimately vary by map. Across the solo/co-op
boundary, 115 paths are shared and every one is byte-identical. The varying
language closures union to 101 solo and 47 co-op IDs with no value conflict.
The 20 co-op runtime DEFs union to 25 declaration keys with no body conflict.

That result was still insufficient. The first unified-tree audit correctly
rejected five runtime declarations because another map caused their complete
source DEF file to enter the same tree. They are
`target_coop_increase_spawnlevel`, `trigger_coop_enablegui`,
`monster_boss_guardian_coop` (entity and model), and `trigger_teleport`.
The accepted builder indexes every non-supplemental DEF, verifies each overlap
has the exact normalized body, then omits only the redundant supplemental copy.
Any difference or any duplicate among complete DEF files is fatal. Repeated
`export fred/james` conversion directives are not runtime idDecl identities and
are deliberately outside that collision rule.

The independent v2 audit rehashes the exact file allowlist, rejects extras and
reparse points, requires every MAP's PROC/CM companions, reparses all 78 DEF
files, and reparses all three material files. This proves a structurally clean
test tree, not that the engine accepts declaration order or that any map plays
correctly. The 1.009 GB tree is local retail-derived test data and must remain
outside Git and distribution.

## Checkpoint 064 co-op portable-package findings

The final co-op generation exists as 20 separate development overlays beside
many older generations. A recursive "latest manifest" heuristic is useful for
auditing work in progress but is not a reproducible packaging selector: copied
manifests or unrelated later work can change modification-time ordering. The
co-op packager therefore requires the exact accepted suffix and searches only
matching direct children of the named source root.

Each manifest is validated as a co-op runtime overlay with a unique Xbox co-op
map identity. Its entries are the only payload allowlist. The packager checks
source and destination size/SHA-256, preserves the manifest bytes, excludes
everything unlisted, stages to a temporary sibling, refuses an existing
destination and publishes atomically after all 20 maps close. The independent
audit then requires no untracked file and reproduces both accepted ledgers.

This establishes deterministic package identity, not native two-peer behavior.
The package is local retail-derived data and must remain outside Git and public
distribution. Loader selection, host/client synchronization, progression,
respawn, save/load and matched Xbox visual/gameplay fidelity remain native test
obligations.

## Checkpoint 063 portable-package findings

An audit view is not automatically a safe test artifact. Thirty-nine of the
41 final solo map directories are NTFS junctions to earlier accepted overlays;
copying or archiving that tree with a junction-aware tool can preserve host
paths, omit content or unexpectedly traverse outside the intended root. The
package step therefore treats each overlay manifest as the sole allowlist and
never enumerates payloads for inclusion.

For every listed file, the packager verifies the source size and SHA-256,
copies it into a temporary ordinary directory, then verifies the destination
size and SHA-256. It copies the exact manifest bytes, excludes untracked files,
refuses an existing destination and renames the completed stage into place.
The resulting corpus contains no reparse points. Its independent corpus audit
has the same per-map records and campaign-wide ledgers as the accepted
junction-backed view.

This solves portability and accidental-inclusion risk only. The package is
local retail-derived test material and must not be committed or redistributed.
Matching hashes do not establish native loading, rendering, collision,
visibility, progression, save/load or gameplay fidelity.

## Checkpoint 062 campaign-matrix findings

Aggregate totals can hide a missing map. The final matrix therefore compares
the complete case-insensitive map set in every applicable report against the
overlay baseline, rejects duplicates, and fails on each report's own unresolved,
missing, failure or port-regression boundary. It also binds every input report
by length and SHA-256.

The matrix contains 492 solo and 200 co-op per-map cells. Solo gates cover the
overlay, semantics/transitions, direct audio, entity links, script entities and
reachability, frame and GUI commands, AAS requirements, script sounds, compiled
callbacks and player topology. Co-op gates cover the corresponding overlay,
semantics/transitions, links, scripts/reachability, AAS, sounds, two-path
callback bytecode, resurrection and paired spawn topology.

One boundary must stay explicit: the co-op raw script-entity audit reports 60
unprofiled records. Those are not silently discarded; its matrix coverage is
paired with the source-bound reachability report, which classifies them and has
zero port regression. Similarly, attention lists remain evidence even when a
gate is green. A matrix cell proves audit coverage, not engine execution or
fidelity.

## Checkpoint 061 solo player-topology findings

The final solo overlays preserve exactly one `info_player_start` in every Xbox
segment. Player topology is bound to the decoded source through the manifest's
source MAP hash, not inferred from the stock PC campaign. All start, teleport
and legacy deathmatch epairs match those source maps exactly.

Of 42 `info_player_teleport` entities, 38 are addressed by a MAP reference and
one by an active direct `$entity` script expression. Three have neither static
path: Alpha Labs 3 `info_player_teleport_1`, Hell 1 part 3
`info_player_teleport_2` and Hellhole 2 `info_player_teleport_3`. Monorail 2
also retains one `info_player_deathmatch`. These four records are present in the
authenticated sources, so uniformity is not a valid reason to remove them.

Exact entity preservation does not establish the runtime-selected start,
collision clearance, teleport activation, target side effects or save/load
state. A computed name or native path can also escape the two exact-reference
scans. Those are gameplay observations rather than reasons for an offline map
rewrite.

## Checkpoint 060 co-op spawn-topology findings

Co-op spawn validation must use effective `spawn_level` defaults: player-one
and player-two definitions default to level one, while the optional safe spawn
defaults to zero. Counting only explicit MAP epairs misclassifies many authored
initial points. Several maps also retain multiple player pairs at one level,
including entities whose historical names still say `info_player_deathmatch`;
the classname and effective level, not a filename-style suffix, define their
runtime role.

All 20 maps have equal player-one/player-two multiplicity at every effective
level, a level-one pair and no gaps. There are 50 pairs total. Pairing by the
minimum source-space separation avoids assuming that legacy entity-name suffixes
encode identity. All spawn/start/advance entity epairs match the hash-bound
decoded MAP sources exactly.

The 22 `target_coop_increase_spawnlevel` entities have 31 incoming MAP links.
Link presence proves topology, not how many times a trigger fires or which
point the runtime selects. Three maps have no safe-spawn entity and six pairs
face different angles; both patterns are authenticated source content. Native
two-peer spawn, telefrag avoidance, progression and rejoin observation remains
required before changing those placements.

## Checkpoint 059 co-op resurrection findings

The official GPL opcode order continues from `OP_CALL` 96 to `OP_THREAD` 97
and `OP_OBJTHREAD` 98. A global thread stores its function operand in statement
A, so the recovered function-varDef mapping used for calls also resolves that
case. An object thread instead stores an object in A and a virtual-function
immediate in B. Counting those statements is exact; resolving their method
symbol requires an additional serialized-varDef grammar and is not guessed.

Across the 20 startup programs, the added decoder finds 51 global thread
statements and 32 object threads. None of the global call/thread operands names
the resurrection initializer, resurrection callback or either player-death
method. The active recovered source contains no player-death method call
expression, and no MAP/script root reaches `Coop::initCoop`.

The earlier two Hell attention records are not missing conversion content.
Hell 1-1's `trigger_relay_114` has no incoming entity link or active script
reference. Hell 1-2's `trigger_relay_118` is targeted only by hidden
`resurrect_gui_0`; the matching pad is hidden, the initializer/reveal function
is unreachable, and no numbered resurrection point exists. The raw decoded
sources contain the same records. Enabling them or creating a point would
invent behavior, so they remain byte-preserved dormant residue.

The retail XBE has no exact ASCII instance of the six helper/state terms. That
is supporting negative evidence, not proof that arbitrary indirect machine
code cannot enter the functions. The 32 virtual object threads also remain
symbolically unresolved. Two-peer death, spectator, rejoin and respawn testing
therefore remains required even though the static MAP/startup path is closed.

## Checkpoint 058 co-op script-sound and rebuild findings

Co-op overlay selection needs the same script-literal sound boundary as solo.
Across all active calls, only the MCU split named the nonexistent third
machinery set. The declaration and source witnesses are independent: the Xbox
sound metadata proves `mset3` did not ship, while the unsplit PC script proves
the matching third-howitzer behavior is `mset2`. Correcting those two literals
is therefore recovery of shipped intent, not substitution by convenience.

Generated overlays are valid resource roots, but they are not always suitable
provenance roots. An idempotent correction is no longer visible as a fresh
transform when a corrected overlay is fed to the builder again. The corpus
rebuilder now accepts an explicit input suffix so a final candidate can be
derived from the named accepted checkpoint and carry fresh input/output
receipts for every new correction.

The same rebuild exposed a byte-idempotence bug in four stale callback guards.
A substring count also matched an already-commented call and prepended another
`//` on each generation. The transform now matches one complete epair line,
distinguishes active from disabled form, and normalizes any legacy repeated
prefix to one comment. The callback remains disabled; only unstable generated
markup changes. A second pass is byte-identical.

## Checkpoint 057 solo script-sound findings

Script sound dependencies are a separate closure boundary from map speaker
spawnargs and direct WAV fields. Scanning only declarations or MAP entities
does not prove that literal names passed to `cacheSoundShader` and
`startSoundShader` exist. The new audit strips comments, follows all overlay
scripts and checks active literal calls against the installed stock-PC sound
shader set.

The only gap in 41 maps was the Xbox MCU split's `mset3_movement` and
`mset3_stop`. This is not evidence of a missing bank: the authenticated Xbox
global sound metadata contains the first two machinery sets and no third set.
The unsplit stock-PC source is a stronger semantic witness: its identical
`howitzer_3` code uses the second set for both movement and stop, while caching
only sets one and two. The port therefore corrects six literal occurrences to
`mset2`; it does not synthesize shaders, samples or declarations.

The AAS corpus auditor also learned to retain logical overlay paths when maps
are exposed through a local junction/symlink audit view. Resolving every match
first incorrectly moved inherited paths outside the requested root. This was a
reporting-path bug only; hashes and parsed AAS bytes are unchanged. Release
packaging must contain ordinary files, not the audit view's link metadata.

## Checkpoint 056 co-op callback compilation-boundary findings

Co-op `.script.bin` cannot be treated like the solo per-map compiled program.
Its source metadata names a sibling `*_main.script`, and the recovered main
source shows the exact include closure. Map-specific functions appear in the
binary only when that main unit explicitly includes their source. The engine's
separate worldspawn map-script load supplies the remaining MAP callbacks.

The positive cases prove the distinction. `xc_admin_main.script` includes
`script/map_admin.script`, and `map_admin1::kill_wounded_marine` is compiled.
`xc_mcu_main.script` includes `script/map_mcu_1.script`, and its two
`close_secdoor` callback records resolve to the compiled function. Conversely,
`xc_mars_city2_1_main.script` includes AI, player and co-op support but not its
sibling map script; its three functional MAP callbacks therefore correctly
remain outside startup bytecode and are provided by the audited map-load source.

Across the corpus, six of 60 functional callback records are startup-compiled
and 54 are map-load source records. Absence from startup bytecode is not itself
a missing function. A valid audit must first bind each binary to its compilation
unit and then preserve the semantic source audit for the second load path.

## Checkpoint 055 co-op script reachability findings

Direct script references need control-flow classification, not a blanket rule.
A missing entity used as a receiver can be a deliberate inert visual remnant,
while a missing required entity argument to a system event terminates the PC
script thread. The latter becomes a progression defect when later statements
carry gameplay actions.

`xc_mars_city2_1` demonstrates that distinction. Its split Xbox MAP omits
`speaker_281` and `speaker_282`, but `connect_sarge_speaker` still triggers both
before `trigger_relay_111`. The official interpreter rejects a null required
entity argument and marks the thread dying. Guarding only those two absent audio
triggers preserves the authored delay and monitor behavior and makes the final
relay reachable; adding stock-PC speaker entities would instead invent content
for the split map.

EnPro 2 is the opposite case. The MAP retains the `machineclaw1_move` callback,
but the controlled machinery was renamed with `vv_` prefixes and the script's
setup block is explicitly marked `vv remove`. Its thread reaches a missing
`waitFor` argument and ends, while the same trigger independently targets the
combat maggot. Those 63 records are source-authored disabled visual machinery,
not names lost by conversion, so the port does not reactivate them without a
runtime witness.

The shared resurrection helper remains a bounded unknown. It constructs
`RESURRECT_POINT+i` in both Hell splits, but the compiled scripts contain no
call to `Coop::initCoop`. An external C++ name-based invocation has not been
excluded because the reconstruction repository is unavailable with current
credentials. The maps are therefore preserved pending source access or the
later deliberate two-peer test rather than receiving invented resurrection
points.

## Checkpoint 054 solo compiled-callback findings

The recovered function-record grammar also handles unqualified function names;
this matters for establishing the common statement-array base even when the
last compiled function is global. With that extension, all 41 solo binaries
infer base 4,100 and decode without a structural exception.

Source-text symbol closure alone can accidentally accept a function left only
inside comments or otherwise omitted from the shipped program. Cross-referencing
the 41-map semantic report against each binary's recovered function table closes
that gap: all 403 namespaced MAP callback records have an exact compiled name.
The two `target_callobjectfunction` records resolve by method suffix to compiled
`char_sentry::flashlight_on` and `char_sentry::flashlight_off`. No functional
callback is text-only. Four already documented retail-PC warning/no-op records
remain exceptions by provenance, not missing-port regressions.

## Checkpoint 053 compiled-script findings

The Xbox `.script.bin` payload is a serialized Doom script program, not native
machine code. It starts with length-prefixed source metadata and an include-file
list, then a counted global-data image. Namespaced functions can be recovered as
records containing statement range, parameter/local sizes, name, file number,
definition/type indices, parameter sizes and event index. The final statement
array is counted and consumes the remainder of the file; each statement is
eight bytes of little-endian `uint16 a, b, c, opcode`.

All 20 co-op binaries independently infer the same 4,100-statement base. Opcode
96 is `OP_CALL` in the official GPL `Script_Compiler.h`. The operand mapping is
not inferred from the absent call: all 16 binaries containing `coop.script`
also yield exactly one compiled `Coop::initCoop -> Coop::showResurrectors` call
and two `Coop::resurrect_player -> Coop::getNearestLocation` calls.

Against that validated decoder, the corpus has zero `OP_CALL` statements whose
target is `Coop::initCoop`, and no compiled function name ending
`::setupCoop`. Therefore finding `Coop::initCoop` as printable text proves only
that the shared function was defined. It does not override the text-source and
MAP evidence that the retained `setupCoop` callbacks are stale. This does not
exclude a C++ function-name lookup outside bytecode and does not establish
two-peer resurrection behavior.

## Checkpoint 051 co-op entity-link findings

Co-op link closure needs the same case-insensitive lookup rules as the engine,
but source comparison cannot rely on filenames alone. Each overlay manifest
records the decoded MAP input hash before compatibility transforms. Selecting a
retained decoded source by that hash prevents a later intermediate or another
candidate with the same basename from laundering a port regression.

Across 4,654 link-bearing spawnargs, 667 targets are absent from their local
split map. Every one is identically dangling in the hash-matched Xbox source;
they are preserved split-map or editor residue, not names lost during export.
They remain runtime-attention records because source provenance does not prove
that an engine path never executes them.

The Site 3 source contains both `target_endlevel_1` and
`target_endLevel_1`. Doom 3 name lookup is case-insensitive, so this is one
collision even though the text differs. The converter preserves both spellings
and the audit classifies the collision as source-authored. Choosing or renaming
one without execution evidence would alter the terminal transition.

## Checkpoint 050 co-op overlay receipt findings

An overlay manifest is a set, not an event log. A resource may satisfy several
dependency discoveries, but its virtual path needs exactly one final receipt.
The direct-WAV pass previously appended another receipt when the runtime
resource pass had already copied that WAV. Bytes on disk were correct, yet the
manifest was noncanonical and a naive byte total double-counted 18 records.

The corrected builder first checks the staged destination. If it exists, the
direct MAP reference is already satisfied and no copy or receipt is added.
This preserves provenance from the explicit runtime profile and makes manifest
cardinality equal the actual payload-file count. Corpus validation now rejects
duplicate, missing or hash-mismatched manifest records and distinguishes
engine-local config files from untracked content.

A co-op AAS corpus ledger must also use canonical `<map>/<aas-name>` paths.
Hashing development candidate directory names makes a content ledger change
after a manifest-only rebuild. Canonical names and canonical sort order keep
the navigation corpus identity tied to map content instead of workspace layout.

## Checkpoint 049 co-op AAS requirement findings

The co-op maps use the same `use_aas` inheritance contract as solo, but the
required navigation is not limited to the ordinary `.aas48`/`.aas96` pair.
Resolving the final entityDefs across direct MAP entities, entityDef-valued
spawnargs and literal script spawns found eight boss/large-actor instances in
two maps whose exact authored classes were absent from their overlays.

Those classes were present in the authenticated shared Xbox archive:
`xc_hell1_2.aas_guardian.x`, `xc_hell1_2.aas_mancubus.x`, and
`xc_hellhole_1.aas_cyberdemon.x`. The preexisting
`xc_recycling2_1.aas_mancubus` was already correct. The recovered files add
989 areas, 2,862 reachabilities and 4,481 nodes; every nonzero node and area is
covered by its BSP. Overlay rebuilds changed no prior payload, demonstrating
that the correction is navigation-only rather than a dependency-closure drift.

Latest-overlay selection matters because development leaves older immutable
candidate directories in place. The co-op corpus auditor groups manifests by
virtual map name, selects the newest candidate, and audits only AAS files whose
basename matches that map. This prevents stale candidates or solo files from
inflating the result.

## Checkpoint 048 entityDef-driven AAS findings

File-family enumeration is insufficient for navigation closure. The effective
`use_aas` spawnarg must be resolved through entityDef inheritance for every
actual AI root, including direct MAP classnames, entityDef-valued MAP
spawnargs and literal script spawns. An empty override is a distinct deliberate
state; a nonempty value requires `maps/vv/<map>.<use_aas>`.

That cross-check found 17 direct instances across five maps requesting four
special classes absent from strict v9. The absence was a pipeline-selection
defect, not missing retail content: the shared Xbox archive contains exact
`aas_sabaoth.x`, `aas_mancubus.x`, `aas_guardian.x` and
`aas_cyberdemon.x` members. Special AAS data is therefore shared-map content,
whereas the ordinary AAS48/AAS96 members live in each map archive.

The five corrected exports add 1,495 areas, 3,631 reachabilities and 5,802
nodes. Each has complete nonzero BSP-node and area coverage. Renaming AAS48 is
invalid because the settings and actor bounds differ; copying stock PC files
is also invalid because their map CRCs and unsplit geometry differ. Strict v10
uses only the authored Xbox payloads with their own class suffix and converted
plane representation.

## Checkpoint 047 solo AAS corpus findings

The strict solo overlays carry 55 decoded navigation files: one AAS48 for each
of 41 segments and the 14 AAS96 classes shipped by the corresponding Xbox
archives. Corpus validation must parse the final packaged files rather than
trust the extraction manifest alone. It verifies standard `DewmAAS 1.07`
structure, inverse plane pairing, BSP reachability from node one and use of
every nonzero area as a BSP leaf.

All files pass. Together they contain 45,857 areas, 226,989 directed
reachabilities, 158,002 nodes and 49,217 plane inverse pairs. Every file has
zero unreachable nonzero nodes and zero unreferenced nonzero areas. This proves
the corrected plane-distance export and structural graph coverage survived
final packaging; it does not prove a particular actor origin/bounds maps to the
intended area or that doors and obstacles enable a route at runtime.

## Checkpoint 046 in-world GUI command findings

GUI files cannot be audited without their MAP instance. A GUI `runScript
"gui::gui_parmN"` appends the instance's `gui_parmN` value to the returned
command stream; it does not name a fixed script function in the GUI file.
Those values may also be `#str_` identifiers and must pass through the loaded
language table before `gameLocal.program.FindFunction`. An unset parameter
leaves no following token, so `HandleGuiCommands` performs no call and
continues; treating it as a missing function is a false error.

The returned game commands have three entity/script paths. Bare `activate`
calls `entityGui->ActivateTargets`, so its references are the already-audited
MAP target graph. Named `activate` and `setkeyval` use case-insensitive
`FindEntity`. Returned `runScript` is a hard function lookup and errors when a
nonempty symbol is missing. The audit binds every overlay MAP entity's `gui*`
spawnarg to overlay files first and then the exact installed PK4 view.

Across 1,700 GUI instances, 128 nonempty localized/dynamic runScript values
resolve, 63 named entity operations resolve, and 893 bare activations use the
owner's targets. Twenty parameter reads are empty no-ops. Three named
activations are absent from both source and overlay: CPU `com_walk1` and MCU
`trigger_cranemaint` in each split segment. They are retained source-authored
attention records rather than retargeted guesses.

## Checkpoint 045 animation frame-command findings

Frame-command auditing must follow selected declarations, not copied DEF
files. Dependency closure copies a whole DEF when one declaration is needed;
unselected model blocks can contain legacy commands such as Caverns 2's
undefined `hk_fireball`. The decl manager does not parse that model merely
because its file is present. The overlay manifest's selected `model` records
are therefore the fail-closed execution scope.

Within a selected model, `call` is resolved immediately through
`gameLocal.program.FindFunction`, `object_call` is resolved against the
animated entity's script object when the frame executes, and `trigger` uses
case-insensitive `gameLocal.FindEntity`. Across the solo corpus, all 331
selected global/namespaced calls and 172 defined object-method names resolve;
23 trigger commands resolve to local entities. Twelve selected trigger
commands name entities absent from both the decoded Xbox source map and its PC
overlay, so they are preserved split-map residue rather than conversion loss.

The selected stock `monster_boss_vagary` model contains `object_call
sonic_attack`, but that method is absent from both the complete stock PC script
corpus and the decoded Xbox Vagary script. Because `object_call` is late-bound,
this is a runtime attention item rather than a declaration-load failure. The
retail declaration remains byte-preserved; inventing a method would change the
Vagary's attack without an Xbox implementation witness.

## Checkpoint 044 reachable script-domain findings

A conservative computed-name profile is not the same as a reachable call
domain. Comm Outside reaches only `airlock_door_open(2,2)` in segment 1 and
`airlock_door_open(3,2)` plus `airlock_door_close(4,1)` in segment 2. Expanding
those exact arguments produces 14 and 25 names respectively, all local. The
MCU pair helpers are broadly profiled with bridge numbers 1, 3, 5 and 7, but
both scripts assign `NUM_BRIDGES = 4` and return before entity lookup when the
argument is greater. Only 1 and 3 can reach the lookup, producing eight local
records per segment. Reachability-domain narrowing must remain a validated
subset of the broad audit profile; it must never add an un-audited name.

Monorail 2 requires source-control-flow evidence beyond a function-level call
graph. Its `main2` assigns `TRAIN_MOVING = 3` before the sole script call to
`move_train`; the state-3 branch calls `train_proceed` and returns before four
first-half references. Its sole MAP callback entity is `noTouch`, bound to the
train, has no incoming target, and is absent from direct, computed and GUI
script references. The profile records all of those witnesses and the auditor
fails closed when a source regex, caller set or callback witness changes.

The only remaining required-null call is Comm 1 `door_bang`'s final statement,
which passes the absent `$monster_zsec_shield_4` after the callback's door-bang
actions have completed. It can terminate only the already-finished thread.
This is retained as explicit native-attention evidence, not erased or called a
local entity.

## Checkpoint 043 PC worldspawn dispatch findings

The stock PC worldspawn has two independent startup paths. After compiling
`maps/<map>.script`, `idWorldspawn::Spawn` schedules global `main` when it is
defined. It then iterates every worldspawn spawnarg beginning with `call` and
schedules those functions as separate threads. A generated global bridge that
calls the same namespaced function already named by the retail worldspawn does
not provide compatibility; it runs map initialization twice.

Forty of the 41 decoded solo maps contain one worldspawn call that exactly
matches the recovered segment initializer, including the two numbered
`main2` cases. Their PC bridge must include the recovered map-script sources
without defining global `main`. `delta4` is the only decoded solo map without
a worldspawn call. Its recovered script still defines the intentionally empty
`map_alphalabs4::main`, so that one bridge emits a global-main fallback.

The builder now fails closed if a worldspawn call names a different symbol,
names the selected entrypoint more than once, or the recovered source does not
define the selected function. Its manifest records `retail-worldspawn-call` or
`generated-global-main-fallback`, the exact symbol, and every observed
worldspawn call.

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

## 5. Compiled static render models (`.lwo.x` / `.ase.x`)

Checkpoint 078 establishes the renderer-static-model payload independently of
the collision `.cm.x` payload. A full GFC inventory—not a selective extraction—
contains the exact compiled render members for eleven previously warned paths.
The decoded file begins with a little-endian surface count. Each surface stores
a 32-bit surface identifier, a length-prefixed material name, six float bounds,
two one-byte flags, a 32-bit index count with 16-bit indices, and a 32-bit vertex
count followed by 36-byte draw vertices. Each vertex is `5f + 4I`: XYZ, ST,
packed NV2A normal, two packed tangents and four color bytes.

Surface identifiers are not reliably sequential. The strict decoder therefore
finds the next header only when all count, flag, finite-float, material-path and
index-range constraints validate. Bytes between primary surface arrays are
renderer-derived data: they are bounded and SHA-256 recorded, not guessed into
the PC export. The PC ASE writer compensates for Doom 3's ASE reader by swapping
the emitted B/C winding, writing `1 - T`, and using retail-style synthetic
absolute bitmap paths containing a `base` component. The material name remains
authoritative. RGB vertex color is retained; stock ASE cannot represent the
fourth `idDrawVert` color byte, which remains an explicit fidelity boundary.

The stock `recycwallight.ase.x` control preserves the stock PC material set and
2/14/2 triangle split. Xbox vertex splitting differs (4/26/4 versus 4/10/4), as
expected after renderer preprocessing. Native focused logs show the decoded
models loading and contain no targeted missing-model or ASE bitmap-path warning.
This is structural/native-load evidence, not yet a matched Xbox screenshot or
vertex-alpha acceptance test.

Checkpoint 080 extends the same format over sixteen further unique solo
payloads (seventeen archive instances because both Monorail segments contain
the same `test_noglass.lwo.x` bytes). They contain 80 declared surfaces, 30,840
vertices and 28,005 triangles. Eight surface slots have no indexes or vertices.
Their bounds are the engine's canonical empty sentinel: minimum components are
approximately `+1e30` and maximum components approximately `-1e30`. A zero
vertex surface is accepted only with that sentinel and zero indexes; a sentinel
on non-empty geometry and a zero-vertex surface with ordinary bounds both fail.

The Xbox payload retains empty authored material slots, but the stock PC ASE
reader rejects an empty `GEOMOBJECT`: after seeing zero faces it reports
`*MESH_TFACELIST before *MESH_FACE_LIST`. The PC translation therefore keeps
the slot in `MATERIAL_LIST` and in the hash-bound decode report but emits no
geometry object for it. This loses no triangle or vertex data because the Xbox
slot contains none. The first maggot-room surface also retains the printable
exporter material label `material #97`; the decoder accepts only the exact
`material #<digits>` form in addition to `textures/` and `models/` paths.

These rules were exercised by the real `floor.lwo.x` and `ribcage2.lwo.x`
members from `hell1_3.gfc`, not introduced from a synthetic assumption. The
first v31 Hell 1 native load is retained as a counterexample and failed on the
empty ASE object. A complete immutable v32 rebuild omitted only those empty
objects, and all six affected maps then loaded with zero error/fatal or
missing-model line.

## 6. Xbox texture-streaming separator entities

The Xbox definition describes `info_textureseparator` as a portal-touching
entity whose activation blocks or unblocks texture streaming through that
portal for the local co-op client; its `type` spawnarg selects close or open.
This is a renderer-memory policy entity, not map geometry, visibility, collision
or progression state. The GPL PC renderer has no matching portal texture-stream
control API to call.

Deleting the entity during conversion is still incorrect because it discards
names and target-graph topology and produces a failed-spawn warning. The host
translation instead registers `idTextureSeparatorEntity` as an `idEntity`,
binds `EV_Activate`, and consumes the event as an explicit no-op. This retains
spawn identity and activation relationships while allowing the PC renderer to
use its native texture residency policy. The no-op must not be described as an
emulation of Xbox streaming behavior.

The first Dedicated Release probe was deliberately rejected: `+map` is not the
accepted dedicated-host command and logged `Unknown command 'map'` without an
entity-spawn marker. Repeating with `+spawnServer` loaded the map. Full minimized
direct-host sweeps then passed 41/41 solo and 20/20 co-op segments with zero
error/fatal line. Auditing every accepted log found no
`info_textureseparator`, `idTextureSeparatorEntity` or `Could not spawn` line,
where the preceding v30 solo logs contained 276 separator spawn failures.

