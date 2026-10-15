# Checkpoint 086: verify the recovery kit before rebuilding

This checkpoint strengthens **asset-free reproducibility**, not gameplay
acceptance. No old converted port, retail archive, model, texture, sound, DLL,
save, private raw log or capture is uploaded. No retail conversion, Doom,
Steam, dmap, xemu or crash helper is run in this checkpoint.

Verified locally on Windows/Python 3.12.14: **553 source tests and 6 pipeline
tests pass**. After source commit
`dbaad8effdc3167bae04306ab103986891d9bccf` was pushed, a fresh source-only clone
from GitHub passed the same 183-file identity check, both byte-identical
regenerations and all 553 tests. This is a fresh **toolkit** check, not a
fresh licensed-input game rebuild. Exact evidence is recorded in the
[checkpoint summary](../evidence/checkpoint-086-portable-recovery.json).
After the pipeline was pushed, a fresh clone of pipeline commit
`fce095e00e730d76b13b39c3250df7a7a5721b76` also passed the verifier against
that fresh source clone, plus all 553 source and 6 pipeline tests. Neither
verification used the original working copies or any installed game inputs.

## One verification entry point in this pipeline repository

The [toolchain lock](../evidence/checkpoint-086-toolchain-lock.json) is the
authoritative source commit and tool/profile identity list. Do not substitute
the reconstruction repository's older `main` branch. The source commit is a
new continuation of `master`; checkpoint 085 remains an immutable baseline.

In a fresh directory on the next machine, using Git and Python 3.10 or newer:

Sign in to GitHub with an account authorized to read the reconstruction
repository first. It was not available to an unauthenticated request during
this checkpoint; the successful local clones used the existing signed-in
credential manager. The public pipeline does not grant private-source access.

```powershell
git clone https://github.com/Zippingrocks/DOOM-3-XBOX-to-PC-Pipeline.git pipeline
git clone --no-checkout https://github.com/Zippingrocks/doom3-gpl-xbox-reconstruction.git reconstruction
$recoveryPin = (Get-Content pipeline/evidence/checkpoint-086-toolchain-lock.json -Raw | ConvertFrom-Json).source_commit
git -C reconstruction checkout --detach $recoveryPin
python -E -s -B pipeline/tools/verify_recovery_checkout.py --source reconstruction --tests
```

This command needs **zero licensed game inputs and zero old ports**. It:

1. Verifies the source commit and every locked Python tool/test, PowerShell
   test dependency and profile. Code line endings are normalized; resource
   profiles retain their byte-exact LF/CRLF contract. Extra Python files and
   unexpected importable native/bytecode artifacts fail verification.
2. Verifies the preserved metadata lock, selectors, structural plan and summary.
3. Regenerates the 41-solo/20-co-op, 525-step, 90-AAS plan in a temporary
   directory and requires byte-identical output. No installed-game paths are
   consulted. Existing Python caches are bypassed for the verification run.
   It also regenerates the final-payload provenance trace byte-for-byte.
4. Runs the synthetic/offline source suite when `--tests` is supplied.

