# Co-op bootstrap recipes and predecessor provenance

Recorded 2026-10-15 during checkpoint 085 recovery planning. This is a bounded,
read-only trace of the existing 20-map co-op build and its reusable producers.
No converter, diagnostic helper, game, Steam, dmap or xemu process was run;
no retail asset was copied or backed up. The commands below are **saved recipes
for a future isolated reconstruction**, not a claim that reconstruction passed.

Use [the recovery plan](REPRODUCIBILITY_RECOVERY_PLAN.md) for scope and acceptance.
`GAME` means the Doom 3 installation; `DEV` means
`GAME/Work files/campaign-port-dev`; `SOURCE` means
`DEV/work/upstream-doom3-gpl-src/DOOM-3-master`. Paths below are DEV-relative
unless marked GAME-relative. `NEW` denotes a fresh, explicitly selected output
workspace, not an existing accepted or rejected generation.

## What is already recoverable

The extraction, MAP/PROC/CM/AAS, model, texture, XACT and compatibility tools
already exist. The missing deliverable is a pinned, closed composition of
those stages without predecessor overlays or ambient roots, plus its successful
execution. Do not repeat format research merely because a local folder name
is not portable.

The source tooling inspected is the checkpoint 084 functional lineage through
`c61e370365ecabd826594947afcc82ec2cfb236f` (documentation successor
`3db16ab0eba778ee2f3fb4b3499d7942978e9002`). These are not inferred execution
commits for older receipts. The checkpoint 085 selector/lock metadata should
preserve explicit member selections, hashes and provenance edges; it cannot
retroactively supply an unrecorded historical tool revision.

## The exact 22-edge co-op replay chain

All 20 records in `work/coop-mergeguard-v20p-rebuild.json` resolve through the
same receipt sequence below. This was checked from the recorded input/output
overlay paths, not from version-name ordering. Arrows point from output to input:

```text
mergeguard_v20p -> v20m -> v20l -> v20k -> v20i -> v20b -> v19b
 -> v18 -> v17 -> v16 -> v15 -> v14 -> v13 -> v12 -> v11 -> v10
 -> v9 -> v7 -> soundguard_v3 -> scriptguard_v2 -> scriptguard_v1
 -> callback_v1 -> original per-map overlay
```

`v20c` through `v20g` are sibling experiments sourced from `v20b`, not required
links in this chain. Failed `v20n` and superseded `v20o` likewise must not replace
the actual `v20m` input to `v20p`.

Receipt filenames are `work/coop-mergeguard-<version>-rebuild.json`, except
v9–v14 use `-rebuild-receipt.json`. The last four are
`coop-soundguard-rebuild-v3.json`, `coop-scriptguard-rebuild-v2.json`,
`coop-scriptguard-rebuild-v1.json`, `coop-callback-rebuild-v1.json`.

The original overlay names are GAME-relative:

| Map | Original overlay |
| --- | --- |
| xc_admin | xbox_coop_port_test_admin_v5 |
| xc_alphalabs2_2 | xbox_coop_port_test_alphalabs2_2_v1 |
| xc_caverns1_1 | xbox_coop_port_test_caverns1_1_offline_v1 |
| xc_caverns2 | xbox_coop_port_test_caverns2_offline_v1 |
| xc_comm1_1 | xbox_coop_port_test_comm1_1_offline_v1 |
| xc_delta2b_1 | xbox_coop_port_test_delta2b_1_v9 |
| xc_delta2b_2 | xbox_coop_port_test_delta2b_2_offline_v3 |
| xc_delta4 | xbox_coop_port_test_delta4_offline_v2 |
| xc_delta5_1 | xbox_coop_port_test_delta5_1_offline_v2 |
| xc_enpro_1 | xbox_coop_port_test_enpro_1_v3 |
| xc_enpro_2 | xbox_coop_port_test_enpro_2_v2 |
| xc_hell1_1 | xbox_coop_port_test_hell1_1_offline_v2 |
| xc_hell1_2 | xbox_coop_port_test_hell1_2_offline_v5 |
| xc_hellhole_1 | xbox_coop_port_test_hellhole_1_offline_v3 |
| xc_mars_city1_1 | xbox_coop_port_test_v6 |
| xc_mars_city2_1 | xbox_coop_port_test_city2_v5 |
| xc_mars_city2_2 | xbox_coop_port_test_city2_2_v3 |
| xc_mcu | xbox_coop_port_test_mcu_v5 |
| xc_recycling2_1 | xbox_coop_port_test_recycling2_1_v4 |
| xc_site3_1 | xbox_coop_port_test_site3_1_offline_v3 |

