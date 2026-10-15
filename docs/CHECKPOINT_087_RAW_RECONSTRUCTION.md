# Checkpoint 087: original-input reconstruction and missing resource recipes

The three separate original-input reconstruction runs are complete. Reviewed
source and metadata are pushed in checkpoints; authentic results are below.
No Doom, Steam, dmap or xemu is launched. No old port is copied or uploaded.
Fresh derived assets stay local and are not backups.

For the shortest practical route, use the
[next-machine quickstart](NEXT_MACHINE_QUICKSTART.md). Its combined entry point
has passed authentic read-only preflight on this device with no output created;
the separate runners' executed results are below. A combined end-to-end
execution is not inferred from the preflight.

## Completed original-input runs

- Raw structural: **41 solo + 20 co-op maps / 525 steps / 124 original archive
  files**, all completed. Available historical witnesses match. The result is
  deliberately `completed-with-companion-identity-failures` (exit 1), not a clean
  pass: Comm Outside 1's authored AAS96 header is `2127086718` while its fresh
  MAP checksum is `1317835462`. No header was stamped or witness weakened.
  Sixty co-op steps (20 MAP-CRC, 20 CM, 20 model steps) lack historical
  witnesses and remain listed as gaps, not inferred equivalence.
  [Sanitized raw proof](../evidence/checkpoint-087-raw-structural-proof.json).

- Shared: all **23 roots / 348 member occurrences / 30 original archive files**
  pass exact extracted-payload witnesses.
  [Sanitized shared proof](../evidence/checkpoint-087-shared-resource-proof.json).
- Audio/texture: all **173 steps / 441 files** pass exact expected hashes,
  including 111 metadata inputs and 330 WAV/DDS payloads. They cover all 860
  targeted final-map sound/DDS entries, with zero unresolved entries in this
  bounded selection. Two original archives and 387 distinct ISO extents/spans
  were authenticated before and after execution.
  [Sanitized audio/texture proof](../evidence/checkpoint-087-audio-texture-proof.json).

All three runs used a fresh GitHub source checkout at the resource pin and new
isolated destinations. No previous overlay or old decoded resource was used
as input. Outputs and logs stay private. The public proof files are strictly
validated receipt projections; publishing them is not itself another payload
replay. All 43 pipeline synthetic tests pass at the tested pipeline revision
recorded below. Both earlier numeric counterexamples pass in the completed
61-map run.

## Current portable kit: deterministic decoding and original resources

Use [the resource toolchain lock](../evidence/checkpoint-087-resource-toolchain-lock.json),
source `123904fa5862e3299b81504ee5d836c394953f2c`, on reconstruction `master`.
The checkout verifier and CI now default to this lock. It binds 195 source
files and eight pipeline artifacts, including the new shared-resource plan,
audio/texture input bindings and audio/texture plan. SHA-256:
`35809549fb588ae7307a09603c42ea7a611cb9bc84e33b91c157376c2a085470`.

Fresh authenticated GitHub checkouts of pipeline
`e6b8efdc524bda126c777c6ddeb3aec38124b4cc` and the pinned reconstruction source
pass all 629 source tests and all 43 pipeline tests on Windows/Python 3.12.14,
and byte-identically regenerate the structural, shared-resource, audio/texture
and provenance plans. The resource-pin 629-test suite
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
ISO extent/input span was newly authenticated; the completed execution above
now matches those output witnesses. No audio/texture asset was uploaded.

Current local shared declaration files were also checked read-only: all 137
selected members match the original extraction hashes. There is no observed
mutation in that current shared catalog. This does not establish every early
overlay's declaration closure or unrecorded historical producer.

## Earlier structural-runner checkpoint (retained evidence)

