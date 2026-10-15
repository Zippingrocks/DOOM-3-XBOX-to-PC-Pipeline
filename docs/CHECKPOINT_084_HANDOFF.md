# Checkpoint 084 immediate handoff

Stopped at the user's request to push immediately. No Doom 3, Steam, dmap or
xemu launch occurred. No installed DLL or original/accepted assets were replaced.
Retail-derived data and raw diagnostics stay local; Git contains source,
synthetic tests, documentation and metadata-only evidence.

## Saved source

Reconstruction repository `master` is pushed through
`c61e370365ecabd826594947afcc82ec2cfb236f`. It includes the main offline fixes,
Guardian duplicate-manifest correction and Lantern dependency-scope correction.
All **460 tests pass**. The older COOP-capable source `main` at
`51d0a78bb19b6b4716726a6afc089ea57fe5741c` is preserved, not overwritten.
The isolated DLL compiled with zero errors and existing warnings; it was not
installed or run. Checkpoint evidence records its exact hash.

## Exact local state

- Solo v40 overlays, package and test tree are complete. Strict tree audit:
  41 maps, 994 files, no duplicate definition/material or missing companion.
  All 244 loose MD5 files pass structure checks. The separate AAS identity
  gate still fails the single original Comm Outside 1 mismatch.
- Co-op: all 20 `xbox_coop_port_strict_*_mergeguard_v20p` overlays are complete,
  with a rebuild receipt. Independent checks verify all 90 MAP/compiled
  companion files, receipt hashes/sizes, no duplicate manifest paths and no
  unused Lantern asset/transform. **The full overlay audit was stopped before
  its receipt was produced.** `work/coop-pkg-mg20p` and
  `work/campaign-coop-test-tree-v32` do not yet exist. Final package/tree/merge/
  MD5/CRC acceptance is unfinished.
- Preserve rejected v20n (duplicate Guardian receipt) and superseded v20o /
  co-op tree v31 (strict checks passed but included an unused Lantern asset).
  Their evidence is not acceptance for v20p.

The final co-op offline process chain was explicitly stopped. No process needs
to keep running in the background. Completed outputs were not deleted.

## Resume without gameplay testing

Use the final source/tool mirror. Start at the **co-op overlay audit** in
[REPRODUCE](REPRODUCE.md#checkpoint-084-offline-only-corpus-review), not the
already-completed v20p rebuild. Verify that all 20 selected audit overlays end
in `mergeguard_v20p`. Continue packaging, separate-tree assembly, strict tree
audit, merge audit, MD5 corpus audit and checksum audit. Named final output/
receipt paths were absent at stop time; check again before using them.

Solo v40 was built at source `a23d1a9062abfc4fe5a1cfcd57ecd83c572fd5c8`;
co-op v20p at `c61e370365ecabd826594947afcc82ec2cfb236f`. Preserve those
per-corpus provenance boundaries when reproducing exact receipts. Later fixes
refine DEF ownership and Lantern demand, not native C++ or authored geometry.

## Unfinished gates

1. Current reconstructed `master` cannot select COOP through its normal cvar,
   game-type and player-definition path. Deliberately integrate the preserved
   older COOP lineage with new map-host classes; adding only a mode name is
   insufficient. Historical loader survival was not two-peer acceptance.
2. Comm Outside 1 AAS96 identifies 2127086718 while MAP/CM/AAS48 identify
   1317835462. The original Xbox input already differs. Do not stamp its header
   to hide the mismatch; which source component is stale is not established.
3. Enpro head `eyecontrol`, five absent declared jumpsuit clips, unsupported
   script events, GUI transition destinations, the dangling Delta 4 callback,
   `sonicips.ips` and `recycwallight_broken.ase` remain flagged.
4. Sabaoth bounds-search routes exist, but full path following is unverified.
   Physics, progression, save/load, visual/audio fidelity and two-peer behavior
   remain unaccepted. Offline checks cannot establish 100% working gameplay.

Public evidence includes a hash-verified inventory of 38 historical warning
families across all 61 maps. Raw logs and recovered assets remain private.