Historical per-map build descriptions are in REPRODUCE checkpoints 013–033.
The chain is a provenance lookup aid, **not a requirement to rebuild 22 rounds**.
A direct fresh recipe should reconstruct the current inputs and transforms,
then compare payloads against the preserved baselines. Old manifests record
structural sources as `converted:<basename>` / `authored-cm:<basename>`;
those labels alone do not identify the exact source directory or tool revision.

## 1. Authenticate and extract the disc/archive inputs

Authoritative local metadata:

- `work/retail-xdvdfs-inventory.json`;
- `work/retail-archives/xdvdfs-extraction-manifest.json`;
- `work/shared-archives/xdvdfs-extraction-manifest.json`.

The recorded ISO is 3,029,598,208 bytes with SHA-256
`444460aab24b6df9e4cf7bd9bc442f2c95d675f44d1022f0242818813eb7d20e`.
Re-inventory the user's licensed input and fail on a different identity until
its variant is deliberately supported. No public download is provided.

For this ISO, campaign GFC/GOB archives are at the **disc root**, not `base/`.
`xdvdfs.py` matches inventory paths literally. The older
`--include 'base/xc_*.gfc'` example selects nothing on this image.

```powershell
python tools/campaign_port/xdvdfs.py inventory ORIGINAL.iso --report NEW/iso-inventory.json
python tools/campaign_port/xdvdfs.py extract ORIGINAL.iso --out NEW/retail-archives --include 'xc_*.gfc' --include 'xc_*.gob'
python tools/campaign_port/xdvdfs.py extract ORIGINAL.iso --out NEW/shared-archives --include 'assets.gfc' --include 'assets.gob' --include 'assets_english.gfc' --include 'assets_english.gob'
```

The original retail-archives extraction also selected five MP archive pairs;
the 20-map campaign selection above intentionally excludes those references.
The shared pair used below is:

| Input | SHA-256 |
| --- | --- |
| assets.gfc | 1fc9ba77a9e54589171d83d06bc14e6ae9feee10794401d6ffccff8dbb35f14f |
| assets.gob | 5c4395024835c42add37db51dfd74ca4ba3d160d81c20f106fb5294199ebc040 |
| assets_english.gfc | 2c98814c9425abe0c4a54132277acf1eab74d9b5b20f22d1690a1d8ffc1fe931 |
| assets_english.gob | 6c284e2f2f45761e0e3cfaf01fe89360fb8de17d3fad7d556ec33ffff9c7518d |

The four-input inventory does not establish that every final co-op file needs
assets_english. Determine actual demand from selected resources before claiming
a minimal raw-input set.

## 2. Reconstruct structural products, retaining all AAS classes

For each explicit map ID above, inventory its authenticated archive pair and
extract the exact structural/script members recorded by
`work/decoded-inputs-all/<map>/gfc-extraction-manifest.json`. Generic extraction
and decode entry points are already documented in REPRODUCE:

```powershell
python tools/campaign_port/gfc.py inventory NEW/retail-archives/xc_MAP.gfc --gob NEW/retail-archives/xc_MAP.gob --report NEW/inventory-xc_MAP.json
python tools/campaign_port/gfc.py extract NEW/retail-archives/xc_MAP.gfc --gob NEW/retail-archives/xc_MAP.gob --out NEW/core/xc_MAP --include './base/xbox_gen/maps/vv/xbox_coop/xc_MAP.*.x' --include './base/script/maps/vv/xbox_coop/*'
python tools/campaign_port/decode_map_x.py INPUT.map.x NEW/decoded/xc_MAP.map --report NEW/reports/xc_MAP-map.json
python tools/campaign_port/decode_proc_x.py INPUT.proc.x NEW/decoded/xc_MAP.proc --report NEW/reports/xc_MAP-proc.json
python tools/campaign_port/decode_aas_x.py INPUT.aas48.x NEW/decoded/xc_MAP.aas48 --report NEW/reports/xc_MAP-aas48.json
python tools/campaign_port/map_geometry_crc.py NEW/decoded/xc_MAP.map --report NEW/reports/xc_MAP-crc.json
python tools/campaign_port/decode_cm_x.py INPUT.cm.x NEW/decoded/xc_MAP.cm --map-crc EXACT_REPORTED_INTEGER --report NEW/reports/xc_MAP-cm.json
```

