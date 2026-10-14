# Reproduce checkpoint 005

## Source and boundary

Implementation repository: `Zippingrocks/doom3-gpl-xbox-reconstruction`.
Checkpoint implementation head: `bb2b336a036782ab861df9d20dc337fe438323d0`
on branch `campaign-port-xdvdfs-mapx`. Use an authenticated clone because the
repository is private. Preserve existing work; use an isolated worktree if the
checkout is dirty.

Python 3.10+ and the standard library are sufficient. Checkpoint 004 ran on
Python 3.11/Windows:

```powershell
python -m unittest discover -s tools/campaign_port/tests -v
```

Expected result at this checkpoint: 103 tests, zero failures. Fixtures contain
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
image names. `xact_audio.py` takes the matching XSND header, INDEXLIST, XSB and
named XWB banks plus selected logical sound names. Both write a new directory
and a manifest. Consult `--help` because bank names and ISO extent parameters
come from the source-bound inventory, not fixed public paths.

Build the local overlay after conversion:

```powershell
python tools/campaign_port/build_runtime_overlay.py `
  --map game/campaign_port_work/converted/maps/vv/xbox_coop/xc_mars_city1_1.map `
  --converted-dir game/campaign_port_work/converted/maps/vv/xbox_coop `
  --retail-root game/campaign_port_work/extracted `
  --def-root game/campaign_port_work/shared-assets/base/def `
  --stock-dir base `
  --language game/campaign_port_work/shared-assets/base/strings/english.lang `
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

