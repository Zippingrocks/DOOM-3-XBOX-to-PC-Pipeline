# Recovery order and acceptance

## Checkpoint 074 co-op loader-closure status

The current v21 tree closes all three observed co-op loader failure families.
MCU, Delta 2B part 2 and Hellhole each spawned, survived a ten-second focus
idle and recorded zero errors or fatals on the same host/DLL pair. Hellhole's
ending resources now form one 50-joint family and the four missing camera paths
are reconstructed from the exact Xbox export ranges of the shared retail take.

Static integrity is also clean: 20 direct-authored CMs, zero unresolved
class/resource/string, and a 1,015-file isolated tree with no missing companion,
duplicate declaration/material, untracked file or reparse point. All 319 tests
pass. Acceptance still requires the fresh 20-map, 60-second sweep and closure
of warned Xbox-only co-op spawnclasses; visual, progression and two-peer gates
remain open.

## Checkpoint 073 co-op loader-blocker status

Two independently reproduced co-op crash families now have source-bound fixes
and clean focused native receipts. MCU spawned and idled 10.015 seconds after
the builder began re-declaring inherited animation channels by joint name when
a derived model selects a private Xbox mesh. Delta 2B part 2 spawned and idled
10.009 seconds after replay was forced to reconstruct the private ZCT alias
from its authenticated 50-joint source family. Both runs recorded zero errors
or fatals.

Hellhole's subsequent focused load identified one final declaration collision:
stock `map_hellhole.def` inherited the private 41-joint Xbox Imp mesh while its
child `hellhole_imp` declaration retained the public 71-joint cyber-wakeup
animation. The transform and regression test are patched, but that fix is not
accepted until a rebuilt native focus run passes. All 316 offline tests pass.

This checkpoint accepts only the two clean focus results and the reproducible
diagnosis. It does not accept Hellhole, the complete 20-map route, warned
Xbox-only co-op spawnclasses, progression, networking, visual/audio fidelity or
matched original-Xbox behavior.

## Checkpoint 072 solo native-loader acceptance

The full original-Xbox solo route now passes the native loader-soak gate. All
41 segments loaded with the direct minimized source-built GPL dedicated host,
reached the spawn marker, remained alive for at least 60 seconds and recorded
zero error/fatal lines and zero premature exits. The run was one current v26
artifact and one current DLL/host pair, not a composite of earlier focused
receipts. Its minimum observed idle was 60.051 seconds.

The accepted v26 static artifacts independently close their integrity gates:
41 overlays and direct-authored CMs, zero unresolved dependency, and an
841-file isolated tree with no missing compiled companion, duplicate runtime
declaration/material, untracked file or reparse point. All 297 offline tests
pass.

This accepts solo map parsing, spawning and one-minute process survival only.
It does not accept rendering, sound, scripted progression, transitions,
save/load, encounter timing or matched original-Xbox fidelity. Co-op remains
outside this checkpoint until all 20 co-op segments pass their own 60-second
native sweep; two-peer progression/death/rejoin remains a later gate.

## Checkpoint 071 solo loader-blocker status

The twelve maps that failed the first complete solo discovery sweep now each
have a clean focused native receipt after source-bound corrections. Together
the receipts cover MCU 1/2, Alpha Labs 2 part 2, Comm Outside part 2,
Recycling 1/2, Delta 4, CPU 1, Site 3, Caverns 1/2 and Hellhole 1. Every run
reached an entity-spawn marker, survived its five-second idle, exited normally
and recorded zero error or fatal line.

The final v17 overlay and v21 isolated tree independently close their static
integrity gates, and the full 294-test suite passes. This accepts the known
loader-blocker fixes and their focused integration only. It does not promote
the 29 earlier discovery passes or the twelve focused passes into one current
all-map result. Acceptance still requires a fresh v21 41-map run with at least
60 seconds idle per map, followed by the co-op campaign run. Visual, audio,
progression, transition, save/load, two-peer and matched-Xbox fidelity gates
remain open after loader soak success.

## Checkpoint 067 native-soak runner status