The GitHub workflow performs the same checks on Windows and Linux with Python
3.11 and 3.12. Both third-party actions are pinned to exact official commits;
workflow permissions are read-only, credentials are not persisted, and it does
not upload build outputs. **The first cloud run failed at source checkout**, not
in the verifier/tests: the pipeline's default token could not read the source
repository. See [the recorded run](https://github.com/Zippingrocks/DOOM-3-XBOX-to-PC-Pipeline/actions/runs/38784945848).
No cloud matrix pass is claimed.

To enable that check, a repository owner must configure the pipeline Actions
secret `RECOVERY_SOURCE_READ_TOKEN` with read-only Contents access to the
reconstruction repository. Do not paste the credential in chat, documentation
or code. The workflow supports this optional token, but none was created or
copied from the local credential manager. Repository visibility was not changed
and private source was not republished to work around the access boundary.
Pipeline-only synthetic tests run before the access gate; an unreadable source
still fails explicitly rather than skipping the required proof and going green.
Fork pull requests without that secret may therefore remain access-blocked.
This does not add an engine build matrix or license any game data for use on CI.

Do not run `tools/refresh_recovery_lock.py` to silence a mismatch. That
maintainer-only command exists to record a deliberately reviewed, committed
toolchain update in a **new** lock. Changed bytes must be investigated first.

## Opt-in raw structural runner

The source tool `tools/campaign_port/run_raw_structural_recipes.py` now turns
the existing structural recipe into an ordered, checked operation. It accepts
the preserved metadata lock, not arbitrary command JSON. The default is
read-only preflight: hash the selected original archives, validate exact map
selection and check that the destination is new. **No output is created**
unless `--execute` is explicitly provided.

After independently acquiring licensed originals and extracting their exact
archive members using [the raw-input recipes](RAW_INPUT_RECIPES.md), arrange:

```text
ORIGINAL_ARCHIVES/
  solo/<41 exact solo IDs>.gfc and .gob
  coop/<20 exact co-op IDs>.gfc and .gob
  shared/assets.gfc and assets.gob
```

These are fresh extractions from originals, not copies of any old port. For
this structural stage the plan selects 124 unique archive inputs (61 pairs
plus the shared pair), not all 136 observed archives. This is not a minimal
input claim for final audio, textures, PC fallbacks or complete overlays.

From the pinned source checkout, with explicit absolute paths substituted:

```powershell
python -E -s -B tools/campaign_port/run_raw_structural_recipes.py --inventory '<PIPELINE>/evidence/checkpoint-085-recovery-lock.json' --inventory-sha256 b171a2b843fad7d7a51ebd0fbfd2b6ff32c84f6cb410eeab84adad6c81ab4a74 --toolchain-lock '<PIPELINE>/evidence/checkpoint-086-toolchain-lock.json' --archives '<ORIGINAL_ARCHIVES>' --output '<NEW_PARENT>/raw-decoded'
```

To preflight a subset, add an exact selector such as `--map coop:xc_admin`.
Unknown, duplicate or wrong-mode names fail. Omit `--map` for all 61 maps.
Check the canonical identity in the plan rather than guessing a selector.
Only when deliberately authorizing offline conversion, repeat with `--execute`.
That flag is **not used** for the authentic corpus in this checkpoint.

Execution authenticates all needed archives before creating the output root,
enforces stage dependencies, runs only the canonical Python converters without
a shell or visible Windows console, and checks extracted member sets, sizes,
input/output hashes, available historical hashes and the fresh MAP-bound CRC.
It never invokes an engine or dmap and never stamps an AAS checksum to hide the
known Comm Outside mismatch. Source tools/profiles are hash-locked and the
receipt records the toolchain identity and interpreter hash/version.

Use short paths such as `D:/D3work` for future Windows recovery. The model
decoder now accepts `--temp-root`, validates same-volume staging before decode,
and the runner supplies the new output's parent. This avoids the previous
cross-volume rename failure without assuming the system TEMP drive matches
the output drive. Long Windows member paths remain a practical consideration.

The destination must not exist and must not overlap originals or source.
Reparse points are rejected. There is no overwrite or partial-run resume.
Failed outputs remain isolated with an `incomplete` receipt; inspect them and
choose another fresh destination rather than promoting them to accepted ports.
Private converter logs and reports stay local and are **not safe to upload
wholesale**. Synthetic tests do not establish full-corpus runner success.

### Witness gaps are explicit, not silently passed

The runner checks all available structural witnesses, including the final
AAS hashes, and compares all 41 solo model-corpus manifests to their locked
input/output identities. Co-op CM/model stages and co-op CRC steps lack the
same historical witnesses in the current structural plan; internally consistent
outputs are labelled unwitnessed rather than historical-equivalence passes.
`completed-with-witness-gaps` is not an acceptance status for final maps.

## What this fixes, and what remains essential

### A specific provenance queue, not another broad recovery search

The [metadata-only provenance trace](../evidence/checkpoint-086-provenance-trace.json)
indexes every final solo-v40/co-op-v20p payload entry. Its 25,914 original-member
witnesses and 2,131 recorded hash transitions link 7,568 of 8,914 entries to
locked Xbox archive pairs. **1,346 entries remain unresolved**, representing
606 distinct path/hash identities. These are evidence gaps, not a count of
broken files or a conversion-completion percentage.

Of the unresolved entries, 576 are beneath `sound/`, 284 beneath `dds/`, 156
beneath `models/`, and 111 beneath `maps/` (including generated script bridges).
Other generated/PC-fallback resources account for the remainder. The report
also flags 237 transform records that have an output but no input hash, and
602 unresolved entries whose recorded source is a predecessor overlay.

Use each unresolved row's final path/hash, source annotation and predecessor
receipt reference to reconstruct its producer. The graph retains individual
transform-receipt references, original archive identities and member witnesses.
It never treats an old overlay as an authenticated original root. Model-corpus
member claims are explicitly distinguished from independent extraction
receipts. Matching bytes can occur in multiple archives; a hash link does not
prove which physical copy was used, all auxiliary inputs, or exact tool options.

This roughly 42 MB JSON is an index of names, hashes and receipt relationships,
not map/model/audio data. It is reproducible from the existing metadata lock
alone; the verifier and CI compare it byte-for-byte. No path named inside the
metadata is opened by the tracer. Missing input hashes must not be invented
merely to improve its coverage numbers.

### Fail-closed fixes

The planner now rejects empty resource selections (which previously meant
“extract all”), duplicate resource members, case-aliased record identities,
invalid sizes, duplicate/noncanonical AAS baseline paths, and a CRC witness
that is invalid or does not belong to its decoded MAP. These failures were
covered with synthetic fixtures. The authentic checkpoint-085 plan remains
byte-identical; the safeguards do not rewrite accepted geometry or witnesses.

The largest remaining work is still **direct raw-input-to-final-overlay
composition**. Reconstruct the shared DEF/AF/static-model/audio/texture roots,
bind the exact PC fallback members and resource lookup order, and apply the
current transforms without using any predecessor overlay. The historical
version chain is a research index, not a build input contract.

Then perform a fresh isolated offline build from licensed originals and compare
every final payload with the preserved solo-v40/co-op-v20p manifests. A mismatch
must remain a failure or a reviewed intentional change, never a new baseline
created merely to make a test pass. The final v20p package audit, COOP host
selection and all previously documented runtime/fidelity gates remain open.

See the [085 recovery kit](CHECKPOINT_085_ASSET_FREE_RECOVERY.md),
[co-op/shared recipes](COOP_RECOVERY_RECIPES.md), and
[next-AI correction plan](REPRODUCIBILITY_RECOVERY_PLAN.md).
Git now preserves more executable recovery work, but a perfect re-port is
still not guaranteed until that full clean-input build and later acceptance.
