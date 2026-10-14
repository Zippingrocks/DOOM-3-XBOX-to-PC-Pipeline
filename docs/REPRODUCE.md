# Reproduce checkpoint 001

## Source and environment

Implementation repository: `Zippingrocks/doom3-gpl-xbox-reconstruction`.
Pinned implementation commit: `51d0a78bb19b6b4716726a6afc089ea57fe5741c`.
Baseline parent: `833379c9920403fdfcc9f460042ca1b7ff205808`.
The diff contains four added files and no modifications/deletions.

Use an authenticated clone because the implementation repository is private.
Do not reset an existing worktree or discard uncommitted work to reproduce.
An isolated worktree keeps the accepted installation and current work untouched:

```powershell
git -C D:/repos/doom3-gpl-xbox-reconstruction fetch origin
git -C D:/repos/doom3-gpl-xbox-reconstruction worktree add --detach `
  D:/repos/doom3-campaign-port-checkpoint-001 `
  51d0a78bb19b6b4716726a6afc089ea57fe5741c
Set-Location D:/repos/doom3-campaign-port-checkpoint-001
python --version
python -m unittest discover -s tools/campaign_port/tests -v
```

The paths are examples. The implementation targets Python 3.10+ with only the
standard library. This pass executed Python 3.13.5 on Linux: 46 tests passed.
Neither native Windows nor Python 3.10 was run here. Fixtures are generated in
temporary directories and contain no game data. Passing these tests is not a
successful map conversion, engine build, loader test or two-player session.

## Local input layout

Under the reconstruction checkout, use:

```text
game/campaign_port_inputs/xbox/            # read-only licensed source copies
game/campaign_port_inputs/pc_mp_reference/ # existing matched MP conversion
game/campaign_port_work/                  # generated reports/extraction/output
```

The source repository already ignores `game/`. Keep all generated files under
that repository boundary. Do not stage these input/output directories into
Git, and do not copy retail data into the public pipeline repository.

Required for the next real recovery pass: complete matching GFC/GOB pairs or
an already-extracted Xbox corpus with provenance, a converted MP reference and
its original Xbox counterpart, and the relevant map registry/shared dependency
files. The retail XBE is a separate local input when reader analysis becomes
necessary. No such retail corpus was available to this checkpoint.

## Inventory and extraction

Run from the implementation repository. Replace `archive.gfc` and all other
example filenames with actual paths; these names are not claims about the disc.

```powershell
$tool = 'tools/campaign_port/doom3_campaign_port.py'
python $tool inventory game/campaign_port_inputs/xbox/archive.gfc `
  --report game/campaign_port_work/inventory-001.json
python $tool extract game/campaign_port_inputs/xbox/archive.gfc `
  --out game/campaign_port_work/extracted-001
```

Use `--gob PATH` if automatic same-stem `.gob` resolution is wrong. Inventory
reads metadata and hashes the pair without decoding payloads. Extraction uses
STBL zlib/stored blocks only. A new output directory is required; unknown
formats, invalid paths, size violations and decoding errors fail instead of
producing a falsely complete tree. Sources are rehashed before publication.

A selective exploratory run can use `--include '*coop*'`, but this is **not** a
complete campaign dependency extraction. Inventory all members and retain
shared assets. Default limits are 64 MiB expanded block, 1 GiB file and 8 GiB
selected output. Increase explicit limits only after inspecting the corpus.
Each extraction publishes `extraction-manifest.json` with source hashes,
original records, block offsets/hashes and copied byte ranges.

## Inspect and pair references

```powershell
python $tool inspect game/campaign_port_inputs/pc_mp_reference/reference.proc `
  --require-decoded --report game/campaign_port_work/reference-proc.json
python $tool inspect game/campaign_port_work/extracted-001/base/maps/candidate.map `
  --report game/campaign_port_work/candidate-profile.json
python $tool probe-reference game/campaign_port_work/extracted-001/base/maps/original-mp.proc `
  game/campaign_port_inputs/pc_mp_reference/reference.proc `
  --report game/campaign_port_work/mp-byte-candidates.json
```

First pair the same MP map; only then apply evidence-supported findings to a
campaign map. Input extensions are labels, not decoder selection. Binary
payloads remain opaque unless an actual decoder exists. The probe searches both
float32 endians and caps anchors/hits; it never selects a layout automatically.
Read the limits in the JSON and in FORMAT_FINDINGS.md.

For supported PC PROC comparison after an actual exporter exists:

```powershell
python $tool compare-proc game/campaign_port_inputs/pc_mp_reference/reference.proc `
  game/campaign_port_work/generated/candidate.proc `
  --report game/campaign_port_work/proc-comparison.json
```

This checkpoint supplies no Xbox-to-PC exporter. The last command is a
comparison facility for a future exported result or an existing second PC
reference, not a claim that `generated/candidate.proc` has already been made.

## Result interpretation

Exit 0 means the command produced its report. Exit 1 means parsed PROC
structures differ. Exit 2 means invalid supported data, I/O failure or refused
overwrite. Exit 3 means `inspect --require-decoded` encountered unsupported or
partial data. Ordinary inspection can return 0 with `decoded: false`; do not
turn that into a readiness badge. Recognized malformed input produces a
`parse_error` report and exit 2.

All reports use exclusive creation: choose a new report filename to preserve
prior evidence. Tool hashes and supported/unsupported obligations are listed in
`evidence/checkpoint-001.json`. Record exact commands, source hashes, outputs,
failures and evidence-level changes for every future checkpoint.
