# Reproduce checkpoint 007

## Source and boundary

Implementation repository: `Zippingrocks/doom3-gpl-xbox-reconstruction`.
Checkpoint implementation head: `7f35412a6cf8c238ca4ca6b91e6df3fce75ce6af`
on branch `campaign-port-xdvdfs-mapx`. Use an authenticated clone because the
repository is private. Preserve existing work; use an isolated worktree if the
checkout is dirty.

Python 3.10+ and the standard library are sufficient. Checkpoint 007 ran on
Python 3.11/Windows:

```powershell
python -m unittest discover -s tools/campaign_port/tests -v
```

Expected result at this checkpoint: 111 tests, zero failures. Fixtures contain
no retail game data. Tests establish decoder contracts, not campaign fidelity.

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

## Decode MAP.X, PROC.X and AAS.X

Run each decoder against the corresponding extracted member. Output/report paths
must not already exist.

```powershell
python tools/campaign_port/decode_map_x.py source.map.x converted.map `
  --report map-report.json
python tools/campaign_port/decode_proc_x.py source.proc.x converted.proc `
  --report proc-report.json
python tools/campaign_port/decode_aas_x.py source.aas48.x converted.aas48 `
  --report aas48-report.json

python tools/campaign_port/doom3_campaign_port.py inspect converted.proc `
  --require-decoded --report proc-inspection.json
```

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

Replace the generated AAS48 with the decoded AAS48, then use the map name
relative to `base/maps` for a bounded loader smoke check:

```powershell
.\Doom3.exe +set com_allowConsole 1 +set logfile 2 `
  +map vv/xbox_coop/xc_mars_city1_1 +wait 240 +quit
```

Checkpoint 004 expects `[Load AAS]` for the recovered AAS48, no bad-token or
out-of-date error, 940 spawned entities and a completed map shutdown. Missing
co-op entity definitions, script functions, GUIs, strings and sounds are known
runtime blockers recorded in the checkpoint receipt; they are not an AAS decode
failure. Do not distribute the generated local map products.

## Claim limits

Corpus-wide decoding proves format coverage for this exact retail image, not
completion percentage. Native `dmap` is independent geometry validation, but
its CM and shadow products are not original-Xbox equivalence. One successful
map load proves parser/runtime entry only. Direct CM.X recovery, dependency
binding, all-map loading, co-op spawns/respawns, transitions, two-peer progression
and comparison against Xbox visual/gameplay evidence remain required.

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
  --out game/campaign_port_work/overlay-xc_mars_city1_1
```

The manifest must list every callback/skeleton compatibility edit with input
and output hashes. A hidden or unrecorded manual edit invalidates the receipt.

Audit a suspect navigation pair without changing the AAS:

```powershell
python tools/campaign_port/aas_route_audit.py converted.aas48 `
  --start=-3392,-3265,184 --goal=-3592,-2952,208 --travel-flags 2
```

Checkpoint 005 finds walk-only routes for all five warned first-map NPC/path
pairs. This is static graph evidence only; dynamic door and obstacle behavior
must be retested with the reconstructed source DLL.

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
`.github/workflows/campaign-port-validation.yml`. It runs the 111-test Python
suite and builds the complete Win32 game DLL:

```powershell
msbuild vendor/doom3-gpl/neo/game.vcxproj /m /t:Build `
  /p:Configuration=Release /p:Platform=Win32 /v:minimal
```

The exact DLL used for the checkpoint-007 native run came from source commit
`243dbafe867d9c89ab48cb56e17bdc05c69ab704`, Actions run `38527277656`,
artifact `11876766170`. Verify the artifact ZIP SHA-256 as
`76e80fe9a5bbb9b3f4cf5661a0916a46f87b279ebe0ce73f03d5d87131606ed8`
and `gamex86.dll` as
`815c4a2238bb49dc52e5090913d6d216d898d0fe5d007fe9246424ae3bc6c011`.
The matching PDB and linker map hashes are recorded in the checkpoint receipt.

Doom 3's non-pure loader prefers a DLL in a PK4 over a loose DLL in the mod
directory and will overwrite the latter in `fs_savepath`. For a local
development run, place the verified test DLL beside `Doom3.exe`; that explicit
path is checked first. Preserve any pre-existing file and remove the test DLL
afterward. Never distribute the DLL together with retail-derived overlay data.

Use the generated overlay as a local mod and start an actual COOP listen server,
rather than using the single-player `map` command:

```powershell
.\Doom3.exe +set fs_game xbox_coop_port_test_v3 `
  +set com_allowConsole 1 +set logFile 2 +set r_fullscreen 0 +set r_mode 3 `
  +set s_noSound 1 +set si_pure 0 +set si_gameType COOP `
  +set si_map vv/xbox_coop/xc_mars_city1_1 `
  +spawnServer +wait 600 +quit
```

Expected checkpoint-007 result: process exit 0; 940 entities spawned; zero
inhibited; `Server: Player joined the game.`; no missing spawnclass/image,
unknown GUI command, unknown material token, `ERROR` or `FATAL` line. Verify
`qconsole.log` SHA-256 as
`618a4760af9645928c5a090195e5da08e4b36ccc5481f975f2154878f3776675`.
The five unique AI path warnings remain actionable. Static routes only prove
graph connectivity; diagnose runtime area selection, bounds, obstacles and
script timing before editing the recovered AAS.
