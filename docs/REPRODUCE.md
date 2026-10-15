# Reproduce checkpoint 061

## Checkpoint 061: solo player-start and teleport topology

Audit all final solo player entities against the decoded MAP hash selected by
each overlay manifest:

```powershell
python tools/campaign_port/solo_spawn_topology_audit.py `
  work/solo-overlays-strict-v11 `
  --source-root work/solo-structural/maps --require-maps 41 `
  --output work/solo-overlays-strict-v11-spawn-topology-v2.json
```

Require 41 maps, 41 exact source player-entity multisets and exactly one
`info_player_start` per segment. Require 42 `info_player_teleport` records and
one Monorail 2 `info_player_deathmatch`. Of the teleport destinations, 38 must
have an incoming MAP link, one an active direct `$name` script reference and
three neither static path. The latter three must be Alpha Labs 3
`info_player_teleport_1`, Hell 1 part 3 `info_player_teleport_2` and Hellhole 2
`info_player_teleport_3`.

Do not delete or connect source-authored residue without a native witness. Run
the full suite and require 250 passing tests. Do not launch Doom 3 or `dmap`.

# Reproduce checkpoint 060

## Checkpoint 060: co-op paired spawn topology

Bind every final spawn entity to the decoded MAP named by its overlay manifest,
then audit starts, player pairs, safe points and spawn-level targets:

```powershell
python tools/campaign_port/coop_spawn_topology_audit.py ../.. `
  --source-search-root work --overlay-suffix soundguard_v3 `
  --require-maps 20 --output work/coop-spawn-topology-v3.json
```

Require 20 maps with exact source spawn-entity multisets, 20
`info_player_start` entities, 50 player-one/player-two pairs, 41 safe spawns,
22 advancement targets and 31 incoming advancement links. Each map must contain
an initial level-one pair; player levels must be paired and contiguous. Require
zero coincident pair, unlinked advancement target or port regression.

Retain the three source-authored maps without safe spawns and the six
source-authored facing-angle differences as native-test observations. Do not
create a safe point or normalize an angle merely to make the corpus uniform.
Run the full suite and require 249 passing tests. Do not launch Doom 3 or
`dmap`.

# Reproduce checkpoint 059

## Checkpoint 059: co-op resurrection topology

Extend the compiled-script statement audit to retain `OP_CALL` (96),
`OP_THREAD` (97) and `OP_OBJTHREAD` (98). Global call/thread targets use operand
A; object-thread operand B is a virtual-function immediate and must remain
explicitly unresolved unless that def grammar is decoded.

```powershell
python tools/campaign_port/xbox_script_bytecode_audit.py `
  work/decoded-inputs-all --require-maps 20 `
  --output work/coop-script-bytecode-resurrection-v2.json

python tools/campaign_port/coop_resurrection_audit.py ../.. `
  --bytecode-report work/coop-script-bytecode-resurrection-v2.json `
  --xbe work/xbe/default.xbe --overlay-suffix soundguard_v3 `
  --require-maps 20 `
  --output work/coop-resurrection-topology-v4.json
```

Require 217,103 statements, 589 calls, 51 threads and 32 explicitly unresolved
object threads. Direct call/thread targets for `Coop::initCoop`,
`Coop::resurrect_player`, `player::player1Death` and
`player::player2Death` must all be zero. The active source scan must find zero
player-death method calls and zero maps with a reachable `Coop::initCoop`.

Require zero numbered resurrection points across all 20 final maps. The only
callback entities must be Hell 1-1's orphan `trigger_relay_114` and Hell 1-2's
`trigger_relay_118`, whose sole incoming path is hidden `resurrect_gui_0` with
no reveal path. The retail XBE must match SHA-256
`a4b677f948aaabb145446946a02841568914e921eab5d6e195d944d7a23c1fb1`
and contain zero exact ASCII hits for the six reported helper/state terms.

Run the full suite and require 246 passing tests. Do not launch Doom 3 or
`dmap`; death/rejoin remains a later two-peer gameplay test.

# Reproduce checkpoint 058

## Checkpoint 058: co-op script-sound closure and stable rebuilds

Select the latest accepted 20 co-op overlays and audit active literal sound
calls against the installed stock-PC declarations:

```powershell
python tools/campaign_port/coop_script_sound_audit.py ../.. `
  --stock-dir ../../base --require-maps 20 --allow-missing `
  --output work/coop-scriptguard-script-sounds-v1.json
```

Require 40 scripts, 226 active calls, 92 unique map/event/shader records and
exactly two missing records: one `mset3_movement` and one `mset3_stop` in
`maps/vv/xbox_coop/xc_mcu.script`. Use the same authenticated Xbox XSND and
stock-PC `map_mc_underground.script` witnesses as checkpoint 057. Do not create
a third shader set.

Rebuild directly from checkpoint-055's accepted inputs, not from an
intermediate generated overlay:

```powershell
python tools/campaign_port/rebuild_latest_coop_overlays.py ../.. `
  --work-root work --input-suffix scriptguard_v2 `
  --suffix soundguard_v3 --require-maps 20 `
  --receipt work/coop-soundguard-rebuild-v3.json
```

The MCU manifest must contain
`correct-unshipped-script-sound-shaders`, count two, with source names
`mset3_movement`/`mset3_stop` and destination names
`mset2_movement`/`mset2_stop`. The Admin, Caverns 1, Caverns 2 and Site 3
manifests must each contain one `normalize-disabled-map-callback` receipt for
their exact stale `setupCoop` epair. A second compatibility-transform pass over
those single-comment lines must make no change.

Rerun the co-op overlay, entity-link, semantic, AAS-requirement, AAS-corpus,
script-entity, reachability and script-sound gates. Require 20 maps, 6,080
payloads, 545,522,554 bytes, payload ledger
`e90511d67bd1eb6ee001e21a9bef001ed833b27e523cc495561bf24c67504cad`,
4,654 links, 63 callback records, 21 transitions, 639 navigation requirements,
30 AAS files, 226 sound calls, zero missing sound declaration and zero port
regression. Run the complete suite and require 243 passing tests. Do not launch
Doom 3 or `dmap`.

# Reproduce checkpoint 057

## Checkpoint 057: solo script-sound declaration closure

Audit active script calls rather than raw strings, using the stock-PC sound
shader declaration set extracted from the installed PK4s:

```powershell
python tools/campaign_port/solo_script_sound_audit.py `
  work/solo-overlays-strict-v10 `
  --stock-dir ../../base `
  --require-maps 41 --allow-missing `
  --output work/solo-overlays-strict-v10-script-sounds-v1.json
```

The strict-v10 result must contain 126 scripts, 746 active sound references,
362 unique map/event/shader records and exactly four missing records. They are
`mset3_movement` and `mset3_stop` once each in `map_mcu_1.script` and twice
each in `map_mcu_2.script`. Verify that authenticated Xbox
`base/sound/global.xsndshd` contains `mset1` and `mset2` machinery shaders but
no `mset3`, and that stock-PC `script/map_mc_underground.script` uses `mset2`
for the identical `howitzer_3` movement and stop calls.

Rebuild MCU 1 and MCU 2 from the accepted structural, model, portable-resource,
shared-asset and recovered-XACT roots with the normal strict builder command.
Do not edit generated overlays. Require the manifest transform
`correct-unshipped-script-sound-shaders`, with two replacements for MCU 1 and
four for MCU 2, and exact input/output hashes. Reuse the other 39 strict-v10
maps byte-for-byte in the local strict-v11 audit view; packaging must copy or
dereference their payloads rather than preserve local junction metadata.

```powershell
python tools/campaign_port/solo_script_sound_audit.py `
  work/solo-overlays-strict-v11 `
  --stock-dir ../../base `
  --require-maps 41 `
  --output work/solo-overlays-strict-v11-script-sounds.json

python tools/campaign_port/solo_aas_requirement_audit.py `
  work/solo-overlays-strict-v11 --require-maps 41 `
  --stock-def-root work/shared-assets-extracted/base/def `
  --output work/solo-overlays-strict-v11-aas-requirements.json

python tools/campaign_port/aas_corpus_audit.py `
  work/solo-overlays-strict-v11 --glob "**/*.aas*" `
  --require-count 60 `
  --report work/solo-overlays-strict-v11-aas-audit.json
```

Rerun the full overlay, semantic, direct-audio, entity-link, script-entity,
script-reachability, frame-command and GUI-command gates. Require 41 maps,
1,792 files, 782,089,007 bytes, 409 callbacks, 14,700 links, 2,739 unique
direct WAV pairs, 1,479 navigation requirements, 60 AAS files and zero
unresolved record. The script-sound result has 358 unique records and zero
missing declaration. Run the full suite and require 241 passing tests. Do not
launch Doom 3 or `dmap`.

# Reproduce checkpoint 056

## Checkpoint 056: co-op callback bytecode/source boundary

Cross-check the checkpoint-055 semantic callback report against all 20 exact
co-op `.script.bin` members and their sibling `*_main.script` compilation-unit
sources:

```powershell
python tools/campaign_port/coop_script_bytecode_callbacks.py `
  work/decoded-inputs-all `
  --semantic-report work/coop-scriptguard-semantics-v2.json `
  --require-maps 20 `
  --output work/coop-script-callback-bytecode-v2.json
```

Require 4,591,834 compiled bytes, 217,103 statements, 5,239 functions, 589
`OP_CALL` instructions and statement base 4,100 in all 20 programs. Of the 63
semantic callback records, exclude the three documented retail no-ops. Require
60 functional records: six resolved in startup bytecode and 54 classified as
map-load source callbacks. There must be zero missing compilation-unit source,
duplicate compiled callback, unexpected semantic resolution or failure. The
report SHA-256 is
`8c0176a332daba448d2005b6c3a51ef8abfbfcc25a84077b6488c64a7673c50c`.
Run the full suite and require 238 passing tests. Do not launch Doom 3 or
`dmap`.

# Reproduce checkpoint 055

## Checkpoint 055: co-op script-entity reachability and Mars City 2 guard

Profile only the two source-proven dynamic domains: Alpha Labs 2 loops 1..10,
and MCU speakers 1..11/lights 1..12. Audit every direct `$entity` reference and
`sys.getEntity` call against the hash-bound decoded MAP, then compute function
reachability from `main` and MAP callback roots:

```powershell
python tools/campaign_port/coop_script_entity_audit.py ../.. `
  --source-search-root work `
  --dynamic-profile tools/campaign_port/profiles/coop_script_entity_domains.json `
  --require-maps 20 --allow-unresolved `
  --output work/coop-script-entities-v4.json

python tools/campaign_port/coop_script_reachability_audit.py ../.. `
  --source-search-root work `
  --dynamic-profile tools/campaign_port/profiles/coop_script_entity_domains.json `
  --require-maps 20 --output work/coop-script-reachability-v3.json
```

Require 216 functions, 99 reachable functions and zero port regression. The 65
attention records must be exactly 60 required-null-argument and three null-value
uses in `xc_enpro_2`, plus one reachable `RESURRECT_POINT+i` residue in each of
`xc_hell1_1` and `xc_hell1_2`.

For `maps/vv/xbox_coop/xc_mars_city2_1.script`, guard exactly the two
`sys.trigger` calls for absent `speaker_281` and `speaker_282`. Preserve
`trigger_relay_111`; its two targets are part of the decoded MAP. The transform
must accept and preserve CRLF source, reject partial/duplicate witnesses, and
record input/output hashes in the overlay manifest. Rebuild all 20 maps with
suffix `scriptguard_v2`, then rerun the checkpoint-052 corpus, entity-link and
semantic gates and the checkpoint-049 AAS gates. Require 6,080 payloads,
4,654 links, 63 callbacks, 21 transitions, 639 AI requirements, 30 AAS files
and zero unresolved port record. Run the full suite and require 236 passing
tests. Do not launch Doom 3 or `dmap`.

# Reproduce checkpoint 054

## Checkpoint 054: all solo compiled-script callbacks

Cross-check the accepted 41-map semantic report against the exact compiled
script member retained for each solo archive:

```powershell
python tools/campaign_port/solo_script_bytecode_audit.py `
  work/solo-structural/maps `
  --semantic-report work/solo-overlays-strict-v10-semantic-audit.json `
  --require-maps 41 `
  --output work/solo-script-bytecode-v1.json
```

Require 10,245,406 input bytes, 487,257 statements, 11,940 function records,
11,938 namespaced function records and 1,654 `OP_CALL` statements. All 41 maps
must infer statement base 4,100. Require 405 callback records: 403 exact
namespaced functions and two object methods resolved to compiled function-name
suffixes. There must be zero missing compiled callback and zero failure.

Rerun the 20-map co-op bytecode audit after the generic function-name extension;
its zero `initCoop` calls, zero compiled `setupCoop` functions and positive
intra-Coop call witnesses must remain unchanged. The solo and co-op report
SHA-256 values are
`3445bc0dc24510548da9a9d80221fe6453a434ec7405c4d17b9f7160afcedb7d`
and `aa9ce25b6f629a51c4c1363c2e71b4a7f8839a038494e4a23685af9995405a87`.
Run the full suite and require 235 passing tests. Do not launch Doom 3 or
`dmap`.

# Reproduce checkpoint 053

## Checkpoint 053: Xbox compiled-script function/call audit

Use the exact `.script.bin` members extracted from the 20 authenticated co-op
archives. Do not regenerate them from the accompanying source text: the purpose
of this audit is to test the shipped compiled program independently.

```powershell
python tools/campaign_port/xbox_script_bytecode_audit.py `
  work/decoded-inputs-all `
  --require-maps 20 `
  --output work/coop-script-bytecode-v1.json
```

Require 20 maps, 4,591,834 input bytes, 217,103 statement records, 5,239
namespaced function records, 589 `OP_CALL` instructions and the identical
statement-index base 4,100 in every map. Sixteen maps must contain the shared
`Coop::initCoop` definition; none may contain a compiled `::setupCoop`
function or an `OP_CALL` to `Coop::initCoop`.

Validate the decoder positively, not only by the zero result: each of those 16
maps must expose one `Coop::initCoop -> Coop::showResurrectors` call and two
`Coop::resurrect_player -> Coop::getNearestLocation` calls. The report SHA-256
is `267bcb85f423d53de142f0b62be16a6679023d7edfcb7f32788ad7088326cd9c`.
Run the full suite and require 233 passing tests. Do not launch Doom 3 or
`dmap`.

# Reproduce checkpoint 052

## Checkpoint 052: unified co-op callbacks, audio and campaign chain

First recover every raw WAV named directly by the co-op MAPs through the
matching XSND/INDEXLIST/XSB/XWB chain. The new recoveries are two files for
`xc_alphalabs2_2`, 11 for `xc_delta2b_1`, three for `xc_mars_city2_1`, one for
`xc_mars_city2_2` and five for `xc_mcu`. Use `xact_audio.py` with the exact
authenticated retail-image extents; never substitute a PC sample. The five
XACT manifests must hash to the values in checkpoint-052 evidence.