`INPUT` is the exact selected member beneath the new extraction root; replace
`xc_MAP` with one of the enumerated IDs, never a guessed archive name. Add each
other authored AAS suffix with the same decoder while preserving its suffix.
The broad original extraction also retained model CM.X files and compiled
scripts for research. A minimal structural selection does not recreate that
whole historical extraction directory; retain its full metadata separately.

Existing MAP/PROC receipts are
`work/converted-all/reports/<map>.map.map.json` and `.proc.proc.json`.
**Do not select the old converted-all AAS merely by directory name.** The
corrected `work/converted-aas-x-v2-plane-distance/maps/vv/xbox_coop` contains
20 AAS48 and six AAS96 files. All 26 hashes were checked against final v20p
manifest records during this trace and matched. The current decoder negates
packed plane `d` for PC text distance; an older syntactically valid output can
retain the wrong sign.

Four more AAS files come from the shared assets pair, not the map archive:

| Exact member beneath `./base/xbox_gen/maps/vv/xbox_coop/` | Existing extraction/decoder evidence |
| --- | --- |
| xc_recycling2_1.aas_mancubus.x | `work/checkpoint-022-recycling2-1/aas-mancubus-raw/gfc-extraction-manifest.json`; `reports/aas-mancubus-decode.json` in that checkpoint |
| xc_hell1_2.aas_guardian.x | `work/coop-special-aas-raw/extraction-manifest.json`; checkpoint 049 recipe |
| xc_hell1_2.aas_mancubus.x | same |
| xc_hellhole_1.aas_cyberdemon.x | same |

Extract each with `gfc.py extract assets.gfc --gob assets.gob --include
EXACT_MEMBER` into a new root, then run `decode_aas_x.py` preserving its class.
Require the exact 30-file identity set, not only an AAS48 count. CM geometry CRC
is computable offline; historical dmap comparison commands are not required
and are not authorized by this recipe.

## 3. Shared declarations, source scripts, models and AFs

`work/shared-assets-extracted/gfc-extraction-manifest.json` selects 137 files:
all 131 `./base/def/*` members plus these six exact members:

```text
./base/particles/coop.prt
./base/skins/skins_player_xbox_coop.skin
./base/strings/english.lang
./base/strings/english_vv.lang
./base/strings/english_vv_live.lang
./base/strings/english_vv_popup.lang
```

Pass those selectors as repeated `--include` arguments to `gfc.py extract` on
the authenticated assets pair into `NEW/shared-assets-extracted`. Do not widen
the particle/skin selectors: that archive contains 34 particle and 28 skin
members, not just the two selected above.

The apparently substantial NPC/player runtime roots are each one original AF
extraction, not missing skeletal converters:

| Root | Exact shared member | SHA-256 |
| --- | --- | --- |
| work/npc-runtime-assets | ./base/af/char_npc_base.af | 5c893304b9cfb079e465eafc85a78450787b2a4fec5766feffd49b49c628ee70 |
| work/player-runtime-assets | ./base/af/player_npcs.af | ae9beb8611b98aec22143aec3b7d7e9523a5e6be2b71eaf5e7e614d5767fdd42 |

Each has `extraction-manifest.json`. Use the same `gfc.py extract` recipe with
one exact member and a distinct new output directory. Checkpoint 084 also adds
`monster_zombie_maint.af`, `monster_zombie_chainsaw.af`, and `char_lanternguy.af`
to `work/checkpoint-084-af-assets`; exact commands/hashes are in REPRODUCE 084.
`char_npc_misc.af` in its separate Enpro root is needed by the solo repair; do
not silently infer that the co-op driver selects that root.

