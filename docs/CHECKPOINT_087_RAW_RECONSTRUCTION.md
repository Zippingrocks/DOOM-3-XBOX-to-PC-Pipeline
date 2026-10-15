# Checkpoint 087: original-input reconstruction and missing resource recipes

This checkpoint is in progress. This first durable checkpoint records reviewed
runner improvements and fresh-checkout/preflight evidence; later results must
not be inferred from this file. No Doom, Steam, dmap or xemu is launched. No old
port is copied or uploaded. Fresh derived assets stay local and are not backups.

## Pinned structural runner

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

The complete 61-map / 525-step original-input reconstruction was launched in a
new isolated output tree after preflight. It consumes no previous overlays.
Its completion, output witnesses and companion failures are not yet recorded
here. Shared-resource and audio/texture recipes are under independent review.
Full raw-to-final composition, co-op host integration and gameplay/fidelity
acceptance remain separate work, not promises established by a Git push.
