#!/usr/bin/env python3
"""Recover authenticated original inputs through three fixed, pinned runners.

Default is read-only: verify the checkout and preflight raw, shared and audio
inputs. --execute starts only after all three preflights pass. Output siblings
PREFIX-raw, PREFIX-shared and PREFIX-audio must not exist; no resume, overwrite,
old-port import, game launch or upload is supported. A metadata-only session
receipt is created exclusively after preflight and updated only by this run.
Known raw companion identity failures remain a nonzero overall result. These
outputs are recovery intermediates, not complete overlays or gameplay proof.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import tempfile
import uuid

sys.dont_write_bytecode = True
sys.pycache_prefix = str(Path(tempfile.gettempdir()) / ("doom3-session-no-cache-" + uuid.uuid4().hex))

import verify_recovery_checkout as checkout

STAGES = ("raw", "shared", "audio")
RUNNERS = {"raw": "run_raw_structural_recipes.py", "shared": "run_shared_resource_recipes.py",
           "audio": "run_audio_texture_recipes.py"}
RECEIPTS = {"raw": "raw-recovery-run.json", "shared": "shared-recovery-run.json",
            "audio": "audio-texture-run.json"}


def absolute(path: Path) -> Path:
    path = Path(os.path.abspath(path))
    return checkout.safe_path(path.parent, path.name)


def archive_roots(values: list[str]) -> dict[str, Path]:
    roots = {}
    for value in values:
        name, separator, directory = value.partition("=")
        if not separator or name not in {"solo", "coop", "shared"} or name in roots or not directory:
            raise ValueError("use unique --archive-root solo=DIR, coop=DIR and shared=DIR")
        path = absolute(Path(directory))
        if not path.is_dir():
            raise ValueError("archive roots must be existing directories")
        roots[name] = path
    if set(roots) != {"solo", "coop", "shared"}:
        raise ValueError("all three original archive roots are required")
    return roots


def destinations(parent: Path, prefix: str) -> tuple[dict[str, Path], Path]:
    if not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9_-]{0,47}", prefix):
        raise ValueError("prefix must be 1-48 ASCII letters, digits, underscores or hyphens")
    parent = absolute(parent)
    if not parent.is_dir():
        raise ValueError("output parent must already exist")
    outputs = {name: checkout.safe_path(parent, prefix + "-" + name) for name in STAGES}
    session = checkout.safe_path(parent, prefix + "-session.json")
    for path in (*outputs.values(), session):
        if path.exists() or path.is_symlink():
            raise ValueError("refusing an existing recovery output or session receipt")
    return outputs, session


def prepare(source, lock_name, iso, roots, outputs):
    """Only fixed runner entrypoints/flags; no plan-provided commands are used."""
    lock_path = checkout.safe_path(checkout.PIPELINE, lock_name)
    lock_bytes = lock_path.read_bytes()
    lock = json.loads(lock_bytes)
    resources = checkout.resource_artifacts(lock)
    required = {"shared_resource_plan", "audio_texture_bindings", "audio_texture_plan"}
    if set(resources) != required:
        raise ValueError("lock must include shared-resource plan and paired audio bindings/plan")
    inventory = checkout.bound_artifact(lock, "metadata_lock")
    raw_plan = checkout.bound_artifact(lock, "structural_plan")
    inventory_sha = hashlib.sha256(inventory.read_bytes()).hexdigest()
    bindings_sha = hashlib.sha256(resources["audio_texture_bindings"].read_bytes()).hexdigest()
    root_args = [value for name, path in sorted(roots.items()) for value in ("--archive-root", name + "=" + str(path))]
    python = [sys.executable, "-E", "-s", "-B", "-X", "pycache_prefix=" + sys.pycache_prefix]
    commands = {}
    for stage in STAGES:
        tool = checkout.safe_path(source, "tools/campaign_port/" + RUNNERS[stage])
        if not tool.is_file():
            raise ValueError("pinned recovery runner is absent")
        flags = (["--bindings", str(resources["audio_texture_bindings"]), "--bindings-sha256", bindings_sha,
                  "--iso", str(iso)] if stage == "audio" else
                 ["--inventory", str(inventory), "--inventory-sha256", inventory_sha])
        commands[stage] = [*python, str(tool), *flags, "--toolchain-lock", str(lock_path),
                           *root_args, "--output", str(outputs[stage])]
    return {"commands": commands, "plans": {"raw": json.loads(raw_plan.read_bytes()),
                "shared": json.loads(resources["shared_resource_plan"].read_bytes()),
                "audio": json.loads(resources["audio_texture_plan"].read_bytes())},
            "source_commit": lock["source_commit"], "metadata_lock_sha256": inventory_sha,
            "bindings_sha256": bindings_sha, "toolchain_lock_sha256": hashlib.sha256(lock_bytes).hexdigest()}


def run(command: list[str], cwd: Path) -> int:
    return subprocess.run(command, cwd=cwd, shell=False, check=False, stdin=subprocess.DEVNULL,
                          creationflags=0x08000000 if os.name == "nt" else 0).returncode


def unique_steps(rows, key):
    values = [key(row) for row in rows]
    if len(values) != len(set(values)):
        raise ValueError("duplicate stage receipt identity")
    return set(values)


def exact_json(actual, expected):
    """JSON equality with type fidelity: bool and integer are not interchangeable."""
    return json.dumps(actual, sort_keys=True, allow_nan=False) == json.dumps(expected, sort_keys=True, allow_nan=False)


def planned_inputs(stage, plan):
    """Pure metadata projection matching each pinned runner's authentication receipt."""
    inputs = {}
    def add(path, row):
        identity = {"path": path, "bytes": row["bytes"], "sha256": row["sha256"]}
        key = path.casefold()
        if key in inputs and not exact_json(inputs[key], identity):
            raise ValueError("conflicting planned input identity")
        inputs[key] = identity
    if stage != "audio":
        for row in plan["maps" if stage == "raw" else "extractions"]:
            for item in row["inputs"].values():
                add(item["path"], item)
        return sorted(inputs.values(), key=lambda row: row["path"])
    prefixes = {"{ORIGINALS}/work/shared-archives/": "shared/",
                "{ORIGINALS}/work/solo-retail-archives/": "solo/",
                "{ORIGINALS}/work/retail-archives/": "coop/"}
    extents = {}
    for step in plan["steps"]:
        for item in step.get("authenticated_inputs", []):
            if item["path"] == "{ISO}":
                continue
            matches = [(prefix, target) for prefix, target in prefixes.items() if item["path"].startswith(prefix)]
            if len(matches) != 1:
                raise ValueError("unrecognized planned audio archive root")
            prefix, target = matches[0]
            add(target + item["path"][len(prefix):], item)
        for row in [*step.get("authenticated_disc_extents", []),
                    *(item["input_extent"] for item in step.get("selected_input_spans", []))]:
            identity = {key: row[key] for key in ("offset", "bytes", "sha256")}
            key = row["offset"], row["bytes"]
            if key in extents and not exact_json(extents[key], identity):
                raise ValueError("conflicting planned disc extent")
            extents[key] = identity
    return {"iso": {key: plan["original_disc"][key] for key in ("sha256", "bytes")},
            "archives": sorted(inputs.values(), key=lambda row: row["path"]),
            "verified_disc_extents": [row for _, row in sorted(extents.items())]}