Map-local GUI/source-script selections are recoverable from
`work/runtime-deps-all/<map>/gfc-extraction-manifest.json` and the first-map
`work/runtime-deps-xc_mars_city1_1/gfc-extraction-manifest.json`. Reproduce exact
member lists, not a guessed extension-wide closure. For example, Admin's
selection contains 44 GUI and 30 script files. Compiled `.script.bin` inputs
are analysis evidence, not scripts to copy into a PC runtime root.

Model conversion producers are already supported:

```powershell
python tools/campaign_port/decode_model_corpus.py NEW/retail-archives/xc_MAP.gfc --gob NEW/retail-archives/xc_MAP.gob --out NEW/models/xc_MAP
```

The wrapper selects `.mdvmesh`, `.mdvanim`, `.md5anim.x`, preserves raw/decode
hashes and maps them to MD5 paths. Its runtime root is the produced `decoded/base`,
not the wrapper's top-level directory. Historical first-map output
`work/decoded-mdv-xc_mars_city1_1-v2/base` has per-output `.json` decoder receipts.
Later per-map model roots live under checkpoints 014–033. MCU's 410-member
selection and model mappings are documented in REPRODUCE 018.

The current replay additionally appends sorted
`work/solo-structural/maps/*/models/decoded/base` roots. This is an actual
cross-corpus dependency, not proof that all 41 solo model archives are minimally
required for co-op. Resolve each final selected resource and preserve exact root
order before reducing it. Do not treat a prior overlay or this glob as an
unexplained terminal source.

## 4. Compiled static models

Each directory below has `gfc-extraction-manifest.json` binding its members to
the correspondingly named co-op archive pair. Extract the exact members with
`gfc.py`; the current overlay builder performs the guarded static-model-X to
ASE conversion and records `decode-xbox-static-model-x-to-pc-ase` transforms.

| Root under work/static-model-x-v1 | Member paths below base/xbox_gen/models/ |
| --- | --- |
| xc_comm1_1 | items/keycard/keycard2.lwo.x |
| xc_caverns1_1 | mapobjects/caves/caves1_6b.ase.x; mapobjects/xbox_coop/xc_caves1_6.ase.x |
| xc_caverns1_1-keycard | items/keycard/keycard2.lwo.x, from xc_caverns1_1 archive |
| xc_site3_1 | mapobjects/hell/site3/stoneroom/blobfingers_vv.lwo.x; mapobjects/hell/site3/archviletemple/mouth_vv.lwo.x |
| xc_hellhole_1 | mapobjects/hellhole/hellhole_cyb_chop3.lwo.x; hellhole_firstroom_halfa.lwo.x; hellhole_firstroom_cordsa.lwo.x in the same directory |
| xc_recycling2_1 | mapobjects/recycle/recycwallight.ase.x |

This is ten member selections across six roots, including the repeated keycard
path from two archive pairs. It is not a promise that every selected source is
emitted by every map. The available unbroken Recycling light does not recover
the source-absent `recycwallight_broken.ase`.

## 5. XACT and D3TFULL roots

The same pinned ISO inventory records:

| Member | Byte offset | Extent bytes |
| --- | ---: | ---: |
| base/soundbanks/global.xwb | 736684032 | 257450496 |
| base/xbox_gen/global.d3tfull | 2825555968 | 178959016 |

Global XWB is sector 359709 times the recorded 2048-byte sector size. These
numbers are specific to the identified ISO, not universal Doom 3 offsets.

Audio metadata producers and receipts already exist:

- `work/sound-metadata/gfc-extraction-manifest.json`: shared
  `./base/sound/global.xsndshd`, SHA-256
  `994c5f859a41558f2c8c28371c73770d6cf56301020ab09f8431b006b828f7ba`;
- `work/solo-sound-indexlists/extraction-manifest.json`: shared INDEXLIST members;
- `work/solo-soundbanks/xdvdfs-extraction-manifest.json`: disc
  `base/soundbanks/*.xsb` members;