Add `script/coop.script` to the shared player resource profile and prepend an
include to every co-op map script exactly once. Apply only the path-scoped MAP
callback corrections recorded in the receipt. In Site 3, preserve the
referenced `target_endlevel_1` and rename only the unreferenced case-fold
duplicate to `target_endLevel_1_solo_orphan`. A rebuilt manifest must carry
`source_map_sha256` from the original decoded MAP; it must not treat a prior
transformed overlay as new source provenance.

Rebuild the latest candidate for all 20 maps, then run the full offline gates:

```powershell
python tools/campaign_port/rebuild_latest_coop_overlays.py ../.. `
  --work-root work --suffix callback_v1 --require-maps 20 `
  --receipt work/coop-callback-rebuild-v1.json

python tools/campaign_port/coop_overlay_corpus_audit.py ../.. `
  --require-maps 20 --output work/coop-callback-overlay-corpus-v1.json

python tools/campaign_port/coop_entity_link_audit.py ../.. `
  --source-search-root work --require-maps 20 `
  --output work/coop-callback-entity-links-v1.json

python tools/campaign_port/coop_semantic_audit.py ../.. `
  --stock-script-root work/pc-stock-scripts `
  --language work/shared-assets-extracted/base/strings/english.lang `
  --language work/shared-assets-extracted/base/strings/english_vv.lang `
  --require-maps 20 --output work/coop-callback-semantics-v1.json
```

Require 6,080 payloads totaling 545,522,466 bytes, no untracked or unresolved
payload, 63 callback records (51 global, nine namespaced and three exact retail
no-ops), 21 transition records, a single closed 20-map chain and zero entity
name duplicates. Rerun the checkpoint-049 AAS gates and require the unchanged
639 requirements and 30-file canonical corpus. Run the full suite; 231 tests
must pass. Do not launch Doom 3 or `dmap`.

# Reproduce checkpoint 051

## Checkpoint 051: co-op named entity links

Bind each latest overlay to its decoded source MAP using the map transform's
`input_sha256`; when no MAP transform exists, use manifest `map_sha256`.
Require an exact match under the retained work tree, then audit case-insensitive
named entity references:

```powershell
python tools/campaign_port/coop_entity_link_audit.py ../.. `
  --source-search-root work `
  --require-maps 20 `
  --output work/coop-latest-entity-links-v2.json
```

Require 20 maps, 15,703 entities, 15,682 unique case-folded names and 4,654
links. Statuses must be 3,985 local named entities, two engine/empty values and
667 hash-matched source-authored dangling links, with zero port-introduced
unresolved record. Preserve and report the two Site 3 spellings
`target_endlevel_1` and `target_endLevel_1` as one source-authored case-fold
collision. The report SHA-256 is
`e8dc24fb63e6161cbf253129429d3e9a1218f270bef7f43e339a5c8eb1c83224`.

Run the full suite; 225 tests must pass. Do not launch Doom 3 or `dmap`.

# Reproduce checkpoint 050

## Checkpoint 050: latest co-op overlay receipt closure

When a raw WAV named by the MAP is also present in an explicit runtime resource
profile, copy it once through the runtime closure. The later direct-audio scan
must detect the staged file and emit neither a second copy nor a second
manifest record. Rebuild `xc_hell1_2` and `xc_hellhole_1`; excluding manifests,
require zero added, changed or removed payloads relative to checkpoint 049.

Rehash the latest candidate for every co-op map:

```powershell
python tools/campaign_port/coop_overlay_corpus_audit.py ../.. `
  --require-maps 20 `
  --output work/coop-latest-overlay-corpus.json
```

Require 20 maps, 6,046 unique manifest paths, 535,777,192 payload bytes, 20
direct-authored CM sources and zero unresolved classname, resource or string
records. The manifest and payload ledgers must be
`8431faf7c4899931e6769f471210083d30c462b38ac233929a97977292bfa6ec`
and `7d063f648981d6aedfa598452582e9f87d606471fef803eacf7946f05351fd24`.

Top-level `config.spec` and `DoomConfig.cfg` are engine-local state, not overlay
payloads. Record any other untracked file. The current local tree has one:
`xbox_coop_port_test_v6/maps/vv/xbox_coop/xc_mars_city1_1/textures/objective2.tga`.
It is not a manifest payload and its nested path cannot satisfy the root
`textures/objective2` reference; exclude it from packaging and do not silently
claim or delete it.

Rerun the checkpoint-049 requirement and structural audits. Require the same
639 requirement statuses and 30 AAS topology totals; the canonical, candidate-
directory-independent AAS ledger must be
`e3877076cf1952a8150d6e5d1471615419476484aaf836a09bc16e74dfe98c08`.
Run the full suite; 223 tests must pass. Do not launch Doom 3 or `dmap`.

# Reproduce checkpoint 049

## Checkpoint 049: entityDef-driven co-op AAS closure

Extract these exact shared-archive members and decode them into the existing
segment workspaces while preserving their class suffix:

```text
base/xbox_gen/maps/vv/xbox_coop/xc_hell1_2.aas_guardian.x
base/xbox_gen/maps/vv/xbox_coop/xc_hell1_2.aas_mancubus.x
base/xbox_gen/maps/vv/xbox_coop/xc_hellhole_1.aas_cyberdemon.x
```

Rebuild `xc_hell1_2` and `xc_hellhole_1` with the same runtime class, resource,
material and `#str_07595` roots as their accepted offline overlays. Excluding
the manifest, require zero changed or removed payloads. The former must add
only Guardian and Mancubus AAS; the latter must add only Cyberdemon AAS.

Audit the latest overlay selected for each co-op map:

```powershell
python tools/campaign_port/coop_aas_requirement_audit.py ../.. `
  --require-maps 20 `
  --stock-def-root work/shared-assets-extracted/base/def `
  --output work/coop-latest-aas-requirements-v2.json

python tools/campaign_port/coop_aas_corpus_audit.py ../.. `
  --require-maps 20 `
  --require-count 30 `
  --output work/coop-latest-aas-corpus.json
```

Require 639 AI requirements: 638 `packaged`, one `explicit-no-aas`, and zero
missing. Require 30 navigation files: 20 AAS48, six AAS96, two Mancubus, one
Guardian and one Cyberdemon. Totals must be 20,770,442 bytes, 22,348 areas,
101,654 reachabilities, 79,281 nodes and 23,731 inverse plane pairs. Every file
must have zero unreachable nonzero nodes and zero unreferenced nonzero areas.

Run `python -m unittest discover -s tools/campaign_port/tests -p 'test_*.py'`;
220 tests must pass. Do not launch Doom 3 or `dmap` for this checkpoint.

# Reproduce checkpoint 048

## Checkpoint 048: entityDef-driven solo AAS closure

Extract the five special navigation files from the authenticated shared
`assets.gfc`/`assets.gob` pair. Match these exact members:

```text
base/xbox_gen/maps/vv/cpu_2.aas_sabaoth.x
base/xbox_gen/maps/vv/hell1_2.aas_mancubus.x
base/xbox_gen/maps/vv/hell1_3.aas_guardian.x
base/xbox_gen/maps/vv/hellhole_1.aas_cyberdemon.x
base/xbox_gen/maps/vv/recycling2_2.aas_mancubus.x
```

Decode each with `decode_aas_x.py` into its segment's decoded `maps/vv`
directory, preserving the class suffix. Rebuild all 41 overlays as strict v10.
Compare strict v9 and v10 after excluding manifests: require zero changed,
zero removed, and exactly the five files above as additions.

Audit packaged requirements and every AAS class:

```powershell
python tools/campaign_port/solo_aas_requirement_audit.py `
  work/solo-overlays-strict-v10 `
  --require-maps 41 `
  --stock-def-root work/shared-assets-extracted/base/def `
  --output work/solo-overlays-strict-v10-aas-requirements.json

python tools/campaign_port/aas_corpus_audit.py `
  work/solo-overlays-strict-v10 `
  --glob "**/*.aas*" `
  --require-count 60 `
  --report work/solo-overlays-strict-v10-aas-audit.json
```

Require 1,479 AI requirements: 1,471 `packaged`, eight `explicit-no-aas`, and
zero missing. Require 60 AAS files: 41 AAS48, 14 AAS96, two AAS Mancubus, and
one each for Guardian, Sabaoth and Cyberdemon. Totals must be 45,328,253 bytes,
47,352 areas, 230,620 reachabilities, 163,804 nodes and 51,727 inverse plane
pairs, with zero uncovered nonzero node or area.

Run the structural, semantic, audio, entity-link, script-entity,
language-aware script-reachability, frame-command and GUI-command audits on
strict v10. Require zero unresolved records and the established attention
counts. Run `python -m unittest discover -s tools/campaign_port/tests -q` from
the campaign-port-dev root; 218 tests must pass. Do not launch Doom 3 or
`dmap` for this checkpoint.

# Reproduce checkpoint 047

## Checkpoint 047: complete solo AAS corpus

Audit every packaged navigation file in strict v9:

```powershell
python tools/campaign_port/aas_corpus_audit.py `
  work/solo-overlays-strict-v9 `
  --glob "*.aas*" `
  --require-count 55 `
  --report work/solo-overlays-strict-v9-aas-audit.json
```

Require 55 files: 41 `.aas48` and 14 `.aas96`. Totals must be 44,109,766
bytes, 45,857 areas, 226,989 reachabilities, 158,002 nodes and 49,217 inverse
plane pairs. Every file must report zero unreachable nonzero nodes and zero
unreferenced nonzero areas. The content corpus ledger, report and auditor
SHA-256 values are:

```text
db57a26fd0228cfad527db122e7e3c43e4df3d090b29ebb4d42b48725c47d18d
8401b49cd8d03eded2b534208564b44fcefa484c73ec7bb3f3c3e29031b10dbc
3ad963e687585933f676a58d8f1c74e29f1d81f525f0616d306c0867ac15ebc0
```

Run the full 215-test offline suite. Do not launch Doom 3 or `dmap` for this
checkpoint.

# Reproduce checkpoint 046

## Checkpoint 046: in-world GUI command targets

Audit each MAP `gui*` instance against overlay files, the installed PK4 view,
the stock/map script corpus and the English language table:

```powershell
python tools/campaign_port/solo_gui_command_audit.py `
  work/solo-overlays-strict-v9 `
  --source-root work/solo-structural/maps `
  --stock-script-root work/pc-stock-scripts/script `
  --stock-base ..\..\base `
  --stock-language work/shared-assets-extracted/base/strings/english.lang `
  --out work/solo-overlays-strict-v9-gui-commands.json
```

Require 41 maps, 1,700 GUI instances and 1,107 relevant commands. Status
counts must be 893 `implicit-entity-targets`, 63 `named-entity`, 128
`namespaced-function`, 20 `empty-gui-script-parm` and three
`source-authored-dangling`. Require three attention and zero unresolved
records. The report, auditor and language-table SHA-256 values are:

```text
e114b4224cdbebe9881b74f56db9fb2a0eff8cb66ce5887a396fe53ba0283b7c
d79a68c9fa5e27af43469b1f7ec95311604635714938e40e918221e91232a012
738dd6f4f8707bd72a7b954d73d9cb6e5bbbd4ddf7da4e84688e71f2bc8ab635
```

Run `python -m unittest discover -s tools/campaign_port/tests -q`; 215 tests
must pass. Do not launch Doom 3 or `dmap` for this offline checkpoint.

# Reproduce checkpoint 045

## Checkpoint 045: selected animation frame commands

Run the frame-command auditor with the strict-v9 overlays, decoded Xbox source
MAPs and complete stock PC script corpus:

```powershell
python tools/campaign_port/solo_frame_command_audit.py `
  work/solo-overlays-strict-v9 `
  --source-root work/solo-structural/maps `
  --stock-script-root work/pc-stock-scripts/script `
  --out work/solo-overlays-strict-v9-frame-commands.json
```

Require 41 maps and 539 commands. Status counts must be 330 global functions,
one namespaced function, 172 object-method names, 23 named entities, twelve
source-authored dangling triggers and one retail-shipped missing object method.
There must be 13 attention records and zero unresolved records. The auditor
must scope commands to manifest-selected model declarations; it must not count
unselected blocks merely because their DEF file was copied.

The report and auditor SHA-256 values are
`91327d90b187c3ce1dff4d68b840897da2ad35c55f262a6c9dcb337774806dbf`
and
`d38c5119c9a9395afb6798cd805f80d9b587755a62dd639397fff4e467c2aca1`.
Run `python -m unittest discover -s tools/campaign_port/tests -q`; 213 tests
must pass. Do not launch Doom 3 or `dmap` for this offline checkpoint.

# Reproduce checkpoint 044

## Checkpoint 044: reachable script entity domains

Run the reachability classifier over the unchanged strict-v9 overlays with the
decoded retail MAP/script source and the current domain profile:

```powershell
python tools/campaign_port/solo_script_reachability.py `
  work/solo-overlays-strict-v9 `
  --source-root work/solo-structural/maps `
  --dynamic-profile tools/campaign_port/profiles/solo_script_entity_domains.json `
  --out work/solo-overlays-strict-v9-script-reachability.json
```

Require 1,025 functions, 524 edges, 652 reachable functions and 373
unreachable functions. Residue counts must be 55 `reachable-profile-local`,
275 `reachable-source-residue`, four `source-control-flow-excluded` and 803
`unreachable-source-residue`, with zero unresolved records. The 275 attention
effects must split 175/53/24/22/1 across safe-null-receiver,
safe-or-script-handled-null-lookup, safe-null-receiver-short-circuit,
nullable-script-argument and source-thread-exit-after-terminal-action.

The domain profile and reachability-report SHA-256 values are
`28a6489bed4dd405bfa73b1fba35b02fc6420bbe918ad6716d99a36784cbd1b1`
and
`cd0e55db9f7a6e5c6f9b74e73a7a6fc871dd8d939328813da7167166fda1af50`.
Run `python -m unittest discover -s tools/campaign_port/tests -q`; 211 tests
must pass. Do not launch Doom 3 or `dmap` for this offline checkpoint.

# Reproduce checkpoint 043

## Checkpoint 043: preserve retail worldspawn dispatch

Read `idWorldspawn::Spawn` in the official GPL `neo/game/WorldSpawn.cpp`.
Confirm that it schedules global `main` after compiling the map script and then
separately schedules every worldspawn `call*` spawnarg. Audit all 41 decoded
solo MAPs against the selected namespace entrypoint. Require 40 exact retail
worldspawn dispatches and one no-call fallback, `delta4`.

