# Next-machine recovery quickstart

This is the short route to authenticated **recovery intermediates**, not an
installer for finished maps. It uses original Xbox inputs and the pinned
tools; it does not require, copy or back up an old port. No game, Steam, dmap,
xemu, native build or asset upload is involved.

Current checkpoint details and authentic-run results belong in
[checkpoint 087](CHECKPOINT_087_RAW_RECONSTRUCTION.md). The combined entry point
has passed authentic read-only preflight and synthetic orchestration tests.
Separate executed runner results do not by themselves prove that the combined
entry point has completed an authentic conversion run.

## 1. Clone and verify the exact source

Use Git and Python 3.10 or newer (Python 3.12 is the current reference runtime).
Sign in to GitHub through your normal Git credential manager using an account
allowed to read the reconstruction repository. Pipeline access does not grant
private-source access. Do not put a token in these commands, source or reports.

In a fresh workspace, run these PowerShell commands:

```powershell
git clone https://github.com/Zippingrocks/DOOM-3-XBOX-to-PC-Pipeline.git pipeline
git clone --no-checkout https://github.com/Zippingrocks/doom3-gpl-xbox-reconstruction.git reconstruction
$recoveryLock = 'evidence/checkpoint-087-resource-toolchain-lock.json'
$recoveryPin = (Get-Content (Join-Path 'pipeline' $recoveryLock) -Raw | ConvertFrom-Json).source_commit
git -C reconstruction checkout --detach $recoveryPin
python -E -s -B pipeline/tools/verify_recovery_checkout.py --source reconstruction --lock $recoveryLock --tests
```

Stop if any command fails. The current resource lock pins source
`123904fa5862e3299b81504ee5d836c394953f2c`, the reconstruction **master lineage,
not its older main branch**. The lock, not the latest branch tip, selects the
source. The verifier checks all pinned source/profile/metadata identities and
regenerates all four metadata plans/traces without opening licensed inputs.
Do not refresh a lock or edit a witness merely to bypass a mismatch.

## 2. Prepare licensed originals, not previous outputs

Obtain the original inputs independently. The supported disc image is
3,029,598,208 bytes, SHA-256
`444460aab24b6df9e4cf7bd9bc442f2c95d675f44d1022f0242818813eb7d20e`.
A different edition or language needs a separately supported identity; do not
reuse these offsets with it.

Use the exact member-selection instructions in the
[solo raw-input recipes](RAW_INPUT_RECIPES.md#1-original-disc-and-the-exact-41-solo-identities)
and [co-op/shared recipes](COOP_RECOVERY_RECIPES.md#1-authenticate-and-extract-the-discarchive-inputs).
The runners need 41 solo GFC/GOB pairs, 20 co-op pairs, and shared
`assets.gfc`/`assets.gob`, plus the original ISO for audio/texture extents.
The plans select exact required members; do not substitute an arbitrary old
extraction or assume a matching filename proves identity.

The three archive directories may stay anywhere: named bindings avoid copying
them into the historical DEV layout. They must contain the archive filenames
directly, not an extra nested `solo/`, `coop/` or `shared/` level. Input hashes
are checked before conversion. No old overlay, PK4 mod, engine installation or
stock PC fallback is an input to this recovery stage.

## 3. Preflight everything before conversion

Replace the example input paths below with your own originals. Use a short,
existing output parent on Windows; model paths can add more than 126 characters.
Create this parent once if needed (or select an existing directory):

```powershell
New-Item -ItemType Directory -Path 'D:/D3recovery'
```

All three output siblings and the session receipt must be absent. The tool
rejects existing destinations, unsafe path redirects and source/input overlap.
There is no overwrite or partial-run resume.

```powershell
$recoveryArgs = @(
    '--source', 'reconstruction',
    '--lock', $recoveryLock,
    '--iso', 'D:/licensed/original.xiso.iso',
    '--archive-root', 'solo=D:/licensed/solo-archives',
    '--archive-root', 'coop=D:/licensed/coop-archives',
    '--archive-root', 'shared=D:/licensed/shared-archives',
    '--output-parent', 'D:/D3recovery',
    '--prefix', 'recovery'
)
python -E -s -B pipeline/tools/recover_original_inputs.py @recoveryArgs
```

Default behavior verifies the checkout and preflights raw, shared and
audio/texture inputs in order. **It creates no recovery output.** A failed
preflight starts no conversion. Prefixes accept 1–48 ASCII letters, digits,
underscores or hyphens, starting with a letter or digit.

Only when deliberately authorizing offline conversion, run:

```powershell
python -E -s -B pipeline/tools/recover_original_inputs.py @recoveryArgs --execute
$LASTEXITCODE
```

This repeats every preflight before starting the first conversion. The three
fixed Python runners create `recovery-raw`, `recovery-shared` and
`recovery-audio`. A metadata-only `recovery-session.json` is created exclusively
after all preflights pass and preserves the completed stages or failure state.
Private converter logs remain in the new output trees. The tool neither builds
command lines from arbitrary JSON nor starts a native game process.

## 4. Interpret results without hiding known failures

| Overall result | Meaning |
| --- | --- |
| Exit 0, `offline-input-recovery-completed` | Every planned runner completed without reported companion failures or historical witness gaps; still not final-overlay acceptance. |
| Exit 1, `completed-with-known-issues` | Recovery finished, but raw companion CRC failures and/or historical witness gaps remain. |
| Other failure, or `incomplete` receipt | Stop and inspect the local failed stage; later conversion stages were not accepted. |

Raw exit 1 is allowed to continue to shared/audio only when its receipt proves
all planned raw steps completed under this session's pinned inputs/toolchain
and consistently reports `completed-with-companion-identity-failures`.
An arbitrary exit 1, a missing receipt, a witness mismatch, or another failure
stops the workflow. Historical equivalence does not repair an invalid AAS/CM
header; never stamp a checksum merely to turn the report green.

For the current pinned originals, the completed reference raw run reports
exactly one companion mismatch (solo `commoutside_1`, AAS96) and 60 historical
witness gaps (co-op MAP-CRC, CM and model steps). Shared and audio/texture
reference runs pass their exact selected witnesses. Use the published
checkpoint-087 proofs to distinguish these known outcomes from a new failure;
do not waive any additional mismatch or treat the known issues as acceptance.

Keep failed trees isolated and select a different fresh prefix for another
attempt. Do not delete or overwrite the failed evidence automatically.
Publish only reviewed code and allowlisted metadata. The original inputs,
converted assets, raw converter manifests and logs are **not** safe to upload
wholesale or include in a Git backup.

## What this does not finish

The remaining boundary is direct, source-bound composition into final solo and
co-op overlays: exact ordered resource roots, current transforms, generated
bridges, stock PC fallback members and retarget dependencies must be completed
without predecessor overlays. Then merged/package/static acceptance, actual
co-op host capability, and separately authorized gameplay/fidelity testing
remain. These commands do not establish perfect maps or a tested final build.

See the [recovery plan](REPRODUCIBILITY_RECOVERY_PLAN.md),
[co-op composition limits](COOP_RECOVERY_RECIPES.md#7-replay-ordering-and-remaining-composition-work)
and [acceptance criteria](ACCEPTANCE.md) before promoting any recovered output.