- each selected recovery root's `xact-audio-manifest.json`: logical names,
  bank/cue/wave indices and output WAV hashes.

For one selected logical name, the existing command interface is:

```powershell
python tools/campaign_port/xact_audio.py --xsndshd NEW/sound-metadata/base/sound/global.xsndshd --indexlist NEW/indexlists/base/sound/xc_MAP.indexlist --xsb NEW/soundbanks/base/soundbanks/xc_MAP.xsb --bank 'global|ORIGINAL.iso|736684032|257450496' --name EXACT_LOGICAL_NAME --output NEW/audio/xc_MAP
```

Repeat `--name` for the exact selected set. This positional bank specification
is `NAME|PATH|OFFSET|SIZE`, not a path to the whole disc used as an unbounded bank.
Validate every requested name's recorded bank before using only `global`.
`recover_solo_audio_corpus.py` already wraps recovery for an authenticated,
closed solo-audio audit; it is not a co-op audit adapter.

The replay's ordered audio roots are `xact-first-map`,
`solo-xact-audio/admin`, `solo-xact-audio/caverns1_1`, checkpoint 019–033's
selected XACT directories, then `xact-coop-xc_mars_city2_1-direct`,
`xact-coop-xc_mars_city2_2-direct`, `xact-coop-xc_mcu-direct`.
Their exact directory spellings and ordering are in
`tools/campaign_port/rebuild_latest_coop_overlays.py`; preserve that list as
metadata, not a discovery wildcard. The three direct roots use the shared
XSND, corresponding co-op INDEXLIST and corresponding disc XSB.

Important historical gap: `xact-audio-manifest.json` stores paths to XSND,
INDEXLIST and XSB but not their hashes, and omits the wave-bank path, extent,
hash and tool revision. Those inputs can be bound now using their extraction
receipts and the ISO inventory, but a new binding is not proof of an older
execution's unrecorded environment.

For HUD textures, the exact command/names are in REPRODUCE's runtime-asset
section. `work/d3t-hud-missing-v3-dxt5/d3t-extraction-manifest.json` records the
six requested images and current expected DDS hashes. Preserve v3's format
handling: older same-named texture roots are not automatically interchangeable.
`work/d3t-hud/d3t-extraction-manifest.json` is the other common HUD selector.

## 6. Cyberdemon compatibility retargets

Three 50-joint source clips are present byte-identically in both
`work/checkpoint-032-hellhole-1/decoded-models/base/models/md5/monsters/cyberdemon`
and `work/solo-structural/maps/hellhole_1/models/decoded/base/models/md5/monsters/cyberdemon`.
The solo model-corpus manifest explicitly binds each `.mdvanim` to its decoded
`.md5anim`. The three recorded source/output hashes are:

| Clip | Decoded source SHA-256 | Retargeted output SHA-256 |
| --- | --- | --- |
| walkheadpain | ada4323f4da358e385d5da9ced6e357745cf7d0ca1462564e9a06c35bdd06d84 | 26a125db30a68b50ea56e41c47b839a7b1bcf250b14d6b90296d0f6a908e160a |
| walkleftarmpain | 7fc2400565a8cf39ca09234eb3121ad8084a87a13d684e9b18bf9ea49173c9c3 | d31aac88ce61273451db66550653c96c2196dfcdee76d8737ee9aea0ddeea532 |
| walkrightarmpain | b59591513304d3c6b2ae37b4bf153ccb0c5f1033f9a1d0acf6f52f870bcbc536 | bd7bd181faf00b284e2ad925862b54199f4a4dc8c1f5a723c2707d4521da5ce4 |

The 78-joint target mesh is PC
`pak002.pk4:models/md5/monsters/cyberdemon/cyberdemon.md5mesh`, 502,099 bytes,
SHA-256 `701328590a7b324a386bcdf0357be86943fbcf754c0641c1d4702e6c6a269177`.
Read-only ZIP membership/hash inspection found that exact member only in
pak002 among the current `base/*.pk4`; the local extracted target hash agrees.
Pin the PC package identity and edition separately; an identical member name
in another installation is not sufficient.