The runtime gate now distinguishes the environment from the content. The
initial 31 direct invocations never initialized Doom's filesystem: every one
exited with code 4, emitted no qconsole bytes and reached no entity-spawn
marker. A Steam attempt did not create Doom while another Steam game was
active. Therefore none of those rows is admissible evidence that a campaign
map loaded, crashed or failed.

The v2 runner fails closed on that boundary, refuses to disturb another Steam
game, supports bounded and resumable batches, hashes its executable, plan and
logs, and requires both a native spawn marker and a complete 60-second idle.
Its non-game smoke test aborts after the first bootstrap failure without
attempting later maps. The 61-map tree remains unchanged and all 274 offline
tests pass.

This accepts the test instrument and classification boundary only. It accepts
zero native map loads. The next admissible gate is 61 `passed` v2 rows after
Steam is free, followed by solo progression/save-load, real two-peer co-op and
matched original-Xbox fidelity work.

## Checkpoint 066 native-test handoff status

The remaining work has crossed the offline/native boundary. Both complete
campaign routes are explicit and source-bound, terminal `endOfGame` links are
identified, dormant external exits are excluded with zero-incoming evidence,
all 61 direct map commands are recorded, and the accepted tree is staged behind
an `fs_game` alias with isolated runtime state. The tree still rehashes exactly
and all 274 offline tests pass.

This accepts only the test handoff. Next is a bounded minimized/windowed loader run
for every map, followed by solo progression/save-load, two-peer co-op
progression/death/rejoin, and matched Xbox visual/audio/timing comparison.
Those steps necessarily execute Doom and were deliberately not started while
they could interrupt the user. See `docs/NATIVE_TEST_PLAN.md` before running
them.

## Checkpoint 065 unified campaign-tree status

One local test tree now contains all 41 solo and 20 co-op map segments without
last-writer-wins ambiguity. It has an exact 1,572-file ledger, every MAP has its
PROC and CM, the three varying closure files were semantically unioned, five
identical supplemental/complete DEF overlaps were safely deduplicated, and the
independent audit finds zero duplicate runtime definition, duplicate material,
untracked file or reparse point. All 272 offline tests pass.

This is the strongest static handoff so far, but it is not native acceptance.
The engine still must parse the combined declarations, load every segment,
select its AAS data, exercise collision/portals/encounters/transitions/save-load,
and complete two-peer co-op synchronization and visual comparison. The local
retail-derived tree is not committed or redistributable. Doom 3 and `dmap` were
not launched while they could interrupt the user's game.

## Checkpoint 064 portable co-op-package status

The final 20-map co-op corpus is now materialized locally as 6,080 ordinary,
manifest-only payload files. The exact accepted generation is selected by
suffix, all copies are hash-checked, no untracked file or reparse point enters
the artifact, and its independent audit reproduces both accepted corpus
ledgers. All 259 offline tests pass.

This accepts package identity and portability, not engine or two-peer runtime
behavior. The 545,522,554-byte output is retail-derived local test data and is
deliberately excluded from Git and distribution. Native loading, collision,
visibility, encounter progression, death/respawn, networking, save/load and
visual comparison remain required. Doom 3 and `dmap` were not launched while
they could interrupt the user's game.

## Checkpoint 063 portable solo-package status

The 41-map solo corpus is now available locally as 1,792 ordinary manifest-only
payload files rather than a junction-backed development view. All source and
copied bytes were hash-checked, the independent final audit reproduces both
accepted corpus ledgers, the recursive reparse-point count is zero, and all 256
offline tests pass.

This accepts package identity and portability, not native runtime behavior.
The 782,089,007-byte output is retail-derived local test data and is deliberately
excluded from Git and distribution. Engine loading, collision/contact traces,
portal visibility, encounter timing, save/load and matched Xbox visual/gameplay
comparison remain required. Doom 3 and `dmap` were not launched while they
could interrupt the user's game.

## Checkpoint 062 complete static-matrix status

Every recovered segment appears in every applicable final offline report: 41
solo maps across 12 gates and 20 co-op maps across ten. All 692 cells pass, all
24 source reports are hash-receipted, and both global AAS corpora have their
required file counts. All 253 offline tests pass.