def audio_output_witnesses(step):
    option = "--output" if "--output" in step["argv"] else "--out"
    directory = step["argv"][step["argv"].index(option) + 1]
    if not directory.startswith("{NEW}/"):
        raise ValueError("audio output is not relative to the new workspace")
    prefix = directory[len("{NEW}/"):]
    return sorted(({"path": prefix + "/" + row["path"], "sha256": row["sha256"], "bytes": row["bytes"]}
                   for row in step["expected_outputs"]), key=lambda row: row["path"].casefold())


def completed_receipt(stage, output, context, exit_code):
    """Validate pinned-runner completion, never classify exit code alone as success."""
    data = checkout.safe_path(output, RECEIPTS[stage]).read_bytes()
    receipt = json.loads(data)
    if "failure_type" in receipt or "active_step" in receipt:
        raise ValueError("runner receipt is incomplete")
    plan = context["plans"][stage]
    identity = receipt.get("provenance" if stage == "audio" else "toolchain", {})
    lock_key = "toolchain_lock_sha256" if stage == "audio" else "lock_sha256"
    if (identity.get("source_commit") != context["source_commit"]
            or identity.get(lock_key) != context["toolchain_lock_sha256"]):
        raise ValueError("runner receipt toolchain differs from this session")
    if stage == "audio":
        if identity.get("bindings_sha256") != context["bindings_sha256"]:
            raise ValueError("audio receipt references other bindings")
    elif receipt.get("metadata_lock_sha256") != context["metadata_lock_sha256"]:
        raise ValueError("runner receipt references another metadata lock")
    if not exact_json(receipt.get("authenticated_inputs"), planned_inputs(stage, plan)):
        raise ValueError("authenticated input receipt differs from the exact planned identities")
    result = {"stage": stage, "status": receipt.get("status"), "exit_code": exit_code,
              "receipt_sha256": hashlib.sha256(data).hexdigest()}
    if stage == "raw":
        if receipt.get("schema") != "doom3-raw-structural-run-v1":
            raise ValueError("unsupported raw receipt")
        expected = {(row["mode"], row["map"], step["id"]) for row in plan["maps"] for step in row["steps"]}
        actual = unique_steps(receipt["steps"], lambda row: (row["mode"], row["map"], row["step"]))
        if actual != expected:
            raise ValueError("raw receipt does not contain every planned step")
        if any(type(row["historical_witness_verified"]) is not bool for row in receipt["steps"]):
            raise ValueError("historical witness result must be boolean")
        map_crcs = {(row["mode"], row["map"]): row["geometry_crc"] for row in receipt["steps"] if row["step"] == "map-crc"}
        if (set(map_crcs) != {(row["mode"], row["map"]) for row in plan["maps"]}
                or any(type(crc) is not int or not 0 <= crc <= 0xffffffff for crc in map_crcs.values())):
            raise ValueError("missing or invalid same-map geometry CRC")
        gaps = [row["mode"] + ":" + row["map"] + ":" + row["step"] for row in receipt["steps"]
                if not row["historical_witness_verified"]]
        if sorted(receipt["unwitnessed_steps"]) != sorted(gaps):
            raise ValueError("raw witness gap report is inconsistent")
        issues = receipt["companion_identity_issues"]
        actual_issues = []
        for row in receipt["steps"]:
            if row["step"] == "cm" or row["step"].startswith("aas"):
                witness = row["companion_identity"]
                if any(type(witness[k]) is not int or not 0 <= witness[k] <= 0xffffffff for k in ("map_crc", "header_crc")):
                    raise ValueError("invalid companion CRC identity")
                if witness["map_crc"] != map_crcs[(row["mode"], row["map"])]:
                    raise ValueError("companion map CRC differs from its own map-crc step")
                match = witness["map_crc"] == witness["header_crc"]
                if witness["matches"] is not match:
                    raise ValueError("inconsistent companion CRC result")
                if not match:
                    actual_issues.append({"mode": row["mode"], "map": row["map"], "step": row["step"],
                                          "map_crc": witness["map_crc"], "header_crc": witness["header_crc"]})
        if not exact_json(issues, actual_issues):
            raise ValueError("raw companion failure report is inconsistent")
        status = ("completed-with-companion-identity-failures" if issues else
                  "completed-with-witness-gaps" if gaps else "structural-witnesses-verified")
        if receipt["status"] != status or exit_code != int(bool(issues)):
            raise ValueError("raw exit/status does not describe a complete known result")
        result.update(steps=len(actual), witness_gaps=len(gaps), companion_identity_failures=len(issues))
    elif stage == "shared":
        if (receipt.get("schema") != "doom3-shared-resource-run-v1"
                or receipt["status"] != "original-member-witnesses-verified" or exit_code != 0):
            raise ValueError("shared extraction did not complete")
        expected = {row["id"]: row for row in plan["extractions"]}
        if unique_steps(receipt["results"], lambda row: row["id"]) != set(expected):
            raise ValueError("shared receipt does not contain every planned extraction")
        for row in receipt["results"]:
            members = expected[row["id"]]["expected_members"]
            if (not exact_json(row["members"], members) or type(row["verified_files"]) is not int
                    or row["verified_files"] != len(members)):
                raise ValueError("shared receipt member coverage differs from plan")
        if (type(receipt["extraction_roots"]) is not int or receipt["extraction_roots"] != len(expected)
                or type(receipt["verified_member_occurrences"]) is not int
                or receipt["verified_member_occurrences"] != sum(len(row["expected_members"]) for row in expected.values())):
            raise ValueError("shared receipt summary differs from plan")
        result["extractions"] = len(expected)
    else:
        if (receipt.get("schema") != "doom3-audio-texture-run-v1"
                or receipt["status"] != "historical-output-witnesses-verified" or exit_code != 0):
            raise ValueError("audio/texture recovery did not complete")
        if unique_steps(receipt["steps"], lambda row: row["id"]) != {row["id"] for row in plan["steps"]}:
            raise ValueError("audio receipt does not contain every planned step")
        if any(row["status"] != "historical-output-witnesses-verified" for row in receipt["steps"]):
            raise ValueError("audio step is incomplete")
        expected = {row["id"]: audio_output_witnesses(row) for row in plan["steps"]}
        for row in receipt["steps"]:
            if not exact_json(row["files"], expected[row["id"]]):
                raise ValueError("audio receipt output path/hash/size differs from planned witnesses")
        expected_summary = {"steps": len(expected), "files": sum(len(rows) for rows in expected.values()),
                            "target_entries": plan["summary"]["target_entries"],
                            "bound_target_entries": plan["summary"]["bound_entries"],
                            "unresolved_target_entries": plan["summary"]["unresolved_entries"]}
        if not exact_json(receipt["summary"], expected_summary):
            raise ValueError("audio receipt summary differs from plan")
        result["steps"] = len(receipt["steps"])
    return result


