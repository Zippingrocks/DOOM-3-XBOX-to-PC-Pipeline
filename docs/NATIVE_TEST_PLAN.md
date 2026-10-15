# Native campaign test plan

This is the first remaining validation tier. Do not infer native playability
from the green offline matrix or unified-tree hashes.

## Immutable input and runtime isolation

- `fs_game`: `xbox_campaign_test_v2`
- accepted tree: `work/campaign-test-tree-v2`
- isolated `fs_savepath`: `work/campaign-test-runtime-state`
- accepted tree ledger:
  `7e5241667542fb38a76a305f1f2aafb360bde2ef854e1e824837570c0fe60979`

The local `fs_game` directory is a junction to the accepted tree. Always set
the separate save root so `DoomConfig.cfg`, `qconsole.log`, saves and screenshots
do not contaminate that tree. Re-run `campaign_test_tree_audit.py` before and
after a test batch.

## Phase 1: bounded background loader pass

Do this only when starting Doom will not interrupt another active game. The
retail executable is Steam-wrapped: a direct launch can exit with code 4 before
filesystem initialization, and Steam will not launch it while another Steam
game is active. That is a launcher/bootstrap failure, not a map failure.

Use the fail-closed harness from the campaign recovery workspace. It refuses to
start when another executable under `steamapps/common` is active, starts Doom
through Steam, requests windowed/silent operation, waits for the native
`entities spawned` marker, observes a full 60-second idle, hashes the log and
then closes the process. It aborts the batch on launcher/bootstrap failure so
one environmental failure cannot be reported as 61 broken maps:

```powershell
cd "C:\Program Files (x86)\Steam\steamapps\common\Doom 3\Work files\campaign-port-dev"
.\tools\campaign_port\run_native_campaign_soak.ps1 `
  -Plan .\work\campaign-native-test-plan-v1.json `
  -DoomExe ..\..\Doom3.exe `
  -StateRoot .\work\native-soak-v2 `
  -Output .\work\native-soak-v2.json `
  -Launcher Steam `
  -IdleSeconds 60
```

Use `-StartIndex` and `-EndIndex` for a bounded slice. Use `-Resume` only with
an existing failure-free, non-aborted v2 report whose plan and executable
hashes still match; already recorded sequence numbers are skipped. A report
containing any failed row must be preserved and replaced rather than resumed,
so the failed sequence cannot be silently bypassed. Co-op entries automatically
set `si_gameType Coop` and `net_LANServer 1`. The runner actively minimizes the
Doom window after Steam creates it.

Preserve one `qconsole.log` receipt per map and the incremental JSON report.
Fail on missing declaration/resource, invalid joint, script error, fatal error,
wrong MAP/PROC/CM selection or abnormal exit. A `bootstrap_failure` or
`launcher_failure` means no map verdict was obtained. Do not advance to visual
testing until all 61 loader receipts close.

The interrupted v1 attempt from 2026-10-14 is retained locally at
`work/native-soak-v1.json`. Its first 31 invocations all exited with code 4,
created no qconsole log and reached no spawn marker while another Steam game
was active. Those rows are rejected bootstrap diagnostics, not campaign-map
failures and not resumable as v2 evidence.

## Phase 2: solo route

Run windowed with sound enabled and follow this exact transition route:

```text
mars_city1_1 -> mcu_1 -> mcu_2 -> mars_city2_1 -> mars_city2_2 -> admin
-> alphalabs1_1 -> alphalabs1_2 -> alphalabs2_1 -> alphalabs2_2
-> alphalabs3 -> enpro_1 -> enpro_2 -> commoutside_1 -> commoutside_2
-> comm1_1 -> comm1_2 -> recycling1_1 -> recycling2_1 -> recycling2_2
-> monorail_1 -> monorail_2 -> delta1_1 -> delta1_2 -> delta2a_2
-> delta2b_2 -> delta3_1 -> delta3_2 -> delta4 -> hell1_1 -> hell1_2
-> hell1_3 -> delta5_1 -> cpu_1 -> cpu_2 -> site3_1 -> caverns1_1
-> caverns1_2 -> caverns2 -> hellhole_1 -> hellhole_2 -> endOfGame
```

At each handoff record spawn placement, objective state, inventory, script
warnings and save/reload behavior. Exercise the three unreferenced teleport
attention records without modifying them unless runtime evidence proves a bug.

## Phase 3: two-peer co-op route

Use two real peers and follow:

```text
xc_mars_city1_1 -> xc_mcu -> xc_mars_city2_1 -> xc_mars_city2_2
-> xc_admin -> xc_alphalabs2_2 -> xc_enpro_1 -> xc_enpro_2 -> xc_comm1_1
-> xc_recycling2_1 -> xc_delta2b_1 -> xc_delta2b_2 -> xc_delta4
-> xc_hell1_1 -> xc_hell1_2 -> xc_delta5_1 -> xc_site3_1
-> xc_caverns1_1 -> xc_caverns2 -> xc_hellhole_1 -> endOfGame
```

At every spawn-level change record both player positions and facing, safe-spawn
selection, telefrag avoidance and host/client agreement. Exercise death,
spectator/rejoin, repeated triggers, inventory sharing, doors/GUI gates,
transitions and save/reload. `xc_site3_1`'s solo Caverns exit and
`xc_hellhole_1`'s solo Hellhole exit are dormant source residue with zero
incoming links; do not wire or follow them speculatively.

## Phase 4: fidelity comparison

After functional closure, compare PC and original Xbox capture at matched
checkpoints for geometry, collision, portals, lighting, materials, animation,
audio, AI counts/placement, scripted timing, objectives and cinematics. Record
every discrepancy against the exact map and entity/resource receipt before any
edit.