This closes silent static-coverage gaps, not the native acceptance boundary.
Source-authored attention records remain open observations. Engine loads,
collision/contact traces, portals and visibility, encounter timing, save/load,
two-peer synchronization and matched Xbox visual/gameplay comparison still
require execution. Doom 3 and `dmap` were not launched while they could
interrupt the user's game.

## Checkpoint 061 solo player-topology status

All 41 Xbox solo overlays now pass a manifest/source-bound player-entity gate.
Every segment has one start, all 42 teleport destinations and the one legacy
deathmatch entity are source-exact, and no player topology was lost during
conversion. All 250 offline tests pass.

This accepts preservation, not native placement. Three teleport destinations
have no exact MAP link or direct `$name` script reference and remain
source-authored attention records. Native progression and save/load must still
confirm initial placement, teleport timing/side effects and collision clearance.
Doom 3 and `dmap` were not launched while they could interrupt the user's game.

## Checkpoint 060 co-op spawn-topology status

The static two-player spawn gate is closed against conversion regression for
all 20 co-op maps. Fifty player-one/player-two placements are paired at the
same effective level, level sequences are contiguous, every map has its stock
start, every advancement target is linked, and all relevant entities are exact
to the manifest-bound decoded source. All 249 offline tests pass.

This accepts authored topology, not runtime spawn behavior. Three maps have no
safe-spawn entity and six pairs use different facing angles; both are retained
source facts. Native testing still must show actual player assignment, safe
fallback choice, teleport/target side effects, repeated spawn-level increments,
telefrag avoidance and host/client agreement. Doom 3 and `dmap` were not
launched while they could interrupt the user's game.

## Checkpoint 059 co-op resurrection status

All 20 final co-op overlays now have a focused offline resurrection topology
audit. It proves zero numbered resurrection points, zero reachable initializer,
zero active player-death source calls and zero direct startup-bytecode
call/thread entry into the shared helpers. The only two callback entities are
source-authored dormant Hell residue: one orphan relay and one relay behind a
hidden GUI with no reveal path. No map edit is justified by this evidence, and
all 246 offline tests pass.

This removes the two resurrection lookups from the port-regression question; it
does not accept death or respawn gameplay. The 32 object-thread statements are
not yet method-symbol resolved, exact XBE-string absence cannot exclude every
indirect native route, and static data cannot demonstrate spectator timing,
two-peer rejoin or spawn placement. Those are retained as focused native test
obligations. Doom 3 and `dmap` were not launched while they could interrupt the
user's game.

## Checkpoint 051 co-op entity-link status

All 4,654 named MAP link and binding spawnargs are accounted for across the
latest 20 co-op overlays. No reference that exists in a decoded Xbox source is
lost by conversion, and there are zero port-introduced unresolved links. All
225 offline tests pass.

The 667 source-authored dangling links remain attention records, not accepted
runtime behavior. Native progression must exercise target chains around split
boundaries. Site 3's case-folded `target_endlevel_1` collision specifically
requires observation at the end-level transition. Static closure cannot decide
which duplicate `FindEntity` returns or prove two-peer activation order.

## Checkpoint 050 co-op overlay corpus status

All 6,046 payloads selected by the latest 20 co-op manifests are present,
unique and byte/hash exact. Every map has direct-authored collision and zero
unresolved classname, resource or string record. The two corrected manifests
describe payload-identical overlays without duplicated direct-audio receipts.
The co-op navigation gate remains closed after rebuilding, and all 223 offline
tests pass.

One local nested TGA outside every manifest remains an explicit packaging
attention item. It is not counted as recovered content and must not enter a
distribution artifact. This checkpoint accepts the manifest-defined corpus,
not the mutable development directories as wholesale packages. Native load,
encounter and two-peer progression acceptance remain outstanding.

## Checkpoint 049 co-op AAS requirement status

The latest 20 co-op overlays now close the static navigation packaging gate:
all 638 nonempty AI requirements have the exact requested authored AAS class,
and the sole empty `use_aas` is explicit. All 30 selected navigation files pass
standard-text structure, inverse-plane and complete nonzero BSP/area coverage
checks. The two rebuilt overlays retain every earlier payload byte-for-byte.
All 220 offline tests pass.

