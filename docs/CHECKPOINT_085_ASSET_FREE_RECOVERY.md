# Checkpoint 085: move the recipes, not the converted ports

2026-10-15. The user cannot transfer the existing converted game files and
does not want a cloud game-data backup. This checkpoint preserves **non-game
source and metadata** in GitHub and makes the raw-input recovery path more
explicit. No game archive, converted map, texture, model, audio, DLL, save,
private log, screenshot or minidump is included.

## What was actually completed

- Source implementation through `c76f6e066d180fd9a0e63d2b02bcfe069dd57010`.
  The complete offline suite passes **501 tests**. No engine was launched.
- A metadata lock covering **1,660 files**, including **1,480 projected JSON
  receipts**, 136 original Xbox GFC/GOB files, 15 local PC PK4 inputs and 29
  tracked profiles. Originals were hashed, **not copied**. Projections discard
  raw name records, hex/byte dumps, script/dialogue text and unapproved fields.
  Known workspace paths become named roots; external paths become digests.
- Exact-member raw structural recipes for **41 solo + 20 co-op maps**:
  **525 ordered steps**, including all **90 recorded AAS files** and their
  shared-archive boss-specific variants. These are generated argv templates,
  not commands executed in this checkpoint.
- All nine reviewed local diagnostic source files are archived inertly, with
  verified original hashes. Their private inputs/outputs are excluded.
- Solo replay can explicitly remap old absolute profile roots with SHA-256
  guards and recorded intentional profile corrections.
- Co-op replay with an explicit input suffix no longer selects identities by
  unrelated “latest” manifest timestamps.
- Profile checkout line endings are pinned. Git's checkout filtering reproduced
  all 29 locked profile hashes, including the historical CRLF MCU profile.
- The mistaken disc selector `base/xc_*.gfc` was corrected to the actual
  root-level `xc_*.gfc` layout for the authenticated original ISO.

The final metadata verification passed all 1,660 selected file identities.
Regenerating the plan from metadata in a different working directory produced
byte-identical JSON. Exact hashes and validation counts are in the
[checkpoint evidence summary](../evidence/checkpoint-085-asset-free-recovery.json).
None of these checks is a clean-machine game rebuild, package acceptance or
gameplay test.

## Files to use on the other machine

1. [Metadata lock](../evidence/checkpoint-085-recovery-lock.json):
   selected input identities and sanitized original receipt relationships.
2. [Capture selectors](../evidence/checkpoint-085-recovery-selectors.json):
   bounded coverage and exact expected counts, not a list of payloads to upload.
3. [Raw structural recipe plan](../evidence/checkpoint-085-raw-structural-plan.json):
   original member names, source hashes, source/archive relationships,
   decoder arguments, output witnesses and explicit dependencies.
4. [Solo/raw recipes](RAW_INPUT_RECIPES.md):
   exact solo identities, bootstrap contracts, profile transitions and
   Cyberdemon retarget witnesses.
5. [Co-op/shared recipes](COOP_RECOVERY_RECIPES.md):
   original co-op inputs, all 22 replay ancestry edges, corrected AAS provenance,
   shared AF/DEF/static-model/audio/texture producers and remaining gaps.
6. [Original stop state](CHECKPOINT_084_HANDOFF.md) and
   [reproducibility/bug correction plan](REPRODUCIBILITY_RECOVERY_PLAN.md).

The lock and plan are roughly 45 MB of uncompressed JSON combined, not 45 MB
of game content. Their Git transport can be compressed; neither requires a
Mega or Google Drive account. Byte-hash-sensitive JSON is LF-pinned in Git.

## New-machine procedure without old ports

Clone the pipeline repository and the reconstruction repository. Pin the latter
to `c76f6e066d180fd9a0e63d2b02bcfe069dd57010` (source `master` lineage).
Do not substitute the older source `main` branch. It contains different COOP
host work still needed for deliberate later integration.

Supply legitimately obtained original Xbox and PC inputs on the new machine.
Git cannot substitute for those licensed originals. The recorded Xbox ISO is
3,029,598,208 bytes, SHA-256
`444460aab24b6df9e4cf7bd9bc442f2c95d675f44d1022f0242818813eb7d20e`.
A different edition must be deliberately inventoried and supported, not
silently accepted as the same inputs.

### A. Inspect and regenerate the plan using metadata only

From the pinned source checkout:

```powershell
python -B tools/campaign_port/plan_raw_structural_recipes.py --inventory '<PIPELINE>/evidence/checkpoint-085-recovery-lock.json' --output '<NEW_METADATA>/raw-structural-plan.json' --require-solo 41 --require-coop 20
```

This requires **no game files and no predecessor ports**. It should report
41 solo maps, 20 co-op maps, 525 steps and 90 compiled AAS inputs.
It verifies the preserved archive/extraction/decode identity relationships
before emitting a plan. The output must not already exist.

The plan's braces are **substitution markers**, not shell syntax:

- `{SOURCE}`: pinned reconstruction checkout.
- `{PYTHON}`: Python 3.10+ interpreter.
- `{ARCHIVES}`: fresh original-archive extraction root with `solo/`,
  `coop/` and `shared/` children.
- `{NEW}`: new isolated decoding output root.
- `{REPORT:map-crc.geometry_crc}`: read the integer field from that map's
  newly produced CRC report. Never run dmap or stamp an AAS header instead.

Do not feed the JSON to a shell or claim it is an executable orchestrator.
A future runner must resolve substitutions, enforce dependencies, authenticate
inputs, create only fresh outputs and compare every available output witness.

### B. Authenticate originals and extract exact members

Use the disc and archive commands in the two recipe documents. The plan records
the exact disc member for each original archive pair, and exact GFC member
selection including the significant leading `./`. Recreate archive directories
from the ISO; do not copy any old overlay.

The general lock verifier supports explicit replacement roots:

```powershell
python -B tools/campaign_port/recovery_metadata.py verify --inventory '<PIPELINE>/evidence/checkpoint-085-recovery-lock.json' --root 'DEV=<NEW_DEV>' --root 'GAME=<NEW_PC_INSTALL>' --root 'SOURCE=<SOURCE>' --category xbox-original --category pc-input --category tracked-profile
```

This checks the **observed** original-input set at its historical root-relative
layout. It is not a proof of the minimal required set: that inventory includes
five MP reference archive pairs and the installed Xbox MP addon PK4s. Missing
reference-only inputs must be reviewed and deliberately excluded from a future
minimal lock, not treated as permission to loosen all hash checks.

Verifying every category on a new machine will correctly report missing old
receipts/overlays. Those records are **reference evidence**, not mandatory
inputs to the new raw structural plan. Do not restore old ports merely to make
that blanket verification pass.

### C. Rebuild raw structural/model resources, then finish composition

Execute only reviewed stages in a new workspace when reconstruction is
authorized. The plan covers core/script extraction, MAP/PROC/CM/all-AAS decode,
map-CRC calculation, per-map resource extraction and model-corpus decoding.
Shared-archive special AAS extraction is explicit; all final AAS identities
must be present. The original Comm Outside 1 AAS96 CRC mismatch remains a known
defect; matching an expected file hash does not resolve it.

Use the documented shared DEF/AF/static/XACT/D3TFULL/retarget recipes next.
Preserve resource lookup order. Reconstruct initial strict overlays from those
fresh resources; **do not treat nativefix-v12, v39, mergeguard-v20m or an original
per-map overlay as an unexplained required input**.

This last composition is the important unfinished stage. The replay chain is
a research index showing where decisions were made, not a requirement to
recreate every historical version serially. Read existing transformations,
profiles and receipts first; write a direct raw-input composition with exact
selection and validate its payloads against the locked final manifests.

## Incremental replay portability fixes are not a cold-start shortcut

If a future machine has reconstructed a valid predecessor locally, it may use
the improved replay drivers. They still do not generate those predecessors.

For solo v39-to-v40, remap the old profile-directory spelling explicitly:

```powershell
python -B tools/campaign_port/rebuild_latest_solo_overlays.py '<REBUILT_V39>' '<NEW_V40>' --work-root '<NEW_WORK>' --stock-dir '<PC_BASE>' --require-maps 41 --receipt '<NEW_RECEIPT>' --profile-root-map 'C:\Program Files (x86)\Steam\steamapps\common\Doom 3\Work files\campaign-port-dev\tools\campaign_port\profiles' --profile-hash-update 905ca65cf179d2062b64ba157c77b88e9d07e56942a1f776e48a647f7af56e55=6ee107d1145e5608604eadf5f1422a80484133e2e7e277a4b753a11dfe4f6699
```

That hash update is the documented Lantern profile correction, not blanket
permission to accept changed profiles. The rebuild receipt records old path/
hash and resolved path/hash; original predecessor manifests stay untouched.
Unmapped paths retain legacy behavior, so deliberately cover every moved root.

For co-op, use explicit `--input-suffix mergeguard_v20m`; selection is now
deterministic. The final v20p offline audit/package chain is still unfinished,
and no old native load result transfers to newly generated outputs.

## What is still not solved

- Complete source/version/argument binding for every earlier resource producer
  and any manual preparation step.
- Exact initial strict-overlay composition/ordering replacing the v12/original
  per-map-overlay dependency, plus a complete authenticated all-stage runner.
- Audio bank-input hash/extent provenance and minimal PC fallback selection
  wherever historical receipts omit those fields.
- A fresh-machine end-to-end run proving final output equivalence.
- The previously documented COOP host selection, Comm Outside AAS, Enpro head,
  script/GUI/resource and Sabaoth-path problems; final gameplay/fidelity gates.

No game data was backed up, and no gameplay/xemu test was performed. If this
device becomes unavailable, the new machine has substantially more exact
recovery information, but **a perfect re-port is not yet guaranteed**.
