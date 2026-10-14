# Reproduce checkpoint 012

## Source and boundary

Implementation repository: `Zippingrocks/doom3-gpl-xbox-reconstruction`.
Use the open campaign-port pull request through an authenticated clone. Preserve
existing work; use an isolated worktree if the checkout is dirty.

Python 3.10+ and the standard library are sufficient. Checkpoint 012 ran on Python 3.11/Windows:

```powershell
python -m unittest discover -s tools/campaign_port/tests -v
```

Expected result on the current branch: 144 tests, zero failures. Checkpoint 012
captured 142 passing tests; two later synthetic tests cover authored-CM overlay
selection and CRC mismatch rejection. Fixtures contain no retail game data.
Tests establish decoder contracts, not campaign fidelity.

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