This accepts authored navigation presence and decoded structure, not encounter
behavior. Native testing must still load all maps, exercise Guardian, Mancubus
and Cyberdemon movement, and complete two-peer spawn, death/rejoin and
progression flows. No loader or gameplay result is claimed here because Doom 3
was deliberately not launched while it could interrupt the user's session.

## Checkpoint 048 solo AAS requirement status

The solo navigation packaging gate is now closed against effective entityDef
requirements. All 1,471 nonempty AI requirements have a matching authored AAS
file; eight explicit empty values remain intentional. All 60 packaged AAS files
pass structure, inverse-plane and complete nonzero BSP/area coverage checks.
The strict-v10 overlay corpus has 1,792 payloads, zero unresolved dependency or
semantic record, and all 218 offline tests pass.

This supersedes checkpoint 047's file-presence count, which was structurally
correct for the 55 files it selected but incomplete relative to the AI
definitions. It still does not accept encounter routing: native loads must
confirm the actor bounds match each AAS settings block and exercise the five
large-actor encounters through doors, obstacles and combat movement.

## Checkpoint 047 solo AAS corpus status

All 55 packaged solo AAS files pass standard-text, plane-pair and complete
nonzero BSP/area coverage checks. Every segment has AAS48, all 14 source-shipped
AAS96 classes are present, and no file contains an unreachable nonzero node or
unreferenced nonzero area. The 215-test offline suite remains green.

This accepts decoded navigation structure, not encounter navigation. Native
progression must still observe actual AI origins, actor bounds, travel flags,
doors, dynamic obstacles and routing-cache state before any map is called
navigation-perfect.

## Checkpoint 046 in-world GUI command status

All 1,107 relevant commands emitted by 1,700 in-world GUI instances are
statically accounted for. There are zero missing GUI files, unresolved
localized script values, missing functions or source-present entity names lost
by conversion. All 215 tests pass.

The three explicit source-authored dangling activations remain focused native
observations: CPU's `com_walk1` camera-selection action and MCU's
`trigger_cranemaint` security action in both segments. Native interaction must
also confirm that the 893 bare activations drive the expected target chains;
static link closure does not prove GUI state, timing or player progression.

## Checkpoint 045 animation frame-command status

All 539 commands inside manifest-selected model declarations are statically
accounted for. Every global or namespaced frame call resolves, all 172 defined
object-method names resolve, and no trigger entity that exists in a decoded
Xbox source map is lost from its overlay. This closes the frame-command port-
regression gate with zero unresolved records and 213 passing tests.

Thirteen source/retail attention records remain: twelve split-map trigger
names absent from both source and output, plus the retail Vagary
`sonic_attack` object method absent from both PC and Xbox scripts. Native runs
must observe any animation that owns those commands, especially the Alpha Labs
3 Vagary range attack. This checkpoint does not assert that a warning or late-
bound object-call failure is behaviorally harmless.

## Checkpoint 044 reachable script-domain status

The 41-map solo corpus now has no reachable computed lookup or nonterminal
required-entity action that can address an absent entity under the proven
entrypoints, argument domains and source guards. Fifty-five formerly broad
computed-name records resolve locally, and four Monorail 2 first-half records
have fail-closed source/control/callback exclusion witnesses.

The reachability report contains 275 attention records: 175 safe null
receivers, 53 safe or script-handled null lookups, 24 receiver short-circuits,
22 nullable script arguments and one required-null call after its callback's
terminal action. There are zero unresolved records and zero potential
nonterminal thread exits. All 211 tests pass.

This accepts the offline script entity-flow gate, not native behavior. The one
terminal Comm 1 residue remains a targeted runtime observation, and all maps
still require bounded native load, progression and reference-fidelity checks
once launching Doom 3 will not interrupt the user.

## Checkpoint 043 worldspawn dispatch status

Every solo overlay now has exactly one static startup dispatch for its retail
initializer. Forty maps retain their exact worldspawn call and define no
generated global `main`; `delta4` has no worldspawn call and therefore uses the
single generated fallback. The builder rejects a mismatched or duplicate
worldspawn entrypoint instead of publishing an ambiguous overlay.

