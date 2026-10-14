# Reproduce checkpoint 023

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
loader acceptance are still open.

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
