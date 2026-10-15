# Checkpoint 087: original-input reconstruction and missing resource recipes

This checkpoint is in progress. Reviewed source and metadata are being pushed
in checkpoints; authentic conversion results are recorded separately below.
No Doom, Steam, dmap or xemu is launched. No old port is copied or uploaded.
Fresh derived assets stay local and are not backups.

## Current portable kit: deterministic decoding and original resources

Use [the resource toolchain lock](../evidence/checkpoint-087-resource-toolchain-lock.json),
source `123904fa5862e3299b81504ee5d836c394953f2c`, on reconstruction `master`.
The checkout verifier and CI now default to this lock. It binds 195 source
files and eight pipeline artifacts, including the new shared-resource plan,
audio/texture input bindings and audio/texture plan. SHA-256:
`35809549fb588ae7307a09603c42ea7a611cb9bc84e33b91c157376c2a085470`.

Fresh authenticated GitHub source checkout verification passes all 629 source
tests and byte-identically regenerates the structural, shared-resource,
audio/texture and provenance plans. The current working-source 629-test suite
also passes on installed Python 3.11.9, 3.12.14 and 3.13.10. This is local
cross-runtime evidence, not a cloud/Linux CI result.

The first authentic raw runs exposed a Python-version-dependent float-sum
change in a Revenant mesh (CPU2 and Delta1_2). The original input hash was
identical; one serialized joint coordinate differed in its last digits. The
fix makes the historical left-to-right accumulation explicit in model,
retargeting and static-normal serialization. It does not change a witness.
The historical interpreter itself was not recorded; historical bytes match
the ordered arithmetic observed on Python 3.11. A fresh CPU2 conversion using
the fix matches all 459 historical model output witnesses exactly. See the
[retained failed-run counterexamples](../evidence/checkpoint-087-reconstruction-counterexamples.json).

The new shared-resource plan binds 23 exact extraction roots, 348 member
occurrences and 30 original archive files. It also preserves ordered co-op
composition contracts and four still-incomplete retarget dependencies; it
does not invent a final-overlay build command.

The audio/texture capture binds all 860 previously unresolved sound/DDS final
entries (330 distinct payload identities) to 55 XACT and seven texture recipes.
The 173-step plan includes 111 exact metadata inputs. Every selected original
ISO extent/input span was newly authenticated; output hashes are historical
witnesses until execution passes. No audio/texture asset was uploaded.

Current local shared declaration files were also checked read-only: all 137
selected members match the original extraction hashes. There is no observed
mutation in that current shared catalog. This does not establish every early
overlay's declaration closure or unrecorded historical producer.

## Earlier structural-runner checkpoint (retained evidence)

Source `87ed2b6e8a6c6509957d508686bd1ecb9cde8666` is pushed to reconstruction
`master`. The [structural toolchain lock](../evidence/checkpoint-087-structural-toolchain-lock.json)
pins 183 source files and the same five metadata artifacts as checkpoint 086.
Its SHA-256 is `7f08e16641ee66b9da89738e9d7befcc7a918a549a0f68d5ec87658e38d9e4ce`.
The checkpoint-086 lock remains unchanged and still selects its older source.

A fresh authenticated GitHub clone at this new source commit passed:

- 183 source identities and five pipeline artifact identities;
- byte-identical regeneration of the 525-step structural plan and final-payload
  provenance trace;
- all 558 committed source offline tests on Windows/Python 3.12.14;
- authentic read-only preflight of 61 maps and 124 original archives.

The local pipeline's six synthetic tests pass. Cloud CI remains separately
access-blocked until the owner supplies its private-source read token; no cloud
test pass or clean-machine final-overlay equivalence is claimed.

The verifier now accepts a pipeline-relative versioned lock:

```powershell
python -E -s -B pipeline/tools/verify_recovery_checkout.py --source reconstruction --lock evidence/checkpoint-087-structural-toolchain-lock.json --tests
```

Check out the `source_commit` in that lock first, as in checkpoint 086. Do not
refresh a lock merely to bypass a mismatch.

## No rearranging or copying original archives

The runner accepts named directories as an alternative to `--archives`:

```powershell
python -E -s -B reconstruction/tools/campaign_port/run_raw_structural_recipes.py --inventory pipeline/evidence/checkpoint-085-recovery-lock.json --inventory-sha256 b171a2b843fad7d7a51ebd0fbfd2b6ff32c84f6cb410eeab84adad6c81ab4a74 --toolchain-lock pipeline/evidence/checkpoint-087-structural-toolchain-lock.json --archive-root 'solo=D:/licensed/solo-archives' --archive-root 'coop=D:/licensed/coop-archives' --archive-root 'shared=D:/licensed/shared-archives' --output 'D:/recovery087/raw'
```

The output parent must already exist; the output itself must not exist. The
default is read-only and creates no output. Add `--execute` only to deliberately
run offline reconstruction. Keep the output root short on Windows (preferably
under 100 characters): authentic solo model paths can add another 126 characters.
All named originals and the source tree are protected from output overlap.

The new checks independently enumerate every decoded model payload, rejecting
unlisted files, and compare each fresh CM/AAS header to its fresh MAP checksum.
A historically identical output can still have an invalid companion checksum.
The runner records all such mismatches without rewriting/stamping them, finishes
the remaining planned steps, then exits 1 with
`completed-with-companion-identity-failures`. Malformed headers/conversion or
witness failures still stop with an incomplete receipt. Witness gaps remain
separately listed; neither completion status is final-map acceptance.

## Work still running at this checkpoint

The initial runs stopped correctly on the numeric counterexample and remain
incomplete, not passes. After the deterministic fix and a new fresh source
clone, a new complete 61-map / 525-step run was launched. Independent fresh
23-root shared and 173-step audio/texture runs were also launched. They consume
no previous overlays. Their final results are not yet recorded in this section.
Full raw-to-final composition, co-op host integration and gameplay/fidelity
acceptance remain separate work, not promises established by a Git push.