All 1,746 other payloads are byte-identical to strict v8, and the complete
strict-v9 offline gate remains closed with zero port-introduced unresolved
records. The correction removes 40 synthetic wrapper functions and call edges
from the static graph without changing its 334 source-authored attention
records. All 209 tests pass.

This is static startup-dispatch acceptance, not proof of runtime timing. The
first bounded native load of each map must confirm one initializer thread, no
duplicate startup side effects and no missing script function before focused
progression and visual testing.

## Checkpoint 042 split-script entrypoint status

All 41 solo bridges now bind the map segment to its recovered retail namespace
entrypoint. The two exceptional second halves are explicit:
`alphalabs1_2` calls `map_alphalabs1::main2()` and `monorail_2` calls
`map_monorail::main2()`. A successful compile or a global `main()` symbol is
not sufficient acceptance for segmented scripts; the bridge manifest and
semantic call graph must identify the exact entrypoint selected for that map.

Strict v8 passes the complete offline structural, resource, audio, transition,
callback, entity-link and script-entity gates with zero port-introduced
unresolved records. Its corrected call graph reaches 691 of 1,065 functions.
The 334 reachable source-authored residue uses are classified by stock VM
behavior and remain visible as attention records. They are not conversion
loss, but native activation is still required to decide whether any source
thread exit or retained no-op affects play.

This closes the known offline entrypoint defect, not solo runtime acceptance.
Each segment still needs a bounded native load/spawn, start/exit and persistent
state handoff, followed by the focused visual/gameplay pass. Do not launch the
game while it would interrupt the user's active Steam session.

## Checkpoint 041 direct script-entity status

The entity-aware script gate now includes 8,492 direct `$entityName` references
in addition to `sys.getEntity`. It resolves 7,167 to map entities and 325 to
engine entities. All 1,000 missing references are already absent from the
decoded retail source map; zero source-present entity name is lost by overlay
conversion. The combined report is clean and all 202 tests pass.

These 1,000 source-authored references must still be filtered through script
function reachability. Shared split-stage sources can retain inactive functions,
but that must be proven from entrypoints and calls rather than inferred from an
absent entity alone.

## Checkpoint 040 script entity-lookup status

All 225 solo-script `sys.getEntity` sites are parsed. Forty-four are literal;
181 computed sites are expanded through a receipt-bearing domain profile. The
profile covers 1,532 call/name references and 871 unique map/name pairs with
zero unprofiled expression and zero entity name present in decoded source but
missing from the overlay.

Twenty-two literal calls and 408 unique computed names are absent from the
decoded source as well as the overlay. Most arise from scripts shared across
split segments and conservative supersets of function arguments. They remain
open `source-authored` evidence until function reachability proves the code path
inactive or native activation confirms harmless behavior. Do not report this
checkpoint as script-runtime closure.

## Checkpoint 039 runtime-consumed entity-reference status

The solo link auditor now follows the stock PC C++ reference keys in addition
to generic targets and binds: attachments, elevator doors/status GUIs,
binary-mover buddies and state triggers, objective cameras, teleporter views,
spring endpoints, synchronized locks and ownership. The expanded corpus has
14,700 links: 13,084 local, 16 engine/empty and 1,600 matched to the retail
decoded source as dangling. Zero case-insensitive duplicates or port-introduced
unresolved links remain, and all 196 tests pass.

This closes static MAP spawnargs only. Script-computed `sys.getEntity`
expressions, animation frame-command targets and runtime-created entities remain
separate gates.

## Checkpoint 038 solo entity-link status

All 41 solo overlays pass a case-insensitive entity-name and explicit link
audit. Across 38,769 entities and 14,605 audited links there are zero duplicate
PC entity names and zero port-introduced unresolved links. The builder
deterministically disambiguates two Alpha Labs 2 vacuum-marker pairs and the
second Delta 2A exit route, preserving every entity and both exit behaviors.

The remaining 1,589 dangling links match the decoded Xbox source maps by source
entity, origin, key and target. They remain visible as `source-authored-dangling`
records and are not accepted as runtime-proven no-ops. Native load/spawn and
activation tests remain required to determine which are harmless split-map
remnants. The 195-test offline suite passes; the game was not launched.