Historical source `87ed2b6e8a6c6509957d508686bd1ecb9cde8666` is pushed to reconstruction
`master`. The [structural toolchain lock](../evidence/checkpoint-087-structural-toolchain-lock.json)
pins 183 source files and the same five metadata artifacts as checkpoint 086.
Its SHA-256 is `7f08e16641ee66b9da89738e9d7befcc7a918a549a0f68d5ec87658e38d9e4ce`.
This older pin predates the numeric fix; do not select it for new reconstruction.
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
python -E -s -B reconstruction/tools/campaign_port/run_raw_structural_recipes.py --inventory pipeline/evidence/checkpoint-085-recovery-lock.json --inventory-sha256 b171a2b843fad7d7a51ebd0fbfd2b6ff32c84f6cb410eeab84adad6c81ab4a74 --toolchain-lock pipeline/evidence/checkpoint-087-resource-toolchain-lock.json --archive-root 'solo=D:/licensed/solo-archives' --archive-root 'coop=D:/licensed/coop-archives' --archive-root 'shared=D:/licensed/shared-archives' --output 'D:/recovery087/raw'
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

## Later source helpers and existing-output checks

Source `03252a51b2c4395228f633728d32dd4a977889ba` adds an explicit
`build_runtime_overlay.py --virtual-map` identity for flat fresh decoder output,
with namespace/filename/traversal checks, plus a portable exact-generation
co-op auditor. All 645 source tests pass. This successor is **not** substituted
for the resource lock's proven `123904f` execution pin. No authentic final
overlay has been built with the new virtual-map option yet.

The read-only auditor selected exactly `mergeguard_v20p`, bound the existing
rebuild receipt by SHA-256, and rechecked its primary tool identities at exit:

- [Payload proof](../evidence/checkpoint-087-existing-coop/coop-overlay-corpus.json):
  20 overlays, 6,218 files, 559,759,378 bytes; no untracked files or reported
  unresolved class/resource/string references.
- [MD5 structure proof](../evidence/checkpoint-087-existing-coop/coop-md5-structure.json):
  4,843 physical MD5 files (158 meshes, 4,685 animations), 643 unique path/hash
  pairs, no parse/structure issues.
- [Companion proof](../evidence/checkpoint-087-existing-coop/coop-companion-crc.json):
  20 maps / 50 companions, no checksum mismatches.

These are checks of historical local outputs, **not inputs to the fresh runs**.
Only sanitized metadata is saved. No package or assembled test tree was created.
Individual MD5 structure does not prove animation-family compatibility;
matching companion checksums do not prove collision/navigation fidelity.

## Next bounded tasks, without rediscovering the formats

1. Reproduce the checked intermediate stages using the quickstart and exact
   resource lock. The initial failed numeric runs remain counterexamples, not
   passes. Do not reuse their partial output directories.
2. Close direct raw-to-final composition, first for one co-op map and then the
   corpus: ordered resource roots, current transform profiles, generated script
   bridges and individually authenticated PC fallback members. Use the shared
   plan's 20 composition contracts and four unresolved retarget dependencies;
   do not make the old 22-generation overlay chain a new input requirement.
3. Bind each new producer to its source/profile/input hashes, compare final
   logical paths and payload hashes against the preserved witnesses, and
   retain any missing provenance as an explicit gap. The old checkpoint-086
   provenance trace is immutable; its 1,346 unresolved entries have not been
   globally recomputed merely because 860 audio/texture routes now have proofs.
4. Finish fresh assembled-tree/package/merge and model-family gates. Existing
   local-overlay checks above cannot substitute for these fresh-build checks.
5. Integrate the map-relevant co-op host prerequisites deliberately: current
   reconstruction `master` cannot select COOP through its normal game-type
   resolver. The older `main` lineage has broader co-op code but must not
   wholesale replace the newer map-host fixes. Keep the authored AAS mismatch
   and remaining warning families documented in acceptance/format findings.
6. Only after separate authorization, perform loader, two-peer, progression,
   save/load and visual/audio fidelity acceptance. Cloud CI still needs an
   owner-provided private-source read credential; neither local verification
   nor a workflow file is a cloud/Linux matrix pass.

The three authentic runs have finished; no long-running recovery process needs
to survive device migration. Their derived assets and private logs stay local.
Git preserves tools, exact plans, sanitized witnesses and findings, not a game
backup or a claim that the final maps can already be reconstructed perfectly.