def recover(source, lock_name, iso, roots, parent, prefix="recovery", execute=False, git="git"):
    source, iso = absolute(source), absolute(iso)
    outputs, session_path = destinations(parent, prefix)
    checkout.verify(source, git=git, lock_name=lock_name)
    context = prepare(source, lock_name, iso, roots, outputs)
    for stage in STAGES:
        if run(context["commands"][stage], source) != 0:
            raise ValueError("preflight failed: " + stage + "; no conversion was started")
    # Preflight must not create any output; recheck before opening our receipt.
    outputs, session_path = destinations(parent, prefix)
    if not execute:
        return {"status": "preflight-only-no-output-created", "stages": list(STAGES)}, 0
    receipt = {"schema": "doom3-original-input-recovery-session-v1", "status": "incomplete",
               "source_commit": context["source_commit"], "toolchain_lock": lock_name,
               "toolchain_lock_sha256": context["toolchain_lock_sha256"],
               "outputs": {stage: path.name for stage, path in outputs.items()}, "stages": [],
               "limits": ["Recovery intermediates only; not final overlays or gameplay acceptance.",
                          "Original assets, converter outputs and private logs must not be published."]}
    with session_path.open("x+", encoding="utf-8", newline="\n") as stream:
        def persist():
            stream.seek(0)
            json.dump(receipt, stream, indent=2)
            stream.write("\n")
            stream.truncate()
            stream.flush()
            os.fsync(stream.fileno())
        persist()
        try:
            for stage in STAGES:
                receipt["active_stage"] = stage
                persist()
                code = run([*context["commands"][stage], "--execute"], source)
                if code != 0 and not (stage == "raw" and code == 1):
                    raise ValueError("recovery stage failed: " + stage)
                receipt["stages"].append(completed_receipt(stage, outputs[stage], context, code))
                persist()
            receipt.pop("active_stage", None)
            known = any(row.get("companion_identity_failures", 0) or row.get("witness_gaps", 0)
                        for row in receipt["stages"])
            receipt["status"] = "completed-with-known-issues" if known else "offline-input-recovery-completed"
            return receipt, int(known)
        except BaseException as error:
            receipt["failure_type"] = type(error).__name__
            raise
        finally:
            persist()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, required=True)
    parser.add_argument("--lock", default=checkout.LOCK, help="pipeline-relative versioned toolchain lock")
    parser.add_argument("--iso", type=Path, required=True)
    parser.add_argument("--archive-root", action="append", default=[], required=True,
                        help="repeat solo=DIR, coop=DIR and shared=DIR for authenticated originals")
    parser.add_argument("--output-parent", type=Path, required=True)
    parser.add_argument("--prefix", default="recovery")
    parser.add_argument("--git", default="git")
    parser.add_argument("--execute", action="store_true", help="convert only after all read-only preflights pass")
    args = parser.parse_args()
    try:
        result, code = recover(args.source, args.lock, args.iso, archive_roots(args.archive_root),
                               args.output_parent, args.prefix, args.execute, args.git)
        print(json.dumps(result, indent=2))
        return code
    except (OSError, ValueError, KeyError, TypeError, subprocess.CalledProcessError) as error:
        print("error: " + str(error), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