The existing producer interface is:

```powershell
python tools/campaign_port/retarget_md5anim.py DECODED_CLIP.md5anim --target-mesh AUTHENTICATED_PC_CYBERDEMON.md5mesh --allow-target-expansion --out NEW/retargeted/base/models/md5/monsters/cyberdemon/CLIP.md5anim --report NEW/reports/CLIP-retarget.json
```

The expansion flag is required by the recorded 50-to-78-joint operation. This
recipe is reconstructed from the source interface and input/output receipts;
it was not re-executed here. The three 41-frame receipts are:

- `work/checkpoint-069-hellhole1-pc-cyber/walkheadpain-retarget.json`, SHA-256
  `36f9a28296afef26d4cfac239e8e7d27d26ecef4e942784c05171da8027034f1`;
- `work/checkpoint-071-hellhole1-pc-cyber-pain/walkleftarmpain-retarget.json`,
  `d7c377409e52df529406fda15cae898aa888ed9afc5f88d6e740bd53272ecf6e`;
- the same directory's `walkrightarmpain-retarget.json`,
  `80f40c0eddabe0dfce0bdaf98be016018b2f44b088a3d3aec94588cc178c2102`.

They bind source, target and output hashes, but do not record the historical
producer commit or command. Preserve this limitation until history establishes
it. These retargets are not raw Xbox decode outputs and do not establish visual
or animation-event acceptance.

## 7. Replay ordering and remaining composition work

The v20p invocation is documented in REPRODUCE 084 with explicit
`--input-suffix mergeguard_v20m --suffix mergeguard_v20p --require-maps 20`.
The inspected checkpoint-084 driver discovered identities through latest-manifest
scanning. Checkpoint 085 fixes explicit-suffix replay to discover those inputs
deterministically. A new bootstrap must still enumerate the exact 20-map set and record ordered roots;
count-only selection and modification-time discovery are insufficient.

Important precedence in the inspected driver:

- authored checkpoint-084 AF roots and per-map static inputs precede prior
  overlays; most other shared roots follow the prior overlay;
- Caverns 1's separate keycard root is inserted before its ordinary static root;
- Delta 2b part 2's checkpoint-024 decoded source root precedes the prior overlay
  to avoid its contaminated public 63-joint ZCT family;
- Hellhole's two Cyberdemon retarget roots precede raw 50-joint model roots;
  its source-bound ending models and solo source resources also precede the
  generic list;
- sorted solo decoded model roots are appended, and stock PC PK4 lookup is a
  separate fallback with its own precedence.

Known remaining work, not missing decoder algorithms:

1. Join each final resource to the exact original archive/member or PC package;
   follow inherited/derived aliases and generated scripts, not only copied files.
2. Recover missing historical producer revisions/arguments where possible and
   label them unresolved elsewhere. Current tool hashes are not past-execution
   proof.
3. Replace all predecessor inputs and ambient glob/mtime discovery with explicit
   selectors, logical root IDs, versioned recipes and fail-closed preflight.
4. Bind audio/texture archive extents, PC package precedence, complete profile
   hashes and all cross-corpus source choices; do not flatten resource folders.
5. Execute a fresh isolated offline build only after the user-approved scope
   allows it, compare payload hashes, and retain mismatches as failures. This
   document does not complete final v20p package/tree acceptance or gameplay.

## Publication boundary

Do not upload the original local manifests wholesale. Older GFC receipts
contain `trailer_hex`; newer receipts contain `entry.name_record_hex`, including
raw fixed-length archive records. Inventory files can contain additional
`tail_hex`/raw spans. Public preservation must use an allowlist of paths,
identifiers, offsets, lengths, hashes and selected numerical metadata, removing
raw byte/text fields and private absolute paths. The original receipt hash may
be preserved to bind the sanitized record to its local source.

The nine diagnostic **source** snapshots under source
`docs/checkpoint-084-diagnostics` are a separate, inspected non-game-code archive.
Their preservation does not authorize their execution or publication of dumps,
raw logs, PDBs, decoded assets or helper output. No exhaustive local backup or
clean-machine reproducibility claim is made.