Rebuild all maps with the current `build_runtime_overlay.py`. For a matching
worldspawn call, the generated `maps/vv/<segment>.script` must include the
recovered map sources but must not define global `main`. Its transform receipt
must say `dispatch: retail-worldspawn-call`. For `delta4`, require
`dispatch: generated-global-main-fallback` and a single call to
`map_alphalabs4::main()`. A mismatched or duplicate worldspawn symbol must fail
closed and publish no overlay.

Compare strict v8 with strict v9. Require 1,746 non-bridge, non-manifest files
to be byte-identical. The only changed paths are all 41 generated bridge
scripts and all 41 manifests. The strict-v9 corpus must contain 41 maps, 1,787
payload records and 780,870,520 bytes, with manifest ledger
`134b0a271500d33ddf1d4899f89e3f0a9c82e00656ae2f444bcb2700c45ebcad`
and payload ledger
`4685bc5ba9db10677c73f6d5f5bec6673806713e9ef1f67195541e735d65b669`.

Run the corpus, semantic, direct-audio, entity-link, script-entity and
reachability audits. Their local report SHA-256 values, in that order, are:

```text
3caec1110f2e4f06bff12be979538948e33890492dbfce7b7502bf685485720a
1bc49f618584a7d6387b408830d0df68abfdea3e2d366cb473a39e3b30d7acec
0fa2da790dd199d7e66727a2f857ce09e3093ff6beb4776253cafee89247f586
761f83be009c146c5166a409355b0fb7238ab92a69da8ea75d97716412d5bff7
a390290988ae752af82d9412773542fb67d0e58f4bf4bc83db91a6d675c0817f
8190c68b67338a99bb749b04cbc42de9840303488b44725c80fd0f4ce9fee8da
```

Require zero unresolved records in all six reports. The reachability report
must contain 1,025 functions, 524 edges, 652 reachable functions, 373
unreachable functions and 334 attention records. Run
`python -m unittest discover -s tools/campaign_port/tests -q`; 209 tests must
pass. Do not launch Doom 3 or `dmap` for this offline checkpoint.

## Reproduce checkpoint 042

## Checkpoint 042: exact split-map script entrypoints

Rebuild all 41 checkpoint-041 overlays with the current
`build_runtime_overlay.py`. The builder's exact path map must select `main2`
for only these two sources:

```text
maps/vv/alphalabs1_2.map -> map_alphalabs1::main2()
maps/vv/monorail_2.map   -> map_monorail::main2()
```

Require each recovered source to define the selected function before the
builder publishes an output. The generated bridge SHA-256 values are
`6416d0c1379dcff81e37100424ec2a247bc5c2e7e4a72d6b2cf29d3b37f75e26`
and
`1d335185720d69761f42931b796e364e577bb81b653afd9b4947583a2418402f`.
Their manifest SHA-256 values are
`11f3b134b17c51e6466547ac4db3aecd62ab33c9566adb7353027a24ab2a9867`
and
`5c32f1394621d1cab6dea5e01e84a6fc60ecbc4482ae9271f4242b34e4bcd641`.
Compare strict v7 and v8 and require exactly these two scripts plus their two
manifests to differ; the other 1,824 files must be byte-identical.

Run the corpus, semantic, direct-audio, entity-link, script-entity and script-
reachability auditors over `solo-overlays-strict-v8`. Require 41 maps, 1,787
payload files, 780,869,120 bytes, 409 explained callbacks, a closed 41-map
transition chain, 3,891 direct WAV references, 14,700 static entity links,
8,492 direct script entity references, 225 `sys.getEntity` sites and zero
unresolved records in every report. The manifest and payload ledgers are
`e1758426df1188d9a9ee170bf72ca92e68304a10575da729d19a6aca3ed7fc6a`
and
`39b679d89c549a2fa96475edc7adbbcaa1694ea593c831b9f155bf28bb18040f`.

The six local audit report SHA-256 values, in the order above, are:

```text
3f7e8fa5cb342010890fd059d9a1881dcd0e0fe2cb56c4315a42738b912ed83d
38f700d31085c9f80eb0eeeee5bec97f4f6b2362b134a2daa3a1018f8d485677
eaad020d6283d95d77864bb61f8f6488ea5d7bc607131019fdab772473259b0a
d49234518ee7c544530171ac0540a1b94354b5097beb34fd9ff4e071a6b3e1f6
5702326d8b77c5769dfc9378c2056f8205ecff9435f4e6bc1c098ba97a50fe63
39c9688169c06c55e5debcfa457449487bcb39ae5b4951eb989e170a4e729872
```

The reachability report must contain 1,065 functions, 564 edges, 691 reachable
functions, 374 unreachable functions, 334 attention records and zero
unresolved records. Run
`python -m unittest discover -s tools/campaign_port/tests -q`; 208 tests must
pass. Do not launch Doom 3 or `dmap` for this offline checkpoint.

## Reproduce checkpoint 041

## Checkpoint 041: direct script entity names

Run the checkpoint-040 command with the current auditor. It additionally scans
direct `$entityName` references after neutralizing comments and string literals.
Require 8,492 references, 2,627 unique map/name pairs, 7,167 local entity
references, 325 engine references, 1,000 source-authored missing references and
zero unresolved records. The combined report SHA-256 is
`b62de2eadca76959a9a3966db09e41a8c0fd0f66b1dcbf1ac2411f05505c4da3`.
Run all 202 tests. Do not launch Doom 3.

## Reproduce checkpoint 040

## Checkpoint 040: script-computed entity names

Audit all recovered scripts with the source-bound dynamic domain profile:

```powershell
python tools/campaign_port/solo_script_entity_audit.py `
  game/campaign_port_work/solo-overlays-strict-v7 `
  --source-root game/campaign_port_work/solo-structural/maps `
  --dynamic-profile tools/campaign_port/profiles/solo_script_entity_domains.json `
  --out game/campaign_port_work/solo-overlays-strict-v7-script-entity-profiled.json
```

Require 225 calls, zero unprofiled expressions and zero unresolved records.
The profile must expand to 1,532 references and 871 unique map/name pairs. The
profile and report SHA-256 values are
`82643edcfc4316441054ed4045b738cd4a1ed9806b7c3625aba7ae8295d71893`
and `d08553215a984386187b01e1d5e015b5ca922e9b9bbf57889ff93ec2710d9ee3`.
Do not remove the 22 source-authored literal or 408 unique computed missing
names merely to reduce counts. Run all 201 tests. Do not launch Doom 3.

## Reproduce checkpoint 039

## Checkpoint 039: runtime-consumed static entity references

Run the checkpoint-038 entity-link command with the current auditor. Its key
set is derived from `FindEntity`, `GetTargets` and related consumers in the
official stock PC game source. Require 14,700 links: 13,084 `named-entity`, 16
`engine-or-empty`, 1,600 `source-authored-dangling`, zero duplicate names and
zero unresolved records. The report SHA-256 is
`148912f45e6ad07142f93a87053215d35cba8c6587a07010b4e4d521f0588fb0`.
Run the full offline suite; 196 tests must pass. Do not launch Doom 3.

## Reproduce checkpoint 038

## Checkpoint 038: solo PC entity names and links

Rebuild all 41 overlays from checkpoint 037 inputs with the current
`build_runtime_overlay.py`. Do not patch generated MAPs manually. Then compare
explicit links to the decoded retail source maps:

```powershell
python tools/campaign_port/solo_entity_link_audit.py `
  game/campaign_port_work/solo-overlays-strict-v7 `
  --source-root game/campaign_port_work/solo-structural/maps `
  --out game/campaign_port_work/solo-overlays-strict-v7-entity-links.json