## Checkpoint 037 solo offline status

All 41 Xbox solo segments pass structural/model closure plus the new semantic
and direct-audio gates. The campaign is one 41-map chain from `mars_city1_1` to
`hellhole_2`; all 409 active callbacks are explained; and all 3,891 active
direct-WAV references resolve through stock PC media or 419 receipt-bearing
Xbox XACT recoveries. No unresolved classname, resource, string, callback,
transition or direct-audio record remains. All 190 synthetic/authentic offline
tests pass.

The next tier is deliberately native: bounded load/spawn validation for each
segment, start/exit and save-state handoffs, then the focused visual/gameplay
run. Co-op separately retains two-peer synchronization, death/rejoin and
progression acceptance. Static closure must not be reported as proof of script
timing, audible correctness, encounters, rendering or playability.

## Checkpoint 036 solo offline status

All 41 identified Xbox single-player segments pass the structural, model and
strict overlay packaging gates. Their 1,368 manifest-listed files rehash, every
map selects direct authored collision, every recovered segmented script has a
PC global-main bridge, and the unresolved classname/resource/string totals are
zero. The final exceptional class mappings are exact and receipt-bearing; no
unknown class is hidden by a global fallback.

This makes the solo corpus ready for the next validation tier, not fidelity
accepted. Before a visual playthrough, finish the offline campaign-transition,
callback-definition and direct-audio routing audits, then perform one bounded
native load per segment without overwriting the user's active Steam session.
After loader warnings are reconciled, validate starts/exits and save-state
handoffs, then run the focused visual/gameplay pass. Co-op still additionally
requires two-peer spawn, death/rejoin and synchronized progression checks.

Do not treat the stock-PC-identical silent Mars City shutter orphan, the inert
Xbox particle remnants or absence of a loader warning as evidence of rendered
or behavioral fidelity. Those claims require native and reference observation.

## Checkpoint 024 offline preflight

`xc_delta2b_2` passes the offline structural and dependency-closure gates. MAP,
PROC, corrected AAS48 and direct 229-model CM.X decode; AAS coverage is
complete; all 343 selected model files decode; and the sole MAP callback,
`falling_floor_secret`, has exactly one recovered definition in the retail map
script. Three MAP commando entities require the Xbox-only `head_butt` animation.
The source payload is byte-identical to checkpoint 023, so its validated
50-to-63-joint retarget is reused rather than regenerated from an assumption.

All 67 direct MAP sample paths are accounted for: 63 resolve to stock PC media,
and four recover through the source-bound Xbox XACT chain. Two retail
`inner1.wav` epairs are exact stale spellings; Xbox XSND, stock PC and the same
entities' close sounds all use `inner_1.wav`. The 276-file candidate has zero
unresolved names and all 161 tests pass. This
does not yet pass the independent-dmap or native gates. PC collision-model
comparison, bounded loading/spawn, runtime sound closure, progression,
transition, two peers and Xbox-reference comparison remain open. Do not launch
the game for this checkpoint while it would interrupt another Steam session.

For the later bounded run, default medium must spawn 843/0. The only difficulty
epair is `not_hard 1` on `item_armor_security_8`, so it must remain present on
medium. Transition acceptance must drive `func_guisync_1` through
`target_endlevel_1` to `vv/xbox_coop/xc_delta4`.

## Checkpoint 023 tenth-segment status

`xc_delta2b_1` passes structural export, corrected AAS48, complete archive-local
model conversion, declaration/resource closure and the bounded loader/spawn
gate. Its decoded MAP/PROC, direct 238-model CM.X and corrected AAS48 load.
Independent PC `dmap` contains every authored collision model; its 57 additions
are exactly MAP entities marked `noclipmodel 1`. Decoded and PC-dmapped PROC
files independently agree on 70 areas, 74 portals and identical portal
geometry.

