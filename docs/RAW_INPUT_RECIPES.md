# Raw-input recipes and the verified solo replay chain

Checkpoint 085, 2026-10-15. This document records CLI contracts, source identities,
existing recipes and unresolved orchestration. **No cold-start reconstruction,
game launch, asset extraction, game-file backup or cloud upload was performed
to prepare it.** The current work preserves non-game material and metadata only.

Use this with [the recovery plan](REPRODUCIBILITY_RECOVERY_PLAN.md) and
[checkpoint 084's stop state](CHECKPOINT_084_HANDOFF.md). Checkpoint 085's
metadata-only `recovery_metadata.py` workflow produces
[recovery selectors](../evidence/checkpoint-085-recovery-selectors.json) and the
[recovery lock](../evidence/checkpoint-085-recovery-lock.json). Those outputs
preserve selected identities, original member spelling, hashes, offsets and
manifest relationships; they are not extracted game data or proof that the
recipes have been executed on a clean machine. Read their status and limits.

## Paths, versions and safe use of the templates

- `GAME`: the existing Doom 3 installation directory.
- `DEV`: `GAME/Work files/campaign-port-dev`.
- `SOURCE`: `DEV/work/upstream-doom3-gpl-src/DOOM-3-master`.
- Paths beginning `work/` below are DEV-relative unless stated otherwise.
- `tools/campaign_port/...` commands are shown relative to a pinned SOURCE
  checkout. The historical DEV mirror is not an independent authority.

Every angle-bracket argument below is a **substitution placeholder**, not a
literal filename. Select it from the metadata lock or an explicitly recorded
input root. Output directories and report paths must be new. These are stage
templates, not a verified runnable full-pipeline script. Do not run them as
part of metadata-only preservation, and do not overwrite the existing work.

Solo v40 was built at source `a23d1a9062abfc4fe5a1cfcd57ecd83c572fd5c8`;
v39's documented implementation is `2869789962b2b02f8809bd1beb59d33245e89715`.
The later functional baseline `c61e370365ecabd826594947afcc82ec2cfb236f`
includes the Guardian receipt and Lantern demand fixes. Preservation commit
`3db16ab0eba778ee2f3fb4b3499d7942978e9002` did not rebuild these artifacts.
Do not attribute every historical receipt to the current checkout.

## 1. Original disc and the exact 41 solo identities

The source identity recorded by checkpoint 034 is:

| Item | Recorded identity |
| --- | --- |
| ISO bytes | `3029598208` |
| ISO SHA-256 | `444460aab24b6df9e4cf7bd9bc442f2c95d675f44d1022f0242818813eb7d20e` |
| Solo archive set | 41 GFC/GOB pairs, 82 files, `445404264` bytes |
| Solo disc-extraction manifest SHA-256 | `ef634d3507d04d0b202c01baf4b9362ea389687ea562760093b6bf9c2cce48b4` |

The manifest exists at
`work/solo-retail-archives/xdvdfs-extraction-manifest.json`; the same bytes were
also saved as `work/solo-retail-extraction-console.json`. Original solo pairs
are `work/solo-retail-archives/<MAP_ID>.gfc` and `.gob`. Do not substitute the
co-op/MP `work/retail-archives` directory merely because its name is similar.

The map set is already public in
[checkpoint 034](../evidence/checkpoint-034-solo-structural.json):

```text
admin alphalabs1_1 alphalabs1_2 alphalabs2_1 alphalabs2_2 alphalabs3
caverns1_1 caverns1_2 caverns2 comm1_1 comm1_2 commoutside_1 commoutside_2
cpu_1 cpu_2 delta1_1 delta1_2 delta2a_2 delta2b_2 delta3_1 delta3_2
delta4 delta5_1 enpro_1 enpro_2 hell1_1 hell1_2 hell1_3 hellhole_1
hellhole_2 mars_city1_1 mars_city2_1 mars_city2_2 mcu_1 mcu_2
monorail_1 monorail_2 recycling1_1 recycling2_1 recycling2_2 site3_1
```

The pinned ISO places these archive members at its root, for example
`admin.gfc`, not `base/admin.gfc`. Inventory the legitimate input, verify its
identity and use the exact manifest member names:

```powershell
python -B tools/campaign_port/xdvdfs.py inventory '<ISO>' --report '<NEW_ISO_INVENTORY>'
python -B tools/campaign_port/xdvdfs.py extract '<ISO>' --out '<NEW_SOLO_ARCHIVES>' --include '<MAP_ID>.gfc' --include '<MAP_ID>.gob'
```

The second command is a **single-pair template**. A corpus invocation needs
all 82 exact `--include` arguments from the locked solo set. Exclude `xc_*`,
`d3dm*`, `assets*` and `pda_vv` from that solo set. Verify identities, not just
the number of selected files. Source edition or language changes require a
different authenticated inventory, not reuse of these offsets/hashes.

## 2. GFC selection and compiled map conversion

Existing per-map metadata is under:

```text
work/solo-structural/<MAP_ID>-inventory.json
work/solo-structural/maps/<MAP_ID>/core/extraction-manifest.json
work/solo-structural/maps/<MAP_ID>/resources/extraction-manifest.json
work/solo-structural/maps/<MAP_ID>/reports/{map,map-crc,proc,cm,aas*}.json
```

`doom3_campaign_port.py extract` matches `--include` against the original
`entry.name`, with backslashes normalized to `/`, **before** `safe_name`
removes a leading `./`. Consequently, an original member such as
`./base/xbox_gen/maps/vv/admin.map.x` must not silently become the selector
`base/xbox_gen/maps/vv/admin.map.x`. The metadata workflow retains both the
original member name and safe output path. Generate exact selectors from
`files[].entry.name`, not only `files[].path`.

```powershell
python -B tools/campaign_port/doom3_campaign_port.py inventory '<GFC>' --gob '<GOB>' --report '<NEW_ARCHIVE_INVENTORY>'
python -B tools/campaign_port/doom3_campaign_port.py extract '<GFC>' --gob '<GOB>' --out '<NEW_CORE>' --include '<EXACT_ORIGINAL_MEMBER>'
```

Repeat `--include` for every locked core member. Perform the same operation
with the separate locked resource-member selection into `<NEW_RESOURCES>`.
The original exact command lines are not present in every extraction receipt;
the recorded member set and hashes constrain a reproducible replacement.
Do not replace that selection with an unexplained wholesale archive copy.

For example, Admin's core receipt records these eight safe output paths:

```text
base/xbox_gen/maps/vv/admin.map.x
base/xbox_gen/maps/vv/admin.proc.x
base/xbox_gen/maps/vv/admin.cm.x
base/xbox_gen/maps/vv/admin.aas48.x
base/xbox_gen/maps/vv/admin.aas96.x
base/script/maps/vv/admin_main.script
base/script/map_admin.script
base/xbox_gen/script/maps/vv/admin_main.script.bin
```

Keep both plaintext script forms and the compiled-script witness when present.
Do not assume every archive has Admin's names or only one AAS class.

The original decoded map layout is
`work/solo-structural/maps/<MAP_ID>/decoded/maps/vv/`. Reconstruct the compiled
products independently:

```powershell
python -B tools/campaign_port/decode_map_x.py '<CORE>/<MAP_MEMBER>.map.x' '<NEW_DECODED>/maps/vv/<MAP_ID>.map' --report '<NEW_REPORTS>/map.json'
python -B tools/campaign_port/map_geometry_crc.py '<NEW_DECODED>/maps/vv/<MAP_ID>.map' --report '<NEW_REPORTS>/map-crc.json'
python -B tools/campaign_port/decode_proc_x.py '<CORE>/<MAP_MEMBER>.proc.x' '<NEW_DECODED>/maps/vv/<MAP_ID>.proc' --report '<NEW_REPORTS>/proc.json'
python -B tools/campaign_port/decode_cm_x.py '<CORE>/<MAP_MEMBER>.cm.x' '<NEW_DECODED>/maps/vv/<MAP_ID>.cm' --map-crc '<COMPUTED_MAP_CRC>' --report '<NEW_REPORTS>/cm.json'
python -B tools/campaign_port/decode_aas_x.py '<CORE>/<EXACT_AAS_MEMBER>.x' '<NEW_DECODED>/maps/vv/<MAP_ID>.<AAS_CLASS>' --report '<NEW_REPORTS>/<AAS_CLASS>.json'
```

`<MAP_MEMBER>` includes the safe member directory, normally
`base/xbox_gen/maps/vv/<MAP_ID>`. `<AAS_CLASS>` includes the complete authored
suffix, for example `aas48` or `aas96`; enumerate every selected AAS member.
Read `<COMPUTED_MAP_CRC>` from the newly generated MAP CRC report, never a
neighboring map or an arbitrarily edited AAS header. No dmap/engine launch is
required for this calculation. Retain the Comm Outside 1 AAS96 mismatch as a
known source discrepancy, not a reason to stamp its checksum.

Checkpoint 034 recorded 296 core records, 178 decoded outputs and zero
rehash/MAP-CM binding failures. A checkpoint-085 metadata comparison also
confirmed that all 41 v40 `source_map_sha256` values equal their corresponding
original `reports/map.json` output hashes. This links source identity; it does
not prove that all current output MAP bytes are unchanged or gameplay-correct.

## 3. Models, portable resources and the first strict overlay

The complete per-archive model corpus has a supported executable wrapper:

```powershell
python -B tools/campaign_port/decode_model_corpus.py '<GFC>' --gob '<GOB>' --out '<NEW_MODELS>'
```

It selects `.mdvanim`, `.mdvmesh` and `.md5anim.x`, validates extracted hashes,
then creates `raw/`, `decoded/` and `model-corpus-manifest.json` under the new
root. Preserve the source-to-output hashes and decoder identity. Historical
model receipts are
`work/solo-structural/maps/<MAP_ID>/models/model-corpus-manifest.json`.
[Checkpoint 035](../evidence/checkpoint-035-solo-models.json) records 18,405
converted model/animation records across 41 maps.

Other existing producers must be bound to exact selections and versions:

- Shared text/DEF/language/AF extraction: `gfc.py` or the existing strict GFC
  extractor, using original archive/member identities. Current AF commands
  and member hashes are in [checkpoint 084's recipe](REPRODUCE.md#checkpoint-084-offline-only-corpus-review).
- Static-model roots named `static-model-x-*` contain extracted compiled
  `.lwo.x` inputs, not already decoded ASEs. `build_runtime_overlay.py` calls
  `decode_static_model_x.py` for the source-bound private ASE routes.
- Textures: `d3tfull.py` with source-bound logical names and bounded disc
  extents. Audio: `xact_audio.py`, or `recover_solo_audio_corpus.py` from a
  closed solo audio audit, with exact XSND/INDEXLIST/XSB/XWB inputs and extents.
- Shared actor and earlier runtime-dependency roots: trace their extraction
  and conversion manifests; a directory name alone is not a producer recipe.

[The runtime-asset section](REPRODUCE.md#runtime-asset-conversion-and-overlay)
documents these CLI entry points. Checkpoint 037 documents the audio audit and
recovery contract. Neither is an already-verified all-input cold-start driver.

[Checkpoint 036](REPRODUCE.md#checkpoint-036-strict-solo-overlay-corpus)
describes the first strict solo build: per-map decoded MAP/companions, portable
model/resource roots, shared player/NPC/HUD/material roots, shared DEFs, stock
PC `base`, two language catalogs, `--def-preference info.def`, and direct
`--authored-cm`. A single-map invocation has this shape:

```powershell
python -B tools/campaign_port/build_runtime_overlay.py --map '<DECODED>/maps/vv/<MAP_ID>.map' --converted-dir '<DECODED>/maps/vv' --retail-root '<ORDERED_ROOT_1>' --retail-root '<ORDERED_ROOT_2>' --def-root '<SHARED_DEF_ROOT>' --stock-dir '<PC_BASE>' --language '<ENGLISH_LANG>' --language '<ENGLISH_VV_LANG>' --def-preference info.def --authored-cm '<DECODED>/maps/vv/<MAP_ID>.cm' --out '<NEW_OVERLAY>'
```

This intentionally omits unspecified roots/profile/class/material arguments:
recover their complete per-map values before execution. Do not enable
`--allow-unresolved` to make the incomplete template appear successful.
The exact early strict/nativefix orchestration is still a reconstruction gap.

## 4. Verified replay predecessors and profile rebinding

All 41 maps follow the same **receipt-confirmed** chain:

```text
nativefix-v12 -> v17 -> v18 -> v20 -> v26 -> v32 -> v36 -> v39 -> v40
```

The corresponding DEV-relative receipts are:

| Edge | Receipt |
| --- | --- |
| v12 -> v17 | `work/solo-overlays-nativefix-v17-receipt.json` |
| v17 -> v18 | `work/solo-overlays-nativefix-v18-rebuild.json` |
| v18 -> v20 | `work/solo-overlays-nativefix-v20-rebuild.json` |
| v20 -> v26 | `work/solo-overlays-nativefix-v26-rebuild.json` |
| v26 -> v32 | `work/solo-overlays-nativefix-v32-rebuild.json` |
| v32 -> v36 | `work/solo-overlays-nativefix-v36-rebuild.json` |
| v36 -> v39 | `work/solo-overlays-nativefix-v39-rebuild.json` |
| v39 -> v40 | `work/solo-overlays-nativefix-v40-rebuild.json` |

There are rejected/alternate generations between these numbers; do not infer
that numerical adjacency means ancestry. No earlier replay receipt was found
in the bounded top-level inventory. The `v12 -> earlier strict/raw` connection
must therefore remain unresolved at the exact-command level. The separate
`solo-overlays-packaged-v1-receipt.json` does prove packaging from strict-v11,
but does not prove that packaged-v1 produced nativefix-v12.

The final two historical replay invocations are documented as:

```powershell
python -B tools/campaign_port/rebuild_latest_solo_overlays.py '<V36_ROOT>' '<NEW_V39_ROOT>' --work-root '<WORK_ROOT>' --stock-dir '<PC_BASE>' --require-maps 41 --receipt '<NEW_V39_REBUILD_RECEIPT>'
python -B tools/campaign_port/rebuild_latest_solo_overlays.py '<V39_ROOT>' '<NEW_V40_ROOT>' --work-root '<WORK_ROOT>' --stock-dir '<PC_BASE>' --require-maps 41 --receipt '<NEW_V40_REBUILD_RECEIPT>'
```

Pin each producer revision and its profiles before reproducing an old result.
Executing current code with old path names does not recreate the old revision.
These incremental commands require prior overlays and all selected recovered
roots; they do not replace stages 1-3.

### The twelve absolute predecessor profile paths

The v39 manifests contain 12 distinct absolute paths under the former prefix:

```text
C:/Program Files (x86)/Steam/steamapps/common/Doom 3/Work files/campaign-port-dev/tools/campaign_port/profiles/
```

Map each basename to `SOURCE/tools/campaign_port/profiles/<basename>`. The
table gives the historical v39 hash, not an instruction to silently use a
different current file. The metadata lock retains the owning maps and paths.

| Profile basename | Recorded SHA-256 | Map consumers |
| --- | --- | --- |
| `xbox_solo_admin_pinky_cinematic.resources` | `145b19847c7aa6022ea41a5113431f001993cf2758a912b7a6e794dc4f1466a3` | admin |
| `xbox_solo_alphalabs2_lantern.resources` | `905ca65cf179d2062b64ba157c77b88e9d07e56942a1f776e48a647f7af56e55` | alphalabs2_2 |
| `xbox_solo_cpu1_campbell.resources` | `60b7084f1c3d741bc29cf57da337383fddcde4bff25317b94a62903a65129c43` | cpu_1 |
| `xbox_solo_cyberdemon.resources` | `ce7d5c729cf9f6c910a39550ff19eeb0878ae1fdc82d0e40a2b89d2b47f83690` | hellhole_1 |
| `xbox_solo_delta1_scipull.resources` | `48593ffcf39821be0cd03b0b81aa4ab267249a330f3520528baf9c0822b892f5` | delta1_1 |
| `xbox_solo_delta4_hazmat.resources` | `f5d0d6ec0580c5321764a69c0e2772828158d87e3d1cb2b899cedd3706960ebe` | delta4 |
| `xbox_solo_pinky.resources` | `2c741628591ce1e03b5a8bac2c8216463d42f5f96281bad085a5140be1c4dc97` | admin, commoutside_2, delta1_1, delta1_2, recycling1_1 |
| `xbox_solo_recycling1_revintro.resources` | `9bd5961253d5fd153ae8a5837d6d860d32189492d7152ef26ecff6da35c8ec62` | recycling1_1 |
| `xbox_solo_vagary.resources` | `b1b8f42fed556a0b26b754f63c866f172d2e092d690c1b0ecf8bbfc121315f14` | alphalabs3, caverns2 |
| `xbox_solo_zct.resources` | `f8b068e4721b5cb7c903265ecd1d106034b0f26a2e0445830b765bab5aa90f21` | alphalabs3, cpu_1, delta1_1, delta1_2, delta2a_2, delta2b_2, delta3_1, delta3_2, delta5_1, monorail_1, monorail_2 |
| `xbox_solo_zjump.resources` | `08c25e516677ca01919bd5721e783a6ee5eea300e59a93ba3bbfcce64729adfb` | admin, alphalabs2_1, commoutside_1, delta2a_2, monorail_2 |
| `xc_delta2b_1.resources` | `ec32b29b58146b15784c47096b677b95c1836a025ec62025b37bacd7578f4883` | cpu_1, delta1_1, delta1_2, delta2b_2, delta3_1, delta3_2, delta5_1, monorail_1, monorail_2 |

Eleven hashes matched the tracked files during inspection. Lantern intentionally
changed for checkpoint 084; its corrected profile hash is
`6ee107d1145e5608604eadf5f1422a80484133e2e7e277a4b753a11dfe4f6699`.
AlphaLabs2_2's v39 manifest records the same old path twice. Deduplicate input
paths without destroying historical records. A portable driver must distinguish
an explicit pinned-profile migration from corruption; blanket equality to the
predecessor profile hash would reject the intended v40 correction.

## 5. Concrete Cyberdemon retarget recipe

Three replay dependencies have exact source/target/output witnesses, so their
recipe need not remain an unexplained directory copy. All source clips are in:

```text
work/solo-structural/maps/hellhole_1/models/decoded/base/models/md5/monsters/cyberdemon/
```

The target is the licensed PC `base/pak002.pk4` member
`models/md5/monsters/cyberdemon/cyberdemon.md5mesh`, independently rehashed as
`701328590a7b324a386bcdf0357be86943fbcf754c0641c1d4702e6c6a269177`.
The existing local extracted target under
`work/checkpoint-069-hellhole1-pc-cyber/base/` has that same hash. A future
clean reconstruction must obtain that exact member through a source-bound,
single-member step, not assume the existing extracted copy or a mod override.

| Clip | Source SHA-256 | Recorded output SHA-256 |
| --- | --- | --- |
| `walkheadpain.md5anim` | `ada4323f4da358e385d5da9ced6e357745cf7d0ca1462564e9a06c35bdd06d84` | `26a125db30a68b50ea56e41c47b839a7b1bcf250b14d6b90296d0f6a908e160a` |
| `walkleftarmpain.md5anim` | `7fc2400565a8cf39ca09234eb3121ad8084a87a13d684e9b18bf9ea49173c9c3` | `d31aac88ce61273451db66550653c96c2196dfcdee76d8737ee9aea0ddeea532` |
| `walkrightarmpain.md5anim` | `b59591513304d3c6b2ae37b4bf153ccb0c5f1033f9a1d0acf6f52f870bcbc536` | `bd7bd181faf00b284e2ad925862b54199f4a4dc8c1f5a723c2707d4521da5ce4` |

The three reports record 41 frames, source 50 joints, target 78 joints, and
restoration of missing target joints using target bind-local transforms. The
matching CLI option is explicit:

```powershell
python -B tools/campaign_port/retarget_md5anim.py '<SOURCE_CLIP>' --target-mesh '<AUTHENTICATED_PC_MESH_FILE>' --allow-target-expansion --out '<NEW_RETARGETED_CLIP>' --report '<NEW_RETARGET_REPORT>'
```

Existing witnesses are:

- `work/checkpoint-069-hellhole1-pc-cyber/walkheadpain-retarget.json`
- `work/checkpoint-071-hellhole1-pc-cyber-pain/walkleftarmpain-retarget.json`
- `work/checkpoint-071-hellhole1-pc-cyber-pain/walkrightarmpain-retarget.json`

The derived outputs live under the corresponding `retargeted/base/` roots.
Their lookup priority before raw 50-joint clips is semantic. Source/target
hashes were checked during this trace, but the retargeter was **not rerun**;
the historical producer revision still needs to be pinned and a future
reproduction must compare the recorded output hashes, not assume equality.

## 6. What is preserved, and what is still missing

The metadata workflow may preserve projections of extraction/model/decode
manifests, replay/package/tree receipts, input and output hashes, member names,
offsets, counts and selected transform metadata. It must not copy game files,
extracted scripts, raw logs/captures, minidumps or arbitrary JSON text fields.
Original inventories can include raw filename-record hex and large parsed
structures; their `.json` extension alone is not a publication allowlist.

Concrete remaining gaps:

1. The complete earlier strict/nativefix production arguments and ordered
   resource roots, especially the exact predecessor of nativefix-v12. The
   original MAP hash links are intact; an unrecorded command must remain an
   explicit unresolved recipe, not a guessed ancestry edge.
2. Exact producer revisions/options for every shared actor, portable resource,
   D3TFULL, XACT and manually prepared derivative root. Preserve source-bound
   member selections and reconstruct only missing orchestration.
3. A complete portable input lock/preflight and stage runner that rejects
   missing or mismatched inputs without relying on old overlays, current
   directory, absolute profile paths, timestamps or ambient mods. Checkpoint
   085 metadata capture is evidence toward this, not a completed cold-start
   converter.
4. Source-bound stock fallback selection. The installed `base` includes custom
   Xbox map-pack PK4s, so record exact PK4 hashes and ordering; do not call
   that entire directory pristine stock or silently discard mod contributions.
5. A future isolated raw-input run across all 61 identities with payload-ledger
   comparison. No such run occurred here. Reproducibility of known defects is
   separate from fixing them and from final gameplay/two-peer acceptance.

Finish the already-built co-op v20p offline audit/package/tree gates independently
as described in the stop handoff. Do not let these recipe templates imply that
those missing acceptance gates, a private game-file backup, or runtime testing
have been completed.