```

Require 41 maps, 38,769 entities, 14,605 links, zero case-insensitive duplicate
names and zero unresolved records. The 1,589 `source-authored-dangling` records
must match decoded retail source by entity, origin, key and target; never erase
or retarget them merely to make the count zero. Re-run the corpus, semantic and
audio audits and require their unresolved counts to remain zero.

The entity-link, corpus, semantic and audio audit JSON SHA-256 values are
`c3d91ee9e8f1007a6b292f793b86972437cc0ba938a9fd4f151e7aef1478aa4e`,
`787f4567da16d996e7e584ec6cd1badfdb6b414e8ae0d4ff6296fef90fbe940b`,
`dfd25517392c763e038669ffd77a79f852f1f75675d756d824316ced6a377a32`
and `38f577161953ec638e74dd3e3554132c0bb321ea60e2350d684af865915b538e`.
The manifest and payload ledgers are
`d13ad69fcba8028c7b894d588ef023e9b3e7ca86ac2a807c27dcb8c1e906e658`
and `91158d62dcd37ae0704c90397f6fb878244a51d8eb103aa18c045ddf5c0ce105`.
Run the full suite; 195 tests must pass. Do not launch Doom 3 for this offline
checkpoint.

## Checkpoint 037: solo semantics and direct audio

Start from checkpoint 036's 41 decoded solo trees. Extract every
`./base/sound/*.indexlist` member from the source-bound `assets.gfc`/`assets.gob`
pair and every `base/soundbanks/*.xsb` member from the authenticated retail ISO.
Use the ISO inventory's bounded global XWB extent; never infer an unbounded bank
from the whole disc.

Run the entity-aware campaign audit against the strict overlays, the extracted
stock PC script corpus and both recovered English catalogs:

```powershell
python tools/campaign_port/solo_semantic_audit.py `
  game/campaign_port_work/solo-overlays-strict-v6 `
  --stock-script-root game/campaign_port_work/pc-stock-scripts `
  --language game/campaign_port_work/shared-assets/base/strings/english.lang `
  --language game/campaign_port_work/shared-assets/base/strings/english_vv.lang `
  --out game/campaign_port_work/solo-overlays-strict-v6-semantic-audit.json
```

Require one start (`mars_city1_1`), one terminal (`hellhole_2`), a 41-map walk,
409 explained calls and zero unresolved records. Audit direct samples against
stock PC media and the Xbox XSND/INDEXLIST/XSB chain. Recover only records
classified `xact-recoverable`, then add that map's new recovery directory as a
retail root when rebuilding its overlay. The builder copies and receipts every
non-stock direct WAV; it fails closed if one is missing.

Re-run `overlay_corpus_audit.py`, `solo_semantic_audit.py` and
`solo_audio_audit.py` on the rebuilt corpus. Checkpoint 037 requires:

- 41 maps, 1,787 payload files and 780,869,086 payload bytes;
- manifest ledger `a99b35fe5bfbf85c5a617be76f38082e752748f7489b5a7d3c9562d7df44cdf3`;
- payload ledger `d6756e9cf3a40cb4c934ab2efbe3a33538f6f492ed942934f7583bbc335bc22b`;
- 409 explained callbacks and a closed 41-map chain;
- 2,320 stock-PC direct-audio pairs and 419 overlay-recovered pairs; and
- zero unresolved class/resource/string, callback, transition or audio record.

The local corpus, semantic and audio audit JSON files hash to
`d9ba1dcdb6097dd0489ceebf3e3897a76e71bdf848fe5038e1aa68c97acc425d`,
`95fb2f4023834fd843d882e6b81c0d96894b59ad3707f0c16f71ce654fee4982`
and `274c3e9fdb5509faefd8faca08a168bf118a0a7b6b79e395c569f140415572a0`.
The XACT corpus receipt hashes to
`0f1cd3113da64d491c14827653d4f8b6e04b1045a3e70e6860cc927754d73082`.
Run `python -m unittest discover -s tools/campaign_port/tests -q`; 190 tests
must pass. Do not launch Doom 3 for this offline checkpoint.

## Checkpoint 036: strict solo overlay corpus

Begin with the checkpoint-034 decoded structural tree and checkpoint-035 model
tree. For each of the 41 segment names, call `build_runtime_overlay.py` with:

- `--map` and `--converted-dir` pointing at that segment's decoded
  `maps/vv` directory;
- retail roots for its decoded models and recovered portable resources,
  followed by the shared player, NPC, HUD, material and shared-asset roots;
- the shared retail DEF directory, stock PC `base`, both recovered English
  language files, and `--def-preference info.def`;
- `--authored-cm` pointing at the direct decoded `<segment>.cm`; and
- a new, empty output directory. Do not use `--allow-unresolved`.

The builder is fail-closed and never overwrites an output. Require every
`xbox-solo-overlay-manifest.json` to identify
`doom3-xbox-solo-runtime-overlay`, the expected `maps/vv/<segment>.map`,
`collision_source: direct-authored-cm`, and three empty unresolved arrays.

Then rehash the complete corpus:

```powershell
python tools/campaign_port/overlay_corpus_audit.py `
  game/campaign_port_work/solo-overlays-strict `
  --expected-root game/campaign_port_work/solo-structural/maps `
  --out game/campaign_port_work/solo-overlays-strict-audit.json
```

The 2026-10-14 receipt requires 41 maps, 1,368 payload records and 609,521,747
payload bytes; 41 direct-authored collision selections; zero unresolved
classnames, resources and strings; manifest ledger
`b245c39835c7c50a1003f45cec924a6ee244db9a933f45a392e03a43d906bfa7`;
and file ledger
`ac3b51ec34123b92a5cc4997b50189b7f6b107e3613df390b5579a372eeff508`.
The local audit JSON hashes to
`6735231a5c30b07f3fe639ba1779af2d18ee628e736d3ffd664c862f653cd584`.
Run the complete Python suite from the tool repository root; checkpoint 036 is
173 passing tests. Do not launch Doom 3 as part of this offline recipe.

## Source and boundary

Implementation repository: `Zippingrocks/doom3-gpl-xbox-reconstruction`.
Use the open campaign-port pull request through an authenticated clone. Preserve
existing work; use an isolated worktree if the checkout is dirty.

Python 3.10+ and the standard library are sufficient. Checkpoint 014 used Python 3.11/Windows:

```powershell
python -m unittest discover -s tools/campaign_port/tests -v
```

Expected result on the current implementation branch: 161 tests, zero failures.
Checkpoint 012 captured 142 passing tests; later synthetic tests cover authored-
CM overlay selection, identity rejection, path-independent material receipts,
the exact unshipped armor-shard map-icon transform, `xc_admin` inert orphan and
script handling, stale Pinky joint removal, absent material-stage handling,
path-scoped AF endpoint aliases, the MCU security-GUI correction and the exact
duplicate-location witness.
Fixtures contain no retail game data.
Tests establish decoder contracts, not campaign fidelity.

### Campaign-wide co-op overlay integrity gate

Before executable testing, select the newest manifest for each of the 20
`maps/vv/xbox_coop/*.map` overlays. Recompute SHA-256 for every path in each
manifest's `files` array and require exact equality. Require zero missing files,
zero hash mismatches, zero unresolved class/resource/string names, and
`collision_source` equal to `direct-authored-cm` for every map. The 2026-10-14
offline gate hashed 5,878 records and passed 20/20 overlays. This proves the
portable inputs are internally intact; it does not replace native loading,
progression, two-peer, or visual acceptance.

### Xbox single-player structural gate

Select the 41 root-level retail single-player GFC/GOB pairs, excluding `xc_*`,
`d3dm*`, `assets*`, and `pda_vv`. For every pair, require exactly one MAP.X,
one PROC.X, one CM.X and at least one AAS.X below
`base/xbox_gen/maps/vv/`. Decode MAP and compute its geometry CRC with
`map_geometry_crc.py` before decoding CM with that exact CRC. Decode every AAS
class rather than assuming only `aas48` exists, and retain both the namespaced
main script and map script when present.

Rehash every core extraction-manifest record and every decoder output against
its report. Require zero missing files, zero hash mismatches, and exact equality
between every CM report's `map_crc` and its MAP geometry report. The 2026-10-14
pass covered 41 maps, 296 core records and 178 decoded outputs (594,563,894
bytes), with all three failure counts at zero. This is a structural gate only;
it precedes model, resource, XACT, script and runtime closure.

### Checkpoint 029 Site 3 part 1 offline preflight

Require MAP SHA `7957749b59ae1148ffd7b85c603cb0d634d23af71f3010427112981aed8a8471`
at CRC `2465825243`, PROC SHA
`354dae29d332bbbd0122fb8c1410125588f2ab9a70d083960db7998ae57ca8da`,
AAS48/AAS96 hashes `8780818474f02829dcc806ce6af1925c45a4e25fe1f64255579c57e569c5efcb`
and `77bd276b549ff80fb5f2648e30b039939d27d44837c48918165ee57fec18722c`,
and authored CM SHA
`b39d942e1dcc955c9a4f0bf0cf95a4b2020db86ee167365ccfe989a372ebc7b0`.
Decode all 345 models and recover 13 of 65 direct samples. The final manifest
hash is `425362631e431c73cb6b613a4653217d24ddbd21241eb27974ce11dd19d33ac0`.
Preserve both end-level values for runtime route auditing; do not guess which
one fires from static proximity alone.

### Checkpoint 028 Delta 5 part 1 offline preflight

Require MAP SHA-256
`7cc1a8ba5aedf3e22bebdad9f8584ae3389ef89e4414c70ad2d9df32f0958168`
at CRC `1946210965`, PROC SHA-256
`79293c5b1efae29d82535516e5d34e411b9d6a1a92729cd011cbead20b15fb66`,
AAS48 SHA-256
`994b51b9043f9da3453cd365e37c1f03223f5cc53fea99dbc925c7ae674ea208`
and authored CM SHA-256
`7a6b55c9996361b1fbe7040eb2ad6b6b5732709ad4b53ac394ee59924cd689c1`.
Decode all 333 models. Recover 12 of 63 direct samples through INDEXLIST SHA
`6ab704154fd87b04cc26acc25b777fc530ea2970c4776ff71a4f5e4f82c60d2b`
and XSB SHA `80d7a3157defdf54213d14fa445dc373999c93fd5e2016e39887165e8568c43d`.
Generate the receipt-bearing empty map script only after proving the retail GFC
has `_main.script` plus its compiled binary but no `xc_delta5_1.script` member.
The final manifest hashes to
`92c5cb19e355d2e024e8ba4680b01133d3e43d2fd53b80f8b6d2f708aeb2c6f6`
with zero unresolved names. Expect 893/1 on medium and preserve the Site 3
transition.

### Checkpoint 027 Hell 1 part 2 offline preflight

Require decoded `xc_hell1_2` MAP SHA-256
`4f80f6508af50fa8198ffcb55c9f5d14bd37dd51cf40f5e991f363e1b2b9a2c4`
at CRC `3647446564`, PROC SHA-256
`02a47cda1d04c9a29f798231f99861284f9b0ea14d5d23daa31562ce3652760d`,
AAS48 SHA-256
`3109cb83e9c573f5152286b2852578d3835e36f0dff1ec327c54bfc4594047fd`
and authored CM SHA-256
`65fc159cc7be4e0231a06c8382db1c6563497731f5fc0cab52ef4e59d279aaf8`.
Decode all 301 model members. Recover the 15 of 40 direct MAP samples absent
from stock through INDEXLIST SHA-256
`0aeeccc057d53de1222d3e844236a95d449647e63cf4562e789756f0f941539f`
and XSB SHA-256
`cc6f0a6a83fbc62ec1a88241a09e55acf8ffb5a3c7cae7e00a8062ed9f479f80`;
the WAV corpus totals 9,239,110 bytes. The final 148,075-byte overlay manifest
hashes to `14d9052092f3129868831e9d32e2c0f32d8c48ea9c10b8e87492bd76cd19bbd1`
with zero unresolved names. Preserve the transition to
`vv/xbox_coop/xc_delta5_1` and medium expectation 735/0.

### Checkpoint 026 Hell 1 part 1 offline preflight

For `xc_hell1_1`, require decoded MAP SHA-256
`847cf3bf21bdcb5c1f5a74664863df2b10df8642f3778b9845b3a935eb6356ff`
at geometry CRC `2355691493`, PROC SHA-256
`7ad52761f2031be4b6f3102002d8e2c616b382debec9598f943d05927d4e8ac2`,
AAS48/AAS96 hashes `c6a80109729a6a1816aa60aaf9fb262fabac6e75d365d1bdada838121f330685`
and `7955490e4d6273cd1a398abe86ada835dbc26ace9051a3269b9a6614c7eb5dba`,
and authored CM SHA-256
`251fa1c1790d40709a0e8729f960547b12a282b853c4c941cb65f1d6f8a8c3c7`.
Decode all 308 selected model members.

Of 50 unique direct MAP WAV paths, recover the 15 absent stock paths through
the 14,150-byte INDEXLIST (SHA-256
`bf7c01db83f78f6f758b5e14f772a53fc1987e34ed42d40f26d256778fd229bd`)
and 26,108-byte XSB (SHA-256
`e47687831457dca78b92254ea5d6f978c22abf87fbee4920dcbce86daaf71d0b`).
The recovered WAV corpus totals 7,479,300 bytes. Use the prior source-bound
Delta 4 model root to supply eight player-machinegun animations omitted from
this segment archive. The final 286-file overlay manifest is 148,586 bytes,
hashes to `ca182608e92d3b34ba006e86ed6cd06e86aa5ca8f8c096747c3fc8ec747fcc69`,
and reports zero unresolved names. Preserve the 11 resolved callbacks and
transition to `vv/xbox_coop/xc_hell1_2`; expect 866/0 entities on medium.

### Checkpoint 025 Delta 4 offline preflight

For `xc_delta4`, require the 1,696,138-byte decoded MAP with SHA-256
`3b7357236b29a113c72d86b3126581964683d5ff111ab23495571c7fb8fa2e2a`,
the 1,639,005-byte PROC with SHA-256
`fe8b2fae0e92b3047fe0b3df8c84b026014477f670d4f467206d31ebe103d8bd`,
and direct authored CM SHA-256
`09f22305c424730b830fe76fc55a7f960941c77c5b737f010049e8b927621eb5`.
Select both corrected navigation files: AAS48 SHA-256
`fd529e4637b7f01c40392ee0cd3953fe6301d606a512f905a209289439415796`
and AAS96 SHA-256
`b664b956673dee6119c85551d2eb471dc2245066575aea5b2ff415cd80295eaf`.

Decode all 283 selected model members. Audit the MAP's 35 unique direct WAV
paths against stock WAV/OGG members. Recover the sole absent path,
`sound/foley2/pipes/airgen_04.wav`, through the 14,150-byte Delta 4 INDEXLIST
(SHA-256 `cc20fd7ca77f96067c580dcf3c4790a5875d30e892318d8e71ae1bf99f545fd1`)
and the 21,856-byte XSB (SHA-256
`7c98b3bffc99562c0bc234d64e9aa7a3da7d821817a1bf97347ce32a892fb990`).
The recovered 250,684-byte PCM WAV must hash to
`6c7f1d4d300c0163057c53bce45a2c24b3789bb7f4530e4b49d50612265aa3f7`.

Build with `xc_delta4.resources`, the decoded model root, the map's 68-file
runtime dependency root and the shared roots used by checkpoint 024. The final
overlay has 273 files, 237 copied resources, one generated EFX and eight
transform records. Its 142,124-byte manifest hashes to
`4fe5dfe545dbf9a9c6e7994880dbba13aef3dacb053eaed2cce0418f83e0afca`
and reports zero unresolved names. No difficulty epairs are present, so the
default-medium expectation is 394 spawned and zero inhibited. Preserve the
transition to `vv/xbox_coop/xc_hell1_1`. Do not launch Doom 3 or run `dmap`
until the campaign-wide offline pass is complete and executable testing is
explicitly cleared.

### Checkpoint 024 offline preflight

For `xc_delta2b_2`, verify GFC/GOB SHA-256 values
`acdf1c91bd3576ed6c13e17f289b5be3f1f39849167d5debf3794f41b9970434`
and `97b7f715a5b61b96bae9620e28f9715dffbbfa099854c71a6807f62686fc9221`.
Decode MAP, PROC, AAS48 and CM.X with the checkpoint-023 tools. Supply MAP CRC
`3474151774` to `decode_cm_x.py`. Require output hashes
`8855cf483adc48905176408fc4983bbdc75e5a2152c6b498a7664dd3939e0b76`,
`6112ed27ede585a7a2fd111cd7ca3cb1ffe6ac58658f05b46b66b173b25ec959`,
`f2824b57f2ac775fde482bf81a1691f4e48ad4b50f39c7cad8fa7471bae6bfe7`
and `eb4b5d4d8ce1ec47369fd217610a6cdfecb338584f2beaf971c23d5b5925ebcd`
respectively.

Extract and decode all 343 `.mdvmesh`, `.mdvanim` and `.md5anim.x` members.
They must produce 15,638,869 bytes. Add the five-entry
`xc_delta2b_2.resources` profile and place the checkpoint-023 retarget root
before the decoded model root. Build with the same shared player, HUD,
material, language and DEF roots as checkpoint 023, but preserve the retail
`maps/vv/xbox_coop/xc_delta2b_2.script`.

Audit all direct MAP `.wav` values against stock `.wav` and `.ogg` members.
Recover the four absent XSND names through the 14,150-byte INDEXLIST (SHA-256
`b2a8c43577c4c4a9a717c8637c95c9054b7624644eebe2fd4a6d0bee4e7557c3`)
and 28,724-byte XSB (SHA-256
`259c5e7658555a584b5eee41f0a304193fe85096e839598da27b39bab91123db`).
The four WAVs total 1,420,036 bytes. Correct exactly two `inner1.wav` MAP
epairs to the `inner_1.wav` spelling proven by both Xbox XSND and stock PC.

The resulting offline overlay has 276 file records, 241 copied resources, one
generated EFX, nine transform records and zero unresolved names. Its
137,118-byte manifest hashes to
`7a15c66f28e4c75ec017e24385b5826b3f48a70f8f84770acd1e25e684fd7229`.
Stop here unless a Doom 3 launch has been explicitly cleared: dmap and native
loader acceptance are still open. When cleared, require 843/0 on default medium
and verify the exit GUI reaches `vv/xbox_coop/xc_delta4` through
`target_endlevel_1`.

### Checkpoint 023 tenth-segment receipt

For `xc_delta2b_1`, verify GFC/GOB SHA-256 values
`2a81c50cad444d761a879b4af6107cfe251e3f75a39ecf31b4a19c2596df36ff`
and `7535a96fc95f5cd8df29c520291806d252773071300a22a897d0431e1e5087d9`.
The decoded MAP is 3,291,335 bytes, hashes to
`3060f42d9d5c6391321f6ce0c1ae6ab668e98fb02edddc6c4203b23b22f86621`
and has CRC `4216080146`. Direct CM is 2,677,242 bytes with SHA-256
`77d9173411637bc2a8de0bb4482246c426129a48fbb641fef2e96be4c4d9bce5`.
Require a 238/295 model audit: 238 shared, zero authored-only and all 57
PC-only models explained by `noclipmodel 1`.

Select the corrected 606,188-byte AAS48 with SHA-256
`00fa76e76e79830f9d1dbe9c029d6eb3a16b5ee649ccde4559dd1cb3b4c76bac`.
It must report 698 areas, 3,361 reachabilities, 2,532 nodes, zero unreachable
nonzero nodes and zero unreferenced nonzero areas. Decode all 437 selected model
files: 15 meshes and 422 animations, totaling 19,736,154 bytes.

Retarget the 50-joint Xbox ZCT `head_butt.md5anim` against the stock 63-joint
ZCT mesh with `retarget_md5anim.py --allow-target-expansion`. The 109,143-byte
result must hash to
`2c111bb859bc8816eaf22b66eaaa488d905ffcd8d594c2ddf8c2ec10c35a805b`,
contain 22 frames at 20 fps, 63 joints and 378 animated components, and restore
the 13 target-only joints listed in `head_butt-retarget.json`.

Build the portable overlay from the reconstruction checkout's ignored `work/`
tree. Root order is significant because the retargeted animation must shadow
the decoded 50-joint copy:

```powershell
python tools/campaign_port/build_runtime_overlay.py `
  --map work/checkpoint-023-delta2b-1/overlay-input/maps/vv/xbox_coop/xc_delta2b_1.map `
  --converted-dir work/checkpoint-023-delta2b-1/overlay-input/maps/vv/xbox_coop `
  --authored-cm work/checkpoint-023-delta2b-1/overlay-input/maps/vv/xbox_coop/xc_delta2b_1.cm `
  --retail-root work/checkpoint-023-delta2b-1/retargeted-pc-zct/base `
  --retail-root work/checkpoint-023-delta2b-1/runtime-models/base `
  --retail-root work/runtime-deps-all/xc_delta2b_1/base `
  --retail-root work/xact-first-map `
  --retail-root work/player-runtime-assets/base `
  --retail-root work/npc-runtime-assets/base `
  --retail-root work/decoded-mdv-xc_mars_city1_1-v2/base `
  --retail-root work/d3t-hud-missing-v3-dxt5 `
  --retail-root work/d3t-hud `
  --retail-root work/assets-materials/base `
  --retail-root work/shared-assets-extracted/base `
  --def-root work/shared-assets-extracted/base/def `
  --stock-dir ../../base `
  --language work/shared-assets-extracted/base/strings/english.lang `
  --language work/shared-assets-extracted/base/strings/english_vv.lang `
  --def-preference info.def `
  --runtime-classname player_doommarine1_coop `
  --runtime-classname player_doommarine2_coop `
  --runtime-resource-list tools/campaign_port/profiles/xbox_coop_player.resources `
  --runtime-resource-list tools/campaign_port/profiles/xc_delta2b_1.resources `
  --runtime-resource guis/hud.gui `
  --runtime-resource dds/guis/assets/health/hspike1.dds `
  --runtime-resource dds/guis/assets/hud/TipBorder.dds `
  --runtime-resource dds/guis/assets/hud/Vote.dds `
  --runtime-resource dds/guis/live/assets/FriendInviteReceived.dds `
  --runtime-resource dds/guis/live/assets/FriendOnline.dds `
  --runtime-resource dds/guis/live/assets/GameInviteReceived.dds `
  --runtime-material gui/radiospike `
  --runtime-material guis/assets/hud/TipBorder `
  --runtime-material guis/live/assets/FriendInviteReceived `
  --runtime-material guis/live/assets/FriendOnline `
  --runtime-material guis/live/assets/GameInviteReceived `
  --runtime-string '#str_07595' `
  --generate-empty-efx `
  --out ../../xbox_coop_port_test_delta2b_1_v9
```

The output must contain 278 file records, 237 copied resources, two generated
resources, ten transform records and no unresolved resource, classname or
string. Payload bytes total 21,533,147. The 141,486-byte portable manifest
hashes to
`af9e27cd3e71e5af3a730064f5b2955d9e59f39505b0a2294b264633ffe6cce6`;
the transformed MAP hashes to
`70baa31c9bc93d3c379842d17d3c5963db95e060fcfd3b627a1150b865d1c290`.

The last bounded true-`COOP` run used the pre-relocation overlay. It exited 0,
spawned 912/0 and joined player 0 with no missing resource, joint, AF/IK, error
or fatal line. Its 73,047-byte console log hashes to
`d8b37dbb04f788933fd4213652cde79db6b01ac49c90ef07ae3417c8e633c467`.
Do not call the relocation loader-confirmed yet. Validate the portable candidate
once when it will not interrupt another Steam session; expected closure is the
absence of both the separator-contact and overlapping-location warnings.

### Checkpoint 022 ninth-segment receipt

For `xc_recycling2_1`, verify GFC/GOB SHA-256 values
`960f4a494be1bcb40890f53525ea785f12b41c3b2a1dae3872282a38a6df51c9`
and `3eafec054af28591de0da0a5e62eb8030251c7bebfdd06b72d6a09275df4ad8e`.
The decoded MAP is 3,783,693 bytes, hashes to
`638d279a2df1553b4eaa94024e27e9fdeb22523f4ffbe360d998fdb64e1f92fc`
and has CRC `1305987032`. Direct CM is 3,515,885 bytes with SHA-256
`e8521f124483b5768c12c0a7ec16f8a053d0913e2da24dedd7f15064a7c975ab`.
Require a 105/209 model audit: 105 shared, zero authored-only and all 104
PC-only models explained by `noclipmodel 1`.

Decode both navigation payloads. AAS48 is 938,578 bytes with SHA-256
`82e45ff243a5a141d884d2a9cd4e3f2f91a4b2a8e7f9bdc9fff1864dae23c4a4`;
AAS Mancubus is 109,391 bytes with SHA-256
`46db7092f6056fa56de734d31e578dcc9cb040ca0a45ac599cae78dca04c5f82`.
Both must have zero unreachable nonzero nodes and zero unreferenced nonzero
areas. Decode all 341 selected model files: eight meshes and 333 animations,
totaling 15,301,709 bytes.

Recover the 29 warned sounds using the 14,150-byte
`xc_recycling2_1.indexlist` (SHA-256
`12767056d6cfbfab4942c184c005f6690cc888d988e176f1be6e664f7f37a32c`)
and 30,800-byte XSB (SHA-256
`312d824689520bbcc66ee5b57b18d4c137fc5b4a30b9182315bf5421df01df0e`).
Decoded WAVs total 10,514,246 bytes. Recover the exact
`textures/base_door/a_deldoorgutter_d02` diffuse image from Xbox D3TFULL key
`3D1761C9`; the 64x128, five-mip DDS is 5,584 bytes and hashes to
`e1a5206cf6a0313c14e7facd90c016852bdc73e5e108d1c8a31420d8d6fc872f`.
The finalized 157,889-byte overlay
manifest hashes to
`0115ae7f439fbfb11dca0750e27447905db4d546dd06aaf9de7c098d57bbfde4`
and records 305 files, 266 copied resources, one generated EFX, eight transform
records and zero unresolved resources, classnames or strings.

Under the isolated checkpoint-014 null-guard diagnostic, true `COOP` must exit
0, spawn 880 entities, inhibit exactly `ammo_rockets_large_3` and
`item_medkit_25`, and join player 0. Both inhibited entities carry
`not_medium 1` and `not_hard 1`. Require zero warned sounds, Mancubus AAS
failures, invalid joints, callback/class/script failures, errors or fatals.
The 16,541-byte log hashes to
`55ca644c18df489e8df6391cbb83498e7d35b24438c59b15662ba66f021cf4ba`.
Do not fabricate the absent `a_deldoorgutter_local` and
`a_deldoorgutter_s02` stages or the absent broken light model; preserve their
inventory and stock-baseline evidence.
Restore the root DLL and verify SHA-256
`1eb641d6869cf70bf947e4bc10208949f0a8344953bf1055ded7cf3b3ef74e34`.

### Checkpoint 021 eighth-segment receipt

For `xc_enpro_2`, verify GFC/GOB SHA-256 values
`514b41e35b597c95edfd8e613f41ef6c246d9d5bcc747786c800c3a2154a06f0`
and `4473d2764b4ba6b70598469d092f6609a772675e4be224daebf32ce9670fac6c`.
The decoded MAP is 2,319,237 bytes, hashes to
`d25ffc46afeefc1f349878ff6614675e7ad93e6c09d17cf5ba3030b833de9dc5`
and has CRC `2033356009`. Direct CM is 3,483,436 bytes with SHA-256
`bf1f3526c62e499a3f8048b33a88bbc41cb09ce0426f37ae0de782359fda43f6`.
Require a 163/169 model audit with six explained `noclipmodel 1` additions.
Decode all 321 selected model files. Recover the 11 warned sounds using
`xc_enpro_2.indexlist`/`xc_enpro_2.xsb`; decoded WAVs total 3,347,594 bytes.
The finalized 148,305-byte overlay manifest hashes to
`bd39b87b300753567b876243cfe94aa93ebe81db4dd9c7e1c869dfed2efc3e10`.
The bounded true-`COOP` run must spawn 579/0 and its 71,566-byte console log
must hash to
`8dbd8e09891c029c591f934d709c60e7922e52c055496a627d7f5322a5bca446`.

### Checkpoint 020 seventh-segment receipt

For `xc_enpro_1`, verify the source GFC is 155,432 bytes with SHA-256
`f5cf4150bf14f1092585a96e2b32cb26b5dd08c35eabe30f447cd186d6cde79a`
and its GOB is 8,126,464 bytes with SHA-256
`cf0ccf80778d2c437c3ea6dca4b31d15ca8f9e2707959f603defc75a55f3b98c`.
The decoded 3,626,728-byte MAP hashes to
`eaeaab2c082e4685b091802849f8ac1e6d91555c5c2847fa60c831d9cbc7cb0d`,
has geometry CRC `2226283201`, and contains 709 entities, 3,128 brushes,
18,917 brush sides, 1,724 patches and 33,456 patch points. The decoded PROC is
5,647,175 bytes with SHA-256
`1052809d82b998488b33b27a095148dc96afab828c78eb2c71984173568cb8f6`.
Select the corrected 1,020,377-byte AAS48 with SHA-256
`5bb7de9bd5ff8e7a4e415129d381fa60cd9b1998a92c6fde47ca20654c35f8b5`;
it audits to 1,112 areas, 5,319 reachabilities, 3,834 nodes and no unreachable
or unreferenced nonzero records. The archive has no AAS96.

Export the 3,240,749-byte CM.X directly. It must hash to
`a7e323b99295911eeb0afe4e05adb4e329150a07893ecd72b42ab603dbfed011`
and produce a 5,495,477-byte ASCII PC CM with SHA-256
`b79ce3b9f88d8dffdb7e8103a598a7f701738d1b32e9e9dd30e582de81f96735`.
The authored result contains 182 models, 24,495 vertices, 42,569 edges, 17,196
polygons, 3,029 brushes and 12,040 nodes. Independent PC `dmap` emits 208
models: 182 shared, zero authored-only and 26 PC-only, all 26 carrying
`noclipmodel 1`.

Extract every `.mdvmesh`, `.mdvanim` and `.md5anim.x` member selected from the
map GFC and retain one decoder report per file. Decode the complete 315-file set
to 10 meshes and 305 animations (231 MDV plus 74 MD5ANIM.X), totaling
13,851,502 bytes. The 48-joint skeleton hashes to
`f7a0d02251409120e16bd545a88912121369d198c50e6f2ad8acae2a1e400c09`,
byte-identical to three earlier independent segment copies.

Recover the 16 runtime sounds through `xact_audio.py`. Use the 14,150-byte
`xc_enpro_1.indexlist` with SHA-256
`f1d22742b1c6c6dd79c8687c07a695b4a6aa27830b5c30ce7c868b1d44479bc9`,
the 27,324-byte `xc_enpro_1.xsb` with SHA-256
`5036bbc485f8bb3c31d26ab3c92eacedcd7ef4e53364804f4f8dc0dc97574a32`,
and the inventoried global/memory XWB extents. The 16 ordinary PCM WAVs total
5,535,714 bytes; the 8,186-byte manifest hashes to
`318406c6f11f51a4fd897323ceabb0acfe912d6aeb698e429356f41c649d9d04`.
Do not substitute `monster_demon_maggot_sight2`: it is absent from both the
global XSND header and recovered archive inventories, so disable only that DEF
epair.

Three additional exact witnesses are required. Disable the one MAP call to
`setupCoop`, because the only retail body is inside a block comment. Correct
`grenadeExplosion.ips` to `grenadeExplosion.prt` exactly once in `func.def`;
other Xbox declarations and stock PC `func.def` agree on the shipped `.prt`.
Select the exact previously recovered `dds/lights/nofalloff.dds` beneath the
existing stock PC material. Keep all inherited HUD/player/icon transforms.

The finalized direct-CM overlay must have 292 file records, 253 copied
resources, one generated empty EFX, 32,092,469 payload bytes, ten transform
records and zero unresolved resources, classnames or strings. Its 150,921-byte
manifest hashes to
`82c6d323c48bd2dc30bd91a0bbd845fad81eb04bb528f8e051fd653df045e038`.
Under the isolated checkpoint-014 null-guard diagnostic, preserve the original
instant-hit declarations and start true `COOP`. The bounded run exits 0,
spawns 709/0 and joins the player with no map-specific warning, missing
resource, invalid joint, callback/class/path failure, error or fatal. The
71,530-byte console log hashes to
`92bb90ea0c74623166f4e8b00ec7f4a24c88c95fc9090d448ddcb5c66de8d182`.
Restore the root DLL and verify SHA-256
`1eb641d6869cf70bf947e4bc10208949f0a8344953bf1055ded7cf3b3ef74e34`.

### Checkpoint 019 sixth-segment receipt

For `xc_alphalabs2_2`, verify the source GFC is 145,648 bytes with SHA-256
`8765c5a9627d6ac542a7add9b1185a30593cae7176f65a0e616f73cdd6444760`
and its GOB is 8,239,104 bytes with SHA-256
`e936c315145995f1f6c97ba04e4001318ca525582f951cd794442b75a5fe6f0f`.
The decoded 3,787,497-byte MAP hashes to
`ca9f74dc12b45f009cf47992d43c2b49eedd367539e7ae568d4120309eba6e79`,
has geometry CRC `3745531086`, and contains 766 entities, 2,782 brushes,
16,618 brush sides, 2,071 patches and 45,495 patch points. The decoded PROC is
8,114,149 bytes with SHA-256
`d2cf4f09e16f153d691ec44819f8dfad346ea6553409f5cb752ec0755f9ef5c7`.
Select the corrected 672,630-byte AAS48 with SHA-256
`f56dd1520d36f818bb780fdb05286b0f1053dbb42996eebac7e0f8c389d148f9`;
it audits to 731 areas, 3,319 reachabilities, 2,760 nodes and no unreachable or
unreferenced nonzero records. The source archive has no AAS96.

Export the 3,298,539-byte CM.X directly. It must hash to
`ead3f036f050b67650ca9175743a2f649b4f9faed05389e9aa7852e3ec8d8180`
and produce a 5,784,631-byte ASCII PC CM with SHA-256
`18b6fd6fbd746d5aae3dbf1559e67d7e4cb1f43915515848615ec17e220dfeba`.
The authored result contains 147 models, 24,551 vertices, 43,280 edges, 18,742
polygons, 2,719 brushes and 9,801 nodes. Independently run PC `dmap`; its CM
must contain 261 models. Audit names against the MAP: 147 shared, zero
authored-only and 114 PC-only, with all 114 carrying `noclipmodel 1` and zero
unexplained names.

Extract every `.mdvmesh`, `.mdvanim` and `.md5anim.x` member selected from the
map GFC, retaining path identity and one decoder report per file. Decode the
complete set to eight meshes and 291 animations (217 MDV and 74 MD5ANIM.X),
299 files and 13,095,353 output bytes. The decoded skeleton must hash to
`f7a0d02251409120e16bd545a88912121369d198c50e6f2ad8acae2a1e400c09`,
byte-identical to the independently recovered `xc_mars_city1_1` and `xc_mcu`
copies. Expected mesh joint counts are 50/50 for the two players, 37 for the
z4 head, 48 for skeleton, 44 for player head, 41 for imp, 48 for trite and 48
for the T-shirt zombie.

Build the overlay with the direct authored CM, corrected AAS48, complete
decoded map-local model root, shared player roots/profile, stock zombie AF,
seven explicit HUD resources, five shared HUD/Live materials, `map_alphalabs2`
and co-op DEF preferences, and an empty EFX. No Alpha-Labs-specific transform
is required. The only eight transform records must be the existing empty EFX,
stock zombie AF endpoint alias, HUD command/status fixes, DXT5 material hints,
player neck-control alias and three proven-unshipped inventory icons.

The result must have 274 file records, 237 copied resources, one generated
resource, 29,082,749 payload bytes and zero unresolved resources, classnames or
string IDs. Its 133,929-byte manifest hashes to
`a0cb08707e5ac5e500c8d34cf3cb8a8d4817a9d63a0628056555724e6e10dba6`.
Under the isolated checkpoint-014 null-guard diagnostic, preserve the original
instant-hit declarations and start true `COOP`. The bounded run exits 0, spawns
764 entities, inhibits exactly `ammo_clip_large_27` and
`item_armor_security_8`, and joins the player. Both inhibited entities are
retail player-two pickups with `not_medium 1` and `not_hard 1`; do not remove
those flags. Require zero map-specific warnings, missing resources, invalid
joints, callback/class/path failures, errors or fatals. The 72,923-byte console
log hashes to
`4093fa656dd67a8c817d51f0e4dab6436f097cab6241df28f4627ccfcee43540`.
Restore the root DLL and verify SHA-256
`1eb641d6869cf70bf947e4bc10208949f0a8344953bf1055ded7cf3b3ef74e34`.

### Checkpoint 018 fifth-segment receipt

For `xc_mcu`, the decoded MAP is 3,223,941 bytes with SHA-256
`bda959ab77d6465eecc4d38d4b33ce5d61d4d7cf7fb05136df32b52dcbd5b144`
and geometry CRC `2327495450`. The decoded PROC is 3,904,441 bytes with
SHA-256 `14fb9a9d2123e9f432c8949ebe5f6a875462d52c6fe4b1e8584d1d72cd4bb574`.
Select the corrected 466,213-byte AAS48 with SHA-256
`4b1bf8e5d89af1a013beb97de01868eaccc4ef07a20f1baa1c63f1732b37c0eb`;
the map archive has no AAS96 member.

The 2,175,464-byte CM.X hashes to
`4a7131ba4caa365927de48f8d81fff2bbe77627cb0f6221288fec6133b0d71c7`
and expands to a 3,537,686-byte authored CM with SHA-256
`98551ea432d106f5d1f60393b7856337b6d8282ddd464fa5fc516b553efc9aff`.
The model audit must report 212 authored, 228 PC-`dmap`, 212 shared, zero
authored-only, 16 PC-only, all 16 marked `noclipmodel 1`, and zero unexplained.

Extract every map-local MDV member rather than stopping at the first reported
dependency:

```powershell
python tools/campaign_port/gfc.py extract `
  game/campaign_port_inputs/xc_mcu.gfc `
  --gob game/campaign_port_inputs/xc_mcu.gob `
  --include "*.mdvmesh" --include "*.mdvanim" `
  --out game/campaign_port_work/xc_mcu-all-mdv
```

Decode each `.mdvmesh` to the same relative `.md5mesh` path and each
`.mdvanim` to `.md5anim` with `decode_mdv.py`, retaining one `--report` receipt
per member. The complete input/output set is exactly 410 files: 19 meshes and
391 animations. The decoded outputs total 21,766,572 bytes. The 48-joint
decoded skeleton hashes to
`f7a0d02251409120e16bd545a88912121369d198c50e6f2ad8acae2a1e400c09`,
byte-identical to the independently recovered first-segment copy.

The pruned Xbox meshes omit AF terminal joints while retaining a predecessor in
the same finger chain. Add the unmodified stock PC AF files as retail roots and
let the overlay builder apply its exact path-scoped aliases: `Rfings3/Lfings3`
to `Rfings2/Lfings2` in `monster_zombie_base.af`, and to
`Rfings1/Lfings1` in both security AFs. Each source endpoint must occur exactly
twice or the build must fail; do not make a general joint-name rewrite.

Recover the observed light image directly from D3TFULL:

```powershell
python tools/campaign_port/d3tfull.py retail.iso lights/spot08 `
  --offset 2825555968 --size 178959016 `
  --output game/campaign_port_work/d3t-mcu-lights --json
```

Expected key is `06EFB410`; the 64×64, five-mip, format-`000083F0` DDS is
2,856 bytes with SHA-256
`6f07805e4367a6fa7fd3d430852e60358a69908a9d1a18b3b318e1ffb14326ea`.
Stock PC already declares `lights/spot08`. Copy the exact Xbox DDS but do not
select a second material body: doing so creates a redundant declaration. Do not
use a surrogate image or material.

Two Xbox-authored defects require exact receipts. In
`guis/mc_underground/security_coop.gui`, replace exactly two references to the
undeclared `ContentClipLocker2::rect` with the declared
`ContentClipLocker::rect`. In the MAP, make only `info_location_11` at
`792 -848 88` inert; it overlaps `info_location_9` at `784 -848 88` in the
same portal area and both name `#str_02859`. The second transform changes only
the classname to `target_null`, so the geometry CRC remains unchanged. Both
transforms must fail closed if their complete witnesses do not match.

Build with the shared 229-entry player profile followed by the 414-entry
`xc_mcu.resources` profile, the complete decoded MDV root, the stock-AF root,
the light DDS root, the map and inherited dependency roots, direct authored CM,
and these explicit roots:

```powershell
python tools/campaign_port/build_runtime_overlay.py `
  --map game/campaign_port_work/converted/maps/vv/xbox_coop/xc_mcu.map `
  --converted-dir game/campaign_port_work/converted/maps/vv/xbox_coop `
  --authored-cm game/campaign_port_work/authored-cm/maps/vv/xbox_coop/xc_mcu.cm `
  --retail-root game/campaign_port_work/decoded-all-mdv/base `
  --retail-root game/campaign_port_work/stock-af-root `
  --retail-root game/campaign_port_work/d3t-mcu-lights `
  --retail-root game/campaign_port_work/runtime-deps-all/xc_mcu/base `
  --retail-root game/campaign_port_work/runtime-deps-xc_mars_city1_1/base `
  --retail-root game/campaign_port_work/decoded-mdv-xc_mars_city1_1-v2/base `
  --retail-root game/campaign_port_work/decoded-xanim-xc_mars_city1_1-v4 `
  --retail-root game/campaign_port_work/player-runtime-assets/base `
  --retail-root game/campaign_port_work/npc-runtime-assets/base `
  --retail-root game/campaign_port_work/d3t-hud `
  --retail-root game/campaign_port_work/d3t-hud-missing-v3-dxt5 `
  --retail-root game/campaign_port_work/d3t-lights-nofalloff `
  --retail-root game/campaign_port_work/xact-first-map `
  --retail-root game/campaign_port_work/assets-materials/base `
  --retail-root game/campaign_port_work/shared-assets-extracted/base `
  --runtime-resource-list tools/campaign_port/profiles/xbox_coop_player.resources `
  --runtime-resource-list tools/campaign_port/profiles/xc_mcu.resources `
  --runtime-resource dds/guis/assets/health/hspike1.dds `
  --runtime-resource dds/guis/assets/hud/TipBorder.dds `
  --runtime-resource dds/guis/assets/hud/Vote.dds `
  --runtime-resource dds/guis/live/assets/FriendInviteReceived.dds `
  --runtime-resource dds/guis/live/assets/FriendOnline.dds `
  --runtime-resource dds/guis/live/assets/GameInviteReceived.dds `
  --runtime-resource guis/hud.gui `
  --def-preference map_underground_xbox_coop.def `
  --def-preference coop_defs_engineering.def `
  --runtime-classname player_doommarine1_coop `
  --runtime-classname player_doommarine2_coop `
  --runtime-string '#str_07595' `
  --runtime-material gui/radiospike `
  --runtime-material guis/assets/hud/TipBorder `
  --runtime-material guis/live/assets/FriendInviteReceived `
  --runtime-material guis/live/assets/FriendOnline `
  --runtime-material guis/live/assets/GameInviteReceived `
  --generate-empty-efx `
  --stock-dir base --language english `
  --out game/campaign_port_work/overlay-xc_mcu
```

The finalized overlay must have 540 file records, 497 copied resources, one
generated empty EFX, 35,404,668
payload bytes, zero unresolved resources/classnames/string IDs and 246,171
manifest bytes with SHA-256
`0bf20c433a5c1ff5cd40c546d3df23f1d2d91b705834876ec76bbf2adda72f2f`.

Under the isolated checkpoint-014 null-guard diagnostic, this bounded run exits
0, spawns 811/0 and joins the local player:

```powershell
.\Doom3.exe +set fs_game xbox_coop_port_test_mcu_v5 `
  +set developer 1 +set logFile 2 +set r_fullscreen 0 +set s_noSound 1 `
  +set si_gameType Coop +set net_LANServer 1 `
  +map vv/xbox_coop/xc_mcu +wait 500 +quit
```

The qconsole is 71,005 bytes with SHA-256
`2c571e01998c38a020639a3ac3eb3a169972ec47f1662199e1b0063d65091969`.
It contains no map-specific warning, missing resource, invalid joint, callback,
class, path-diagnostic, error or fatal line. The sole unique map-run warning is
the stock PC `mpmain.gui` reference to undefined cvar `s_driver`. Restore and
verify root `gamex86.dll` SHA-256
`1eb641d6869cf70bf947e4bc10208949f0a8344953bf1055ded7cf3b3ef74e34`
afterward. Repeat with the normally rebuilt source guard before engine
acceptance; the diagnostic binary is not distributable.

### Checkpoint 017 fourth-segment receipt

For `xc_admin`, the decoded MAP is 2,107,679 bytes with SHA-256
`62fe382be45687b646afff6dc7c19d980b25947caa0e3e403cac31ba0f5674fb`
and geometry CRC `25560181`. Select the corrected AAS48 and AAS96 outputs:

- AAS48: 824,144 bytes, SHA-256
  `ab4194f0e152ea40cccbbfa4392a53783a4b48dbb7ce51cda7a0e3c41df3f41d`;
- AAS96: 208,113 bytes, SHA-256
  `b2ae58682ec87bd2fa42b22adb0081cf041d1fd73e4732fddbcf754dd2ac8a0c`.

The 1,282,663-byte CM.X hashes to
`1c9abcff91706ce701353fb108289c12ae55ff4d56084e02ce568aac317dc9cd`
and expands to a 1,929,264-byte authored CM with SHA-256
`5cfef93c02510b61383dca9f02103719546164caee851ca51a0df5ca7b8597df`.
The model audit must report 199 authored, 238 PC-`dmap`, 199 shared, zero
authored-only, 39 PC-only, all 39 marked `noclipmodel 1`, and zero unexplained.

Recover and decode the Pinky, zjump and combo MDV members selected by the admin
GFC. Also extract the shared Xbox `af/monster_zombie_chainsaw.af`; do not use the
stock PC AF, whose `Rfings3/Lfings3` endpoints are absent from the 43-joint
decoded zjump mesh. Add `tools/campaign_port/profiles/xc_admin.resources` after
the shared player profile when building the overlay.

The admin map has two exact source-data defects that must remain receipt-bearing:
its lone `func_spawner` has no Xbox DEF/XBE type and is staged as the inert
`target_null`, while `map_admin1::setupCoop` has no retail script body and is
disabled. Because the retail GFC contains no map script member, generate only an
empty `void main() {}` PC entry point. The Xbox Pinky exporter renames `LoNeck`
to `Waist`; disable the stale `look_joint LoNeck` epair rather than inventing a
joint.

Recover `leftframe_d`, the keycard icon and `id_gui` by logical name from the
global D3T. The paired `leftframe_s`, `leftframe_local`, `id_badge_s` and
`id_badge_local` keys are absent from the Xbox D3T and stock PC PK4 corpus.
Stage the original Xbox `materials/base_door.mtr` and `materials/monsters.mtr`
at their native paths and disable only those four stale stages; never substitute
sibling images.

The final overlay has 322 file records, 20,042,389 payload bytes, 185,030
manifest bytes and manifest SHA-256
`dd04275263441f557cbe320750b8e14f590332b1fe62cbb8e2c49d782a268abf`.
It has zero unresolved resources, classnames or strings. Under the isolated
checkpoint-014 null-guard diagnostic, the bounded true-`COOP` run exits 0,
spawns 883/0, joins the player, and emits no missing-resource, invalid-joint,
callback, class, path-diagnostic, `ERROR` or `FATAL` line. The qconsole SHA-256
is `55fb1d21af782a1c556e70e5c64f7a06f8328384c0183a001e3e2cdbaaf75ff1`.
The remaining `tim_admin_wounded_marine_1 has no AAS file` line is intentional:
both Xbox and stock PC `admin_wounded_marine` explicitly set `use_aas` to empty.
Repeat with the normal rebuilt source DLL before engine acceptance.

### Checkpoint 016 third-segment receipt

For `xc_mars_city2_2`, compute the MAP CRC and export direct collision exactly
as described below. Expected MAP CRC is `2356338129`; expected authored CM is
1,526,425 bytes with SHA-256
`28f66afd7f18544c18cfd59aa8bb3b34190f596660a33b44bcc6bcd98b0deed7`.
The model-set audit must report 129 authored, 171 PC-`dmap`, 129 shared, zero
authored-only, 42 PC-only, all 42 marked `noclipmodel 1`, and zero unexplained.

Use the corrected AAS48, not the original pre-plane-fix corpus output:

```powershell
Get-FileHash game/campaign_port_work/converted/maps/vv/xbox_coop/xc_mars_city2_2.aas48 -Algorithm SHA256
```

Expected SHA-256 is
`bf118f9643843b369c6de0c371356aa4150b1509c6c5c2baf951c7ec4bba8657`.
Recover the only additional observed texture directly from D3TFULL:

```powershell
python tools/campaign_port/d3tfull.py retail.iso lights/nofalloff `
  --offset 2825555968 --size 178959016 `
  --output game/campaign_port_work/d3t-lights-nofalloff --json
```

Expected archive key is `9704C74E`; the 296-byte output
`dds/lights/nofalloff.dds` hashes to
`1d632a0e7b695186ed6462ff026215fe4bf217c6a57370a5bb9c9dfdd775e11b`.
Add that DDS as a runtime resource and its output directory as a retail root.
Do **not** add `lights/nofalloff` as a runtime material: stock PC
`materials/lights.mtr` already declares it.

The final overlay has 276 file records, 16,290,916 payload bytes, 133,402
manifest bytes and manifest SHA-256
`53e8f9022d5b399de4a14709cde49497aafaac7143d3865da8928e56f83d567b`.
Under the checkpoint-014 control-flow diagnostic, the bounded true-`COOP` run
must exit 0, spawn 516/0, join the player, and emit no missing-resource,
skeleton, path, `ERROR` or `FATAL` line. The qconsole SHA-256 is
`6d2e4b88e260b07b09a8e51e780701a5565b5a81a71aa0e32d97759e8f1d144e`.
Repeat with the normal rebuilt source DLL before engine acceptance.

### Checkpoint 015 corrected second-map closure

Do not use the checkpoint-014 AAS48 hash
`9778ae62f8d9e937afa7d89bc1e4a856dcf6ceac2e97daf8f926ae93dfa908a9`.
It is an obsolete pre-plane-distance-fix output. Select the regenerated file:

```powershell
Get-FileHash game/campaign_port_work/converted/maps/vv/xbox_coop/xc_mars_city2_1.aas48 -Algorithm SHA256
python tools/campaign_port/aas_route_audit.py `
  game/campaign_port_work/converted/maps/vv/xbox_coop/xc_mars_city2_1.aas48 `
  --start=-956,-1456,128.25 --goal=-808,-1472,128 `
  --travel-flags 0x400002
```

Expected SHA-256 is
`6e9f0b2cbd8981c3117cb20e029d390c4aa792fd449aad64ae3d241f0f70338e`;
expected route is areas `41,39,38,37,35,34`.

Build the city2 overlay with the same roots and explicit HUD/material arguments
used below, but add the shared profile:

```powershell
python tools/campaign_port/build_runtime_overlay.py `
  --map game/campaign_port_work/converted/maps/vv/xbox_coop/xc_mars_city2_1.map `
  --converted-dir game/campaign_port_work/converted/maps/vv/xbox_coop `
  --runtime-classname player_doommarine1_coop `
  --runtime-classname player_doommarine2_coop `
  --runtime-resource-list tools/campaign_port/profiles/xbox_coop_player.resources `
  --authored-cm game/campaign_port_work/authored-cm/maps/vv/xbox_coop/xc_mars_city2_1.cm `
  --out game/campaign_port_work/overlay-xc_mars_city2_1
```

The profile has 229 entries and SHA-256
`054ada1a04e2bcc6abd6aaae63a40ef8589e3af08a878c098cbd2ed6baa6ddd7`.
The builder must record 15 exact
`disable-unshipped-map-inventory-icon` edits for the unshipped armor-shard
image. Verify the absence against all campaign/MP GFC inventories and both
shared-assets inventories before applying that transform to another source
set.

The resulting manifest has 279 file records, 21,649,981 payload bytes,
137,760 manifest bytes and SHA-256
`dd71366abf46be7cc3caa1139cfd50e99938dde726509fe8e3083f01ec24c465`.
With the original Xbox declarations and the isolated checkpoint-014 null-guard
control-flow diagnostic, the bounded true-`COOP` run must produce exit 0,
1,110 spawned, zero inhibited, a joined player, and no missing-resource,
skeleton, path, `ERROR` or `FATAL` line. Its qconsole SHA-256 is
`3274fabe44fb0a6a78ed5062cf3d4b93420dd6219329007b768afc64a13ed943`.
Repeat this run with the normally rebuilt source DLL before accepting engine
integration; the diagnostic binary is not distributable.

### Checkpoint 014 second-map receipt

Decode `xc_mars_city2_1.map.x`, `.proc.x`, `.cm.x` and `.aas48.x` with the same
commands documented below for the first map. Compute the MAP geometry CRC before
exporting CM.X:

```powershell
python tools/campaign_port/map_geometry_crc.py `
  game/campaign_port_work/converted/maps/vv/xbox_coop/xc_mars_city2_1.map `
  --report game/campaign_port_work/reports/xc_mars_city2_1-map-crc.json

python tools/campaign_port/decode_cm_x.py `
  game/campaign_port_work/extracted/base/maps/vv/xbox_coop/xc_mars_city2_1.cm.x `
  game/campaign_port_work/authored-cm/maps/vv/xbox_coop/xc_mars_city2_1.cm `
  --map-crc 3219770337 `
  --report game/campaign_port_work/reports/xc_mars_city2_1-cm.json
```

The expected authored-CM receipt is 2,927,667 bytes and SHA-256
`dfbebaf505573f89050d3f0b4c2f3ded68ec17de79074d7a9f944a7d2b75999f`.
The exact decoded MAP receipt is 3,573,456 bytes and SHA-256
`a194564447251774131297325e1892f156890e8c5ccc0d90ea410459367c1f16`.
Retain an independent PC `dmap` build; its expected CM receipt for this input is
5,321,250 bytes and SHA-256
`a9335129600acd618de9e762d3032303ea41a36a9ae718ca511e0aa0523e6a33`.

Build the authored-CM overlay with the ordinary map set still pointing to the
PC-compiled MAP/PROC/CM/AAS directory:

```powershell
python tools/campaign_port/build_runtime_overlay.py `
  --map game/campaign_port_work/converted/maps/vv/xbox_coop/xc_mars_city2_1.map `
  --compiled-root game/campaign_port_work/converted `
  --authored-cm game/campaign_port_work/authored-cm/maps/vv/xbox_coop/xc_mars_city2_1.cm `
  --stock-dir base `
  --out game/campaign_port_work/overlay-xc_mars_city2_1
```

The checkpoint-014 provisional manifest has 50 file records, 11,425,489
payload bytes and SHA-256
`d893d9650a09cd0d364f12ef1765277848371ebd96c4fbc18f76aa19880ed1d0`.
It is intentionally not an acceptance fixture: no runtime-resource list was
available, and native player creation exposes dependencies outside the map-root
closure.

Run the real COOP path with the verified reconstruction DLL and the Xbox
declarations unchanged:

```powershell
.\Doom3.exe +set fs_game xbox_coop_port_test_city2_v1 `
  +set com_allowConsole 1 +set logFile 2 +set r_fullscreen 0 +set r_mode 3 `
  +set s_noSound 1 +set si_pure 0 +set si_gameType COOP `
  +set si_map vv/xbox_coop/xc_mars_city2_1 `
  +set g_xboxCoopPathDiagnostics 1 +spawnServer +wait 600 +quit
```

The checkpoint DLL SHA-256 is
`1eb641d6869cf70bf947e4bc10208949f0a8344953bf1055ded7cf3b3ef74e34`.
The expected pre-fix result is an access violation at DLL RVA `0x10caf0` while
spawning the first instant-hit zsec. In a debugger or minidump, the instruction
is `mov eax,[ecx+0x248]` with `ecx == 0`, returned to from RVA `0x22c4d`.
Disassembly of RVA `0x16b70` must also show the `net_instanthit` early-null
path before claiming the same diagnosis on a different build.

Do not ship or commit the diagnostic that changes `net_instanthit` to zero.
It is useful only to prove the boundary: changing the machinegun definition
alone advances to the shotgun and the identical fault; changing every selected
instant-hit definition produces 1,110 spawned, 0 inhibited and exit 0. The
accepted repair belongs in `vendor/doom3-gpl/neo/game/ai/AI.cpp`: guard the
dimension probe when `CreateProjectile` intentionally returns null, preserve a
zero projectile radius for that case, and continue deriving velocity, gravity
and speed from `projectileDef`.

For checkpoint 014, an isolated eight-byte control-flow diagnostic applied that
branch directly after the `CreateProjectile` call while leaving every original
Xbox definition unchanged. Its DLL SHA-256 was
`426af4d3ba58514d4a898f665dbf82eb856d8f08229966e4f6a9c2f0cb24ff71`;
the run produced 1,110 spawned, 0 inhibited, local-player join and exit 0. The
log SHA-256 was
`658924ea0e0cbf2d18e9a73789635c344592ecfd95e51a8448b163553f7a7a40`.
The root DLL was then restored to
`1eb641d6869cf70bf947e4bc10208949f0a8344953bf1055ded7cf3b3ef74e34`.
Do not reproduce or distribute the binary patch as a release artifact; apply
the equivalent source guard, build normally, and rerun this gate.

Keep licensed inputs and generated outputs below ignored local directories such
as `game/campaign_port_inputs` and `game/campaign_port_work`. Never add an ISO,
GFC/GOB archive, extracted asset or converted map to either repository.

## Disc and archive extraction

Inventory the exact XDVDFS image before extracting it:

```powershell
python tools/campaign_port/xdvdfs.py inventory `
  game/campaign_port_inputs/xbox/doom3.iso `
  --report game/campaign_port_work/xdvdfs-inventory.json

python tools/campaign_port/xdvdfs.py extract `
  game/campaign_port_inputs/xbox/doom3.iso `
  --out game/campaign_port_work/retail-archives `
  --include 'base/xc_*.gfc' --include 'base/xc_*.gob'
```

Both extractors require new output directories and never overwrite. For each
co-op pair, select map products and scripts while retaining the full inventory
as the dependency ledger:

```powershell
python tools/campaign_port/doom3_campaign_port.py inventory `
  game/campaign_port_work/retail-archives/xc_map.gfc `
  --gob game/campaign_port_work/retail-archives/xc_map.gob `
  --report game/campaign_port_work/inventory-xc_map.json

python tools/campaign_port/doom3_campaign_port.py extract `
  game/campaign_port_work/retail-archives/xc_map.gfc `
  --gob game/campaign_port_work/retail-archives/xc_map.gob `
  --out game/campaign_port_work/extracted-xc_map `
  --include '*.map.x' --include '*.proc.x' --include '*.cm.x' `
  --include '*.aas*.x' --include '*script/maps/vv/xbox_coop/*'
```

Retail STBL records must have an exact `ENBL` footer after their stored or zlib
body. Unknown envelopes, codecs, paths, incomplete streams and extra bytes fail
closed. Extraction reports retain source hashes and block contributions.

## Decode MAP.X, PROC.X, AAS.X and CM.X

Run each decoder against the corresponding extracted member. Output/report paths
must not already exist.

```powershell
python tools/campaign_port/decode_map_x.py source.map.x converted.map `
  --report map-report.json
python tools/campaign_port/decode_proc_x.py source.proc.x converted.proc `
  --report proc-report.json
python tools/campaign_port/decode_aas_x.py source.aas48.x converted.aas48 `
  --report aas48-report.json
python tools/campaign_port/decode_cm_x.py source.cm.x converted.cm `
  --map-crc 2410032894 --report cm-report.json

python tools/campaign_port/doom3_campaign_port.py inspect converted.proc `
  --require-decoded --report proc-inspection.json
```

The packed plane row stores the internal engine equation
`normal dot point + d = 0`, but standard PC AAS text stores
`idPlane::Dist() == -d`. The decoder must negate the packed fourth float.
A direct copy can still parse while sending native point-to-area lookup into
the wrong BSP leaves, so keep the nonzero-distance tests enabled.

CM.X uses the same internal-plane convention, so the CM exporter negates every
brush/polygon plane's fourth float. CM.X does not carry the PC MAP geometry CRC;
`--map-crc` must be the exact CRC printed in the standard CM generated from the
same converted MAP. Do not borrow a CRC from another map or suppress the PC
loader's CRC check.

Audit the complete extracted collision corpus before export:

```powershell
python tools/campaign_port/cm_corpus_audit.py `
  game/campaign_port_work/extracted-all `
  --require-count 1200 --report game/campaign_port_work/cm-x-corpus.json
```

For this checkpoint the audit must report 1,200 files, 391 unique payloads,
zero unreferenced polygons/brushes, zero within-node duplicate references and
corpus manifest SHA-256
`a4e1fd30551a26de22310c7c13085b527d9cd5e7fdbdeb35ef11a1791c3779ca`.

Compute and cross-check each converted MAP CRC, then hash all 20 direct CM
exports without retaining the outputs:

```powershell
python tools/campaign_port/map_geometry_crc.py converted.map `
  --report map-crc.json
python tools/campaign_port/cm_campaign_export_audit.py `
  game/campaign_port_work/converted/maps/vv/xbox_coop `
  game/campaign_port_work/extracted-all `
  --require-count 20 --report game/campaign_port_work/cm-export-corpus.json
```

Expected totals are 20 files, 43,791,272 CM.X bytes, 71,372,306 generated PC
CM bytes and 3,633 models. The binding manifest digest is
`3a27835c398b2d5c9bd280a29c397efe47868ea965ae4d9f9900fa2755cf0603`.
For `xc_mars_city1_1`, `map_geometry_crc.py` must return `2410032894`,
matching the CRC independently written by native `dmap`.

Explain the first map's authored/generated model-set difference:

```powershell
python tools/campaign_port/cm_model_set_audit.py `
  converted/maps/vv/xbox_coop/xc_mars_city1_1.map `
  extracted/base/xbox_gen/maps/vv/xbox_coop/xc_mars_city1_1.cm.x `
  dmap/maps/vv/xbox_coop/xc_mars_city1_1.cm `
  --report cm-model-set.json
```

Expected: 243 authored models, 277 PC-`dmap` models, all 243 shared,
34 PC-only models, all 34 mapped to `noclipmodel 1`, and zero unexplained or
authored-only names.

Repeat over all 20 `xc_` archive pairs. Expected checkpoint-004 coverage is 20
MAP reports, 20 PROC reports, 20 AAS48 reports and six AAS96 reports. Every PROC
inspection must return decoded true. A count mismatch, unconsumed byte, invalid
index/reference, unexpected delimiter or non-finite float is a decoder failure;
do not continue that map with guessed values.

## Focused native validation

Keep the decoded MAP and source map script under
`base/maps/vv/xbox_coop` and `base/script/maps/vv/xbox_coop`. Run native `dmap`
once to generate PC collision and independently regenerate geometry:

```powershell
.\Doom3.exe +set com_allowConsole 1 +set logfile 2 `
  +dmap maps/vv/xbox_coop/xc_mars_city1_1 +quit
```

Replace the generated AAS48 with the decoded AAS48. For direct-collision
validation, preserve the generated CM byte-for-byte, replace it temporarily
with the decoded CM carrying the same MAP CRC, and restore the generated file
after the run. Hash all three states. Then use the map name relative to
`base/maps` for a bounded loader smoke check:

```powershell
.\Doom3.exe +set com_allowConsole 1 +set logfile 2 `
  +map vv/xbox_coop/xc_mars_city1_1 +wait 240 +quit
```

Checkpoint 009 expects `[Load AAS]` for the recovered AAS48 and a collision
summary of 243 models, 15,146 vertices, 25,468 edges, 10,005 polygons, 2,784
brushes and 7,167 nodes for the direct first-map CM. The collision load should
complete in 29 ms on the recorded machine, followed by 940 spawned entities and
a clean shutdown. Any CM bad-token, CRC, model, index or truncation error is a
conversion failure. Do not distribute extracted or converted map products.

## Deterministic native collision comparison

Build the map-port game DLL containing the hidden
`xboxCoopCollisionDigest` command. Preserve the installed DLL and generated CM
by exact hash. The command syntax is:

```text
xboxCoopCollisionDigest [count] [seed] [verbose] [model] [mask] [minx miny minz maxx maxy maxz]
```

`model` defaults to `worldMap`; `mask` defaults to `0x9`
(`SOLID|PLAYERCLIP`); the box defaults to
`(-16,-16,0)-(16,16,64)`. Supply either all six hull floats or none. Invalid
masks, inverted/partial hulls and unresolved model names must print `SKIP`
rather than run. Verbose mode emits 8,192 lossless rows for count 4096.

Start the true-`COOP` first map with the generated CM and run each profile,
saving a separate `qconsole.log`:

```text
xboxCoopCollisionDigest 4096 23 1 worldMap 0x111 -16 -16 0 16 16 64
xboxCoopCollisionDigest 4096 23 1 worldMap 0x801 -3 -3 -6 3 3 6
xboxCoopCollisionDigest 4096 23 1 doorClip_1 0x9
xboxCoopCollisionDigest 4096 23 1 trigger_coop_enablegui_2 0x1000
xboxCoopCollisionDigest 4096 23 1 func_static_52977 0x1
```

Replace only the CM with the direct CM.X export carrying the same MAP CRC and
repeat the identical commands. Restore both original files afterward and verify
their pre-test hashes. Compare each generated/authored pair without publishing
the licensed logs:

```powershell
python tools/campaign_port/compare_cm_trace_logs.py `
  game/campaign_port_work/traces/generated-profile.log `
  game/campaign_port_work/traces/authored-profile.log `
  --allow-differences `
  --report game/campaign_port_work/traces/profile-comparison.json
```

Omit `--allow-differences` for a strict equivalence gate. The comparator must
reject missing summaries, different summary input digests, different coordinate
bits or missing records. The input digest binds resolved model name, mask, hull,
model bounds, count, seed and raw coordinates. It separates stopping trajectory
(fraction/end position), contact geometry (point/normal/plane distance),
material/contents and stable topology.

For checkpoint 011, require 8,192 rows per run, 40,960 paired rows total, zero
summary/coordinate input mismatch, zero missing records and zero hit mismatch.
Expected non-equivalence totals are 121 trajectory, 2,741 contact-geometry, 875
metadata and 3,507 gameplay mismatches. Every point geometry agrees; all 2,742
geometry mismatches are swept-box records. Per-profile comparison report hashes
are recorded in `evidence/checkpoint-011.json`.

The command masks raw point-contents results before suppressing a trace because
the engine's point fast path ignores the requested contents mask. It also
normalizes `CONTACT_TRMVERTEX`'s pointer-cast polygon feature to zero so ASLR
cannot appear as topology. Do not weaken tolerances, discard contact points or
ignore material/content differences to manufacture equivalence.

## Live spawned-entity collision comparison

Checkpoint 012 adds an entity-target form to the diagnostic command. A leading
`@` resolves the current map entity and uses the live clip model's origin,
axis and absolute bounds:

```text
xboxCoopCollisionDigest 4096 31 1 @doorClip_1 0x9
xboxCoopCollisionDigest 4096 31 1 @trigger_coop_enablegui_2 0x1000
xboxCoopCollisionDigest 4096 31 1 @func_static_53167 0x1
```

Run each command once with the PC-`dmap` CM and once with the direct CM.X
export, in a freshly loaded `vv/xbox_coop/xc_mars_city1_1` COOP process. Keep
the DLL and CM swaps isolated and hash both before and after. Compare each pair:

```powershell
python tools/campaign_port/compare_cm_trace_logs.py generated-door.log authored-door.log --report door.json --allow-differences
python tools/campaign_port/compare_cm_trace_logs.py generated-trigger.log authored-trigger.log --report trigger.json --allow-differences
python tools/campaign_port/compare_cm_trace_logs.py generated-static.log authored-static.log --report static.json --allow-differences
```

Expected checkpoint-012 totals are 24,576 shared records, zero coordinate/input
or hit mismatches, 11 start-contents and skip mismatches, one trajectory
mismatch, 3,367 contact-geometry mismatches, 97 metadata mismatches and 3,393
gameplay mismatches. Each runtime load spawns 940 entities with none inhibited.
The exact commands, bounds, digests, counts and SHA-256 receipts are in
`evidence/checkpoint-012.json`.

## Claim limits

Corpus-wide decoding proves format coverage for this exact retail image, not
completion percentage. Native `dmap` is independent geometry validation, but
its CM and shadow products are not original-Xbox equivalence. One successful
map load proves parser/runtime entry only. Direct CM.X now passes the first-map loader boundary and a static PC-engine
trace matrix. Remaining-map and live transformed collision, all-map CM loading,
dependency binding, co-op spawns/respawns, transitions, two-peer progression and
comparison against Xbox visual/gameplay evidence remain required.

## Runtime asset conversion and overlay

Use the first map's audited dependency ledger to select inputs; do not bulk-copy
the disc. The decoders refuse malformed records and existing outputs:

```powershell
python tools/campaign_port/decode_mdv.py source.mdv --kind mesh `
  --out output.md5mesh --report output.mdvmesh.json
python tools/campaign_port/decode_mdv.py source.mdv --kind anim `
  --out output.md5anim --report output.mdvanim.json
python tools/campaign_port/decode_md5anim_x.py source.md5anim.x `
  --out output.md5anim --report output.md5anim-x.json
python tools/campaign_port/retarget_md5anim.py source.md5anim `
  --target-mesh target.md5mesh --out retargeted.md5anim `
  --report retarget.json
```

For one complete map archive, the fail-closed corpus wrapper selects every
`.mdvanim`, `.mdvmesh`, and `.md5anim.x`, verifies extracted hashes, maps them
to `.md5anim`/`.md5mesh`, rejects case-insensitive destination collisions, and
writes one atomic manifest:

```powershell
python tools/campaign_port/decode_model_corpus.py map.gfc `
  --gob map.gob --out campaign_port_work/map-models
```

On Windows the wrapper stages below the short system temporary path; nesting
both archive and corpus stages below a deep Steam checkout can exceed the
classic path limit for legitimate retail animation names. After conversion,
reopen and hash every raw and decoded member against the manifest. Checkpoint
035 covers 18,405 records (36,810 file reads) with zero missing files and zero
hash mismatches.

`d3tfull.py` takes the D3TFULL file or its containing ISO plus selected logical
image names. For the checkpoint disc identity, recover the six additional HUD
images directly from the inventoried extent without copying the whole archive:

```powershell
python tools/campaign_port/d3tfull.py `
  game/campaign_port_inputs/xbox/doom3.iso `
  --offset 2825555968 --size 178959016 `
  --output game/campaign_port_work/d3t-hud-missing `
  guis/assets/health/hspike1 `
  guis/assets/hud/TipBorder guis/assets/hud/Vote `
  guis/live/assets/FriendInviteReceived `
  guis/live/assets/FriendOnline `
  guis/live/assets/GameInviteReceived

python tools/campaign_port/doom3_campaign_port.py extract `
  game/campaign_port_work/retail-archives/assets.gfc `
  --gob game/campaign_port_work/retail-archives/assets.gob `
  --out game/campaign_port_work/assets-materials `
  --include '*materials/*.mtr'
```

`xact_audio.py` takes the matching XSND header, INDEXLIST, XSB and named XWB
banks plus selected logical sound names. These converters write a new directory
and manifest. Consult `--help` because bank names and other source extents come
from the source-bound inventory, not invented public paths.

Build the local overlay after conversion:

```powershell
python tools/campaign_port/build_runtime_overlay.py `
  --map game/campaign_port_work/converted/maps/vv/xbox_coop/xc_mars_city1_1.map `
  --converted-dir game/campaign_port_work/converted/maps/vv/xbox_coop `
  --retail-root game/campaign_port_work/extracted-first-map/base `
  --retail-root game/campaign_port_work/decoded-runtime `
  --retail-root game/campaign_port_work/d3t-hud-missing `
  --retail-root game/campaign_port_work/assets-materials/base `
  --def-root game/campaign_port_work/shared-assets/base/def `
  --stock-dir base `
  --language game/campaign_port_work/shared-assets/base/strings/english.lang `
  --language game/campaign_port_work/shared-assets/base/strings/english_vv.lang `
  --def-preference info.def `
  --runtime-classname player_doommarine1_coop `
  --runtime-classname player_doommarine2_coop `
  --runtime-resource-list tools/campaign_port/profiles/xc_mars_city1_1.resources `
  --runtime-resource guis/hud.gui `
  --runtime-resource dds/guis/assets/health/hspike1.dds `
  --runtime-resource dds/guis/assets/hud/TipBorder.dds `
  --runtime-resource dds/guis/assets/hud/Vote.dds `
  --runtime-resource dds/guis/live/assets/FriendInviteReceived.dds `
  --runtime-resource dds/guis/live/assets/FriendOnline.dds `
  --runtime-resource dds/guis/live/assets/GameInviteReceived.dds `
  --runtime-string '#str_07595' `
  --runtime-material gui/radiospike `
  --runtime-material guis/assets/hud/TipBorder `
  --runtime-material guis/live/assets/FriendInviteReceived `
  --runtime-material guis/live/assets/FriendOnline `
  --runtime-material guis/live/assets/GameInviteReceived `
  --generate-empty-efx `
  --authored-cm game/campaign_port_work/authored-cm/maps/vv/xbox_coop/xc_mars_city1_1.cm `
  --out game/campaign_port_work/overlay-xc_mars_city1_1
```

The manifest must list every callback/skeleton compatibility edit with input
and output hashes. It must also report `collision_source:
direct-authored-cm`, the shared embedded map CRC, and separate PC-`dmap` and
authored CM hashes. The builder rejects a missing file, wrong filename,
non-PC-text CM header or CRC mismatch before publishing the overlay. A hidden
or unrecorded manual edit invalidates the receipt.

Checkpoint 013's finalized first-map receipt is:

- 374 file records, zero unresolved resources and zero unresolved classnames;
- 34,299,470 payload bytes plus a 183,787-byte manifest;
- manifest SHA-256
  `97a07d80b1071d79a96bff5e85e729fdefdb8654f1a8f2d369928459ca532315`;
- generated CM SHA-256
  `2a62ec67934e572fc0f1fed3fec572f712f103e2252eb889724f781c51daff3a`;
- authored CM SHA-256
  `35a8ebff563a9d449995c02a90f1e822aa9dfeb42ec289b0128b8b1132cd8931`;
- shared embedded MAP CRC `2410032894`; and
- generated material-closure SHA-256
  `b2efa3e713313c4937e6189817bea9c2ef5bf606b3ecbf752cf7cb9ee8b5df00`.

An identical build using absolute versus relative resource-root spelling must
produce the same generated material-closure bytes. The native true-`COOP`
smoke load must spawn 940 entities with none inhibited and produce no error,
fatal or missing-resource line. Licensed overlay files and the native log stay
local; publish only their receipts.

Audit a suspect navigation pair without changing the AAS:

```powershell
python tools/campaign_port/aas_route_audit.py converted.aas48 `
  --start=-3392,-3265,184 --goal=-3592,-2952,208 --travel-flags 2
```

The auditor reads PC text planes as `normal dot point - distance`. Checkpoint
008 corrected both that convention and the exporter's opposite sign error.
On the corrected first-map AAS, the native engine resolves the diagnosed points
and emits zero AI path warnings. Static graph output still does not replace
native bounds, obstacle and gameplay validation.

For clean-room executable work, `xbe.py info`, `xrefs`, `refs`, `calls`,
`dwords` and `disasm` operate read-only. Code-inspection commands require the
optional Capstone package. Publish behavioral findings and addresses, never the
retail executable or copied disassembly.

The final native stock-DLL harness loads 940 entities in 2.825 seconds. It has
no missing selected DDS/WAV, EFX, AF-joint, script callback or copy-joint
warning. Five Xbox-only classname families cannot spawn because the stock DLL
lacks the new source classes; do not interpret that harness as source-runtime
acceptance.

## Source-DLL validation

The implementation branch contains
`.github/workflows/campaign-port-validation.yml`. It runs the 141-test Python
suite and builds the complete Win32 game DLL:

```powershell
msbuild vendor/doom3-gpl/neo/game.vcxproj /m /t:Build `
  /p:Configuration=Release /p:Platform=Win32 /v:minimal
```

Checkpoint-008 head commit `0181311c92681e09d05adfcd104d9ed9e10117f7`
passed both jobs in Actions run `38532475190`; its 116-test Python job and
complete Win32 DLL build succeeded. Artifact `11878578712` has ZIP SHA-256
`f6a237f9a43767f072145157e25e74550e2e27713a5fb96a55fbab33916bd76d`.
Its members are: `gamex86.dll`, 2,723,328 bytes, SHA-256
`5295d1ba626e319d1ee94d5d3b6483e6d4fe700716230fee8a8b33585b5341b8`;
`Game.pdb`, 17,551,360 bytes, SHA-256
`6abf58f6673ea64fe978f82cfd58a4fb04b3ee60e0ffac53b1dcb1af365204bc`;
and `gamex86.map`, 2,211,963 bytes, SHA-256
`4b24b9db4187bc542f568660db45bee5e81ed00d274350b3ee18f40f99422f9a`.
This head artifact is CI evidence and was not substituted into the native run.

The exact diagnostic DLL used for the checkpoint-008 native run came from
source commit `a60a42a07152fc77ca47f2b2de920aff85372636`, Actions run
`38531204632`, artifact `11877622996`. Verify the artifact ZIP SHA-256 as
`70d1c1b7af5655c881940eebeebd019e26014ffc23cd68a2038b41de9387aec2`
and `gamex86.dll` as
`1eb641d6869cf70bf947e4bc10208949f0a8344953bf1055ded7cf3b3ef74e34`
(2,723,328 bytes). Its PDB SHA-256 is
`499b49f822ab98700cf0f41bd5f7e752d4185355eabc5f7e03c0963478c37cb0`
and linker-map SHA-256 is
`bb6a6ddd3b99c6bab5db3dd4593bf6e383eb923d20d8ffdd28fe550cae56aef7`.
Later commits through the checkpoint head change Python tools, tests and
documentation; they do not change the runtime diagnostic code.

Doom 3's non-pure loader prefers a DLL in a PK4 over a loose DLL in the mod
directory and will overwrite the latter in `fs_savepath`. For a local
development run, place the verified test DLL beside `Doom3.exe`; that explicit
path is checked first. Preserve any pre-existing file and remove the test DLL
afterward. Never distribute the DLL together with retail-derived overlay data.

Use the generated overlay as a local mod and start an actual COOP listen server,
rather than using the single-player `map` command:

```powershell
.\Doom3.exe +set fs_game xbox_coop_port_test_v5 `
  +set com_allowConsole 1 +set logFile 2 +set r_fullscreen 0 +set r_mode 3 `
  +set s_noSound 1 +set si_pure 0 +set si_gameType COOP `
  +set si_map vv/xbox_coop/xc_mars_city1_1 `
  +set g_xboxCoopPathDiagnostics 1 +spawnServer +wait 600 +quit
```

Expected checkpoint-008 result: process exit 0; 940 entities spawned; zero
inhibited; `Server: Player joined the game.`; zero missing images, models,
animations or sounds; zero spawnclass, GUI-command or material-token failures;
zero AI path warnings; zero path-diagnostic failures; and zero `ERROR` or
`FATAL` lines. The remaining 26 warning lines are stock/global noise
(duplicate pre-existing materials, undefined `s_driver`, and no deathmatch
spawn). Verify `qconsole.log` SHA-256 as
`f3c849a836ca6964a60ffeb6358cc4268c1423ddff8ff4a64bbf831edae3b8da`,
the corrected first-map AAS48 as
`aa4448e1abca303022f6e4efa6c61ced42a0445781a522ec5385488b78821168`,
and the overlay manifest as
`f2b9787ef8ec8823022de2bf6f502d08c3ec74c2a7dc6787b5f2975f7a24889e`.