All 437 selected model files decode: 15 meshes and 422 animations. The retail
`head_butt` animation uses a 50-joint Xbox ZCT skeleton while the stock PC ZCT
mesh uses 63. The expansion retarget preserves source world-space poses for
shared joints and supplies target bind-local transforms for 13 target-only
joints. The resulting 63-joint animation loads against the stock PC mesh
without invalid-joint, AF or IK warnings.

The last bounded true-`COOP` run predates the location correction. It exits 0,
spawns 912/0, joins player 0 and has no missing model, animation, sound or image
line. Its two map-specific warnings are one causal chain: the retained
`info_locationseparator_19` origin is 51 units from the Xbox portal, outside the
engine's 16-unit search bounds, so the separator does not block location
spreading and two floor-1 locations overlap. A PC-dmapped Xbox PROC reproduces
the same warnings, excluding the PROC decoder as their cause.

The portable candidate moves only that exact separator from `1694 -608 84` to
`1694 -557 84`, the decoded and independently compiled portal plane. It has 278
file records, zero unresolved names and byte-identical payloads to the prior
absolute-path build. All 160 tests pass. Native validation of this final
candidate is intentionally deferred while another Steam game is active. A
bounded confirmation, dynamic combat/progression, transition, two peers and
Xbox-reference comparison remain open.

## Checkpoint 022 ninth-segment status

`xc_recycling2_1` passes structural export, two-class navigation, complete
model/XACT dependency closure and the bounded native loader/spawn gate. Its
MAP/PROC, corrected AAS48, corrected AAS Mancubus and direct 105-model CM.X
all load. Independent PC `dmap` contains every authored collision model; its
104 additions are exactly MAP entities marked `noclipmodel 1`.

All 341 selected model files decode. Twenty-nine warned sounds recover through
the segment INDEXLIST/XSB and original global/memory XWB banks. The 305-file
overlay has zero unresolved resources, classnames or strings, and all 156
implementation tests pass. True `COOP` spawns 880 entities, deliberately
inhibits two pickups carrying both `not_medium 1` and `not_hard 1`, and joins
the player. There are no remaining sound, navigation, joint, callback, class,
script, error or fatal failures.

Four source-authored absence notices remain explicit rather than guessed.
Stock PC Recycling 2 independently reproduces the missing
`recycwallight_broken.ase` and generated `guisurfs/hazard1:1` notices. The
shared retail `a_deldoorgutter_d02` material's exact diffuse stage is recovered
from Xbox D3TFULL. Its normal and specular stages are absent from Xbox D3TFULL
and stock PC packages. A normal rebuilt DLL, an exact art-source witness for
those two stages, dynamic combat/progression,
transition, two-peer and Xbox-reference comparison remain open.

## Checkpoint 021 eighth-segment status

`xc_enpro_2` passes structural export, complete model/XACT dependency closure
and the bounded native loader/spawn gate. MAP/PROC, corrected AAS48 and all 163
direct collision models load; PC `dmap` adds only six `noclipmodel 1` models.
All 321 selected model files and 11 source-bound XACT sounds recover. The
285-file overlay has zero unresolved names and all 156 tests pass. True `COOP`
spawns 579/0 and joins the player without a map-specific warning or missing
resource. Normal rebuilt-DLL, combat, progression, transition, two-peer and
Xbox-reference acceptance remain open.

## Checkpoint 020 seventh-segment status

`xc_enpro_1` passes structural export, complete archive-local model closure,
map-specific XACT audio recovery and the bounded native loader/spawn gate. Its
MAP/PROC, corrected AAS48 and direct 182-model CM.X export all load. Independent
PC `dmap` contains every authored collision model; its 26 additional models are
exactly MAP entities marked `noclipmodel 1`. The archive contains no AAS96.

All 315 selected model files decode. Sixteen runtime sounds recover through
the source-bound EnPro INDEXLIST/XSB/XWB chain. Exact transforms disable one
callback whose body is commented out, disable one demonstrably unshipped sound
shader, correct one retail particle extension typo, and retain the inherited
player/HUD/icon compatibility set. The 292-file overlay has zero unresolved
resources, classnames or strings, and all 156 implementation tests pass.

Under the isolated instant-hit null-guard diagnostic, true `COOP` spawns all
709 entities, inhibits none, joins the player and emits no map-specific
warning, missing-resource, invalid-joint, callback, class, path-diagnostic,
error or fatal line. This accepts seventh-segment packaging and the bounded
loader/spawn boundary only. A reviewed source guard and normal rebuild, dynamic
combat, progression, transition, two peers and Xbox-reference comparison remain
open.

## Checkpoint 019 sixth-segment status

`xc_alphalabs2_2` passes structural export, complete archive-local model closure
and the bounded native loader/spawn gate. Its MAP/PROC, corrected AAS48 and
direct 147-model CM.X export all load. Independent PC `dmap` contains every
authored collision model; its 114 additional models are exactly MAP entities
marked `noclipmodel 1`. The source archive does not contain AAS96.

All 299 selected model files decode: eight meshes and 291 animations. The
48-joint skeleton is byte-identical across three independently recovered co-op
segments. The 274-file overlay has zero unresolved resources, classnames or
string IDs, requires no new map-specific transform, and all 154 implementation
tests pass.

Under the isolated instant-hit null-guard diagnostic, true `COOP` spawns 764
entities and intentionally inhibits two player-two pickups whose retail flags
exclude medium and hard. The player joins and the log contains no map-specific
warning, missing-resource, invalid-joint, callback, class, path-diagnostic,
error or fatal line. This accepts sixth-segment packaging and the bounded
loader/spawn boundary only. A reviewed source guard and normal rebuild, dynamic
combat, progression, transition, two peers and Xbox-reference comparison remain
open.

## Checkpoint 018 fifth-segment status

`xc_mcu` passes structural export, complete archive-local MDV closure and the
bounded native loader/spawn gate. Its MAP/PROC, corrected AAS48 and direct
212-model CM.X export all load. Independent PC `dmap` contains every authored
collision model; its 16 additional models are exactly MAP entities marked
`noclipmodel 1`. The source archive does not contain AAS96.

All 410 MDV members decode. Three exact stock-AF endpoint aliases account for
terminal joints pruned from the corresponding Xbox meshes; an exact two-token
GUI correction targets the only declared locker window; one duplicate same-area
location entity becomes inert; and the exact `lights/spot08` DDS is recovered
from D3TFULL beneath the existing stock PC declaration. The 540-file overlay
has zero unresolved resources, classnames or string IDs, and all 154
implementation tests pass.

Under the isolated instant-hit null-guard diagnostic, true `COOP` spawns all
811 entities, inhibits none, joins the player and emits no map-specific warning,
missing-resource, invalid-joint, callback, class, path-diagnostic, error or
fatal line. This accepts fifth-segment packaging and the bounded loader/spawn
boundary only. A reviewed source guard and normal rebuild, dynamic combat and
progression, transition, two peers and Xbox-reference comparison remain open.

## Checkpoint 017 fourth-segment status

`xc_admin` passes structural export, dependency closure and bounded native
loader/spawn gates. Its MAP/PROC, corrected AAS48 and AAS96, and direct 199-model
CM.X export all load. Independent PC `dmap` contains every authored collision
model; its 39 additional models are exactly MAP entities marked
`noclipmodel 1`.

The map-specific 43-entry profile closes the Xbox Pinky/zjump/combo model set,
the recovered chainsaw AF and three D3T images. Evidence-bound transforms make
the orphan `func_spawner` inert, disable an absent script callback, generate the
minimum missing PC map-script entry point, remove one exporter-stale Pinky joint
epair, and disable four material stages whose images are absent from both Xbox
and PC retail data. The 322-file overlay has zero unresolved resources,
classnames or strings; all 151 implementation tests pass.

Under the isolated instant-hit null-guard diagnostic, true `COOP` spawns all
883 entities, inhibits none, joins the player and emits no missing-resource,
invalid-joint, callback, class, path-diagnostic, error or fatal line. The prone
wounded marine's one no-AAS warning is intentional retail behavior: both source
sets explicitly clear `use_aas`. This accepts fourth-segment packaging and the
loader/spawn boundary only. A reviewed source guard and normal rebuild, dynamic
combat/progression, transition, two peers and Xbox-reference comparison remain
open.

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

