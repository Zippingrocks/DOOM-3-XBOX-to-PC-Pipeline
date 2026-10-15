#!/usr/bin/env python3
"""Publish an allowlisted, metadata-only projection of a completed resource run.

The caller supplies a trusted toolchain lock. Only the three explicit JSON files
are read; no source checkout, original archive, generated payload or log is read.
This checks receipt consistency, not the truth of an execution claim. It neither
executes recipes nor independently verifies the payloads described by a receipt.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import re
import stat
import sys


SHARED_PLAN = "doom3-shared-resource-recipe-plan-v1"
AUDIO_PLAN = "doom3-audio-texture-recovery-plan-v1"
SHARED_STATUS = "original-member-witnesses-verified"
AUDIO_STATUS = "historical-output-witnesses-verified"
TOOLS = {"doom3_campaign_port.py", "xdvdfs.py", "xact_audio.py", "d3tfull.py"}
PREFIXES = {"work/shared-archives/": "shared/", "work/solo-retail-archives/": "solo/",
            "work/retail-archives/": "coop/"}


def require(condition, message):
    if not condition:
        raise ValueError(message)


def number(value):
    require(type(value) is int and value >= 0, "invalid nonnegative integer")
    return value


def sha(value, length=64):
    require(isinstance(value, str) and re.fullmatch(r"[0-9a-f]{%d}" % length, value), "invalid digest")
    return value


def logical(value):
    require(isinstance(value, str) and re.fullmatch(r"[A-Za-z0-9_./-]+", value), "invalid logical path")
    require(all(p not in {"", ".", ".."} and not p.endswith(".") for p in value.split("/")),
            "invalid logical path component")
    return value


def identifier(value):
    require(isinstance(value, str) and re.fullmatch(r"[a-z][a-z0-9_-]*", value), "invalid logical ID")
    return value


def rows(value, nonempty=False):
    require(isinstance(value, list) and (value or not nonempty), "invalid record list")
    return value


def same_count(actual, expected):
    require(number(actual) == expected, "count differs from selected plan")


def digest(data):
    return hashlib.sha256(data).hexdigest()


def load(data):
    def pairs(items):
        result = {}
        for key, value in items:
            require(key not in result, "duplicate JSON key")
            result[key] = value
        return result

    def constant(_):
        raise ValueError("nonfinite JSON number")

    value = json.loads(data, object_pairs_hook=pairs, parse_constant=constant)
    require(isinstance(value, dict), "JSON document must be an object")
    return value


def identity(row, path=None):
    return {"path": logical(row["path"] if path is None else path),
            "sha256": sha(row["sha256"]), "bytes": number(row["bytes"])}


def file_set(items):
    result = {}
    for item in rows(items):
        record = identity(item)
        key = record["path"].casefold()
        require(key not in result, "duplicate file identity")
        result[key] = record
    return result


def add_identity(result, record):
    key = record["path"].casefold()
    require(key not in result or result[key] == record, "conflicting original identity")
    result[key] = record


def bound(lock, field):
    path = logical(lock[field])
    records = [identity(row) for row in rows(lock["pipeline_artifacts"], True)]
    file_set(records)
    matches = [row for row in records if row["path"] == path]
    require(len(matches) == 1, "artifact must have exactly one locked identity")
    return matches[0]


def toolchain(lock, lock_data, receipt, kind):
    require(lock.get("schema") == "doom3-recovery-toolchain-lock-v1", "unsupported toolchain lock")
    commit = sha(lock["source_commit"], 40)
    files = file_set(rows(lock["files"], True))
    for item in lock["files"]:
        require(item.get("mode", "bytes") in {"lf", "bytes"}, "invalid source identity mode")
    if kind == "shared":
        recorded = receipt["toolchain"]
        require(recorded["source_commit"] == commit and recorded["lock_sha256"] == digest(lock_data),
                "receipt toolchain identity mismatch")
        same_count(recorded["files_verified"], len(files))
    else:
        recorded = receipt["provenance"]
        require(recorded["source_commit"] == commit and recorded["toolchain_lock_sha256"] == digest(lock_data),
                "receipt toolchain identity mismatch")
        same_count(recorded["toolchain_files_verified"], len(files))
    return {"source_commit": commit, "files_verified": len(files), "lock_sha256": digest(lock_data)}


def shared(receipt, plan):
    require(receipt.get("schema") == "doom3-shared-resource-run-v1" and receipt.get("status") == SHARED_STATUS,
            "shared receipt is not complete")
    expected_inputs, output_steps, seen = {}, [], set()
    expected_rows = rows(plan["extractions"], True)
    actual_rows = rows(receipt["results"])
    same_count(len(actual_rows), len(expected_rows))
    for expected, actual in zip(expected_rows, actual_rows):
        step_id = identifier(expected["id"])
        require(step_id not in seen and actual["id"] == step_id, "shared step order or identity mismatch")
        seen.add(step_id)
        for item in expected["inputs"].values():
            token = item["path"]
            require(isinstance(token, str) and token.startswith("{ARCHIVES}/"), "invalid archive root token")
            add_identity(expected_inputs, identity(item, token[len("{ARCHIVES}/"):]))
        members = rows(expected["expected_members"], True)
        expected_files = file_set(members)
        actual_members = rows(actual["members"])
        require(file_set(actual_members) == expected_files, "shared member identities mismatch")
        for member in [*members, *actual_members]:
            require(member["member"] == "./" + logical(member["path"]), "shared member selector mismatch")
        same_count(actual["verified_files"], len(expected_files))
        output_steps.append({"id": step_id, "status": SHARED_STATUS,
                             "files": [expected_files[key] for key in sorted(expected_files)]})
    actual_inputs = []
    for item in rows(receipt["authenticated_inputs"]):
        token = item["path"]
        require(isinstance(token, str) and token.startswith("{ARCHIVES}/"), "invalid authenticated archive token")
        actual_inputs.append(identity(item, token[len("{ARCHIVES}/"):]))
    require(file_set(actual_inputs) == expected_inputs, "shared authenticated original set mismatch")
    count = sum(len(row["files"]) for row in output_steps)
    for summary, root_key, count_key in ((receipt, "extraction_roots", "verified_member_occurrences"),
                                         (plan["summary"], "extraction_roots", "selected_member_occurrences")):
        same_count(summary[root_key], len(output_steps))
        same_count(summary[count_key], count)
    same_count(plan["summary"]["original_archive_files"], len(expected_inputs))
    return {"archives": [expected_inputs[key] for key in sorted(expected_inputs)]}, output_steps, {
        "extraction_roots": len(output_steps), "verified_member_occurrences": count,
        "original_archive_files": len(expected_inputs)}


def archive_identity(item):
    token = item["path"]
    require(isinstance(token, str) and token.startswith("{ORIGINALS}/"), "invalid original root token")
    name = token[len("{ORIGINALS}/"):]
    for prefix, replacement in PREFIXES.items():
        if name.startswith(prefix):
            return identity(item, replacement + logical(name[len(prefix):]))
    raise ValueError("unrecognized original archive layout")


def output_root(step):
    argv = rows(step["argv"], True)
    require(len(argv) > 2 and argv[0] == "{PYTHON}" and isinstance(argv[1], str), "invalid canonical command")
    tools = {"{SOURCE}/tools/campaign_port/" + name: name for name in TOOLS}
    require(argv[1] in tools, "unrecognized canonical converter")
    option = "--output" if tools[argv[1]] in {"xact_audio.py", "d3tfull.py"} else "--out"
    require(argv.count(option) == 1, "ambiguous output option")
    index = argv.index(option) + 1
    require(index < len(argv) and isinstance(argv[index], str) and argv[index].startswith("{NEW}/"),
            "invalid output root")
    return logical(argv[index][len("{NEW}/"):])


def extent(item, iso_size):
    record = {"offset": number(item["offset"]), "bytes": number(item["bytes"]), "sha256": sha(item["sha256"])}
    require(record["bytes"] > 0 and record["offset"] + record["bytes"] <= iso_size, "extent outside pinned ISO")
    return record


def extent_set(items, iso_size, allow_repeated=False):
    result = {}
    for item in rows(items):
        record = extent(item, iso_size)
        key = record["offset"], record["bytes"]
        require(key not in result or (allow_repeated and result[key] == record), "duplicate or conflicting extent")
        result[key] = record
    return result


def audio(receipt, plan, lock):
    require(receipt.get("schema") == "doom3-audio-texture-run-v1" and receipt.get("status") == AUDIO_STATUS,
            "audio/texture receipt is not complete")
    binding = bound(lock, "audio_texture_bindings")["sha256"]
    require(plan["bindings_sha256"] == binding and receipt["provenance"]["bindings_sha256"] == binding,
            "audio binding identity mismatch")
    locked_tools = {row["path"]: row for row in lock["files"]}
    expected_tools = {"tools/campaign_port/" + name for name in TOOLS}
    seen_tools = set()
    for row in rows(plan["producer_tools"], True):
        name = logical(row["path"])
        require(name in expected_tools and name not in seen_tools, "invalid producer identity set")
        seen_tools.add(name)
        require(row["mode"] == "lf" and locked_tools[name]["mode"] == "lf"
                and sha(row["sha256"]) == locked_tools[name]["sha256"], "producer not bound to toolchain")
    require(seen_tools == expected_tools, "incomplete producer identity set")
    disc = plan["original_disc"]
    require(disc["path"] == "{ISO}", "invalid original disc token")
    iso = {"sha256": sha(disc["sha256"]), "bytes": number(disc["bytes"])}
    require(iso["bytes"] > 0, "empty original disc")
    expected_inputs, extents, output_steps, done, global_files, available = {}, [], [], set(), set(), set()
    expected_rows, actual_rows = rows(plan["steps"], True), rows(receipt["steps"])
    same_count(len(actual_rows), len(expected_rows))
    for expected, actual in zip(expected_rows, actual_rows):
        step_id = identifier(expected["id"])
        require(re.fullmatch(r"(?:input|audio|texture)-[0-9]+", step_id), "unknown audio step ID")
        require(step_id not in done and actual["id"] == step_id and actual["status"] == AUDIO_STATUS,
                "audio step order, identity or status mismatch")
        dependencies = rows(expected["requires"])
        require(len(set(dependencies)) == len(dependencies) and set(dependencies) <= done,
                "unsatisfied or duplicate planned dependency")
        done.add(step_id)
        for item in rows(expected.get("authenticated_inputs", [])):
            if item["path"] == "{ISO}":
                require({"sha256": sha(item["sha256"]), "bytes": number(item["bytes"])} == iso,
                        "conflicting original disc identity")
            else:
                add_identity(expected_inputs, archive_identity(item))
        extents.extend(rows(expected.get("authenticated_disc_extents", [])))
        extents.extend(item["input_extent"] for item in rows(expected.get("selected_input_spans", [])))
        root = output_root(expected)
        expected_files = []
        for item in rows(expected["expected_outputs"], True):
            relative = logical(item["path"])
            record = identity(item, root + "/" + relative)
            require(record["path"].casefold() not in global_files, "overlapping planned output files")
            global_files.add(record["path"].casefold())
            expected_files.append(record)
            available.add((step_id, relative.casefold(), record["sha256"]))
        require(file_set(actual["files"]) == file_set(expected_files), "audio output identities mismatch")
        output_steps.append({"id": step_id, "status": AUDIO_STATUS,
                             "files": sorted(expected_files, key=lambda row: row["path"].casefold())})
    expected_extents = extent_set(extents, iso["bytes"], True)
    recorded = receipt["authenticated_inputs"]
    require({"sha256": sha(recorded["iso"]["sha256"]), "bytes": number(recorded["iso"]["bytes"])} == iso,
            "authenticated original disc mismatch")
    require(file_set(recorded["archives"]) == expected_inputs, "audio authenticated archive set mismatch")
    require(extent_set(recorded["verified_disc_extents"], iso["bytes"]) == expected_extents,
            "audio authenticated extent set mismatch")
    target_ids, bound_targets = set(), 0
    targets = rows(plan["targets"], True)
    for target in targets:
        require(target["mode"] in {"solo", "coop"}, "invalid target mode")
        key = target["mode"], identifier(target["map"]), logical(target["path"]).casefold()
        require(key not in target_ids, "duplicate selected target")
        target_ids.add(key)
        target_sha = sha(target["sha256"])
        producer = target["recipe_id"]
        if producer is not None:
            require(isinstance(producer, str) and producer.startswith(("audio-", "texture-"))
                    and (producer, key[2], target_sha) in available, "target has no matching producer output")
            bound_targets += 1
    count = sum(len(row["files"]) for row in output_steps)
    summary = {"steps": len(output_steps), "files": count, "target_entries": len(targets),
               "bound_target_entries": bound_targets, "unresolved_target_entries": len(targets) - bound_targets}
    for key, value in summary.items():
        same_count(receipt["summary"][key], value)
    for key, value in {"steps": len(output_steps), "producer_steps": sum(not i.startswith("input-") for i in done),
                       "target_entries": len(targets), "bound_entries": bound_targets,
                       "unresolved_entries": len(targets) - bound_targets}.items():
        same_count(plan["summary"][key], value)
    summary.update(original_archive_files=len(expected_inputs), verified_disc_extents=len(expected_extents))
    return {"iso": iso, "archives": [expected_inputs[key] for key in sorted(expected_inputs)],
            "verified_disc_extents": [expected_extents[key] for key in sorted(expected_extents)]}, output_steps, summary


def publish(receipt_data: bytes, toolchain_data: bytes, plan_data: bytes) -> dict:
    """Validate explicit metadata bytes and return only typed public fields."""
    try:
        receipt, lock, plan = load(receipt_data), load(toolchain_data), load(plan_data)
        require("failure_type" not in receipt and "active_step" not in receipt, "receipt retains failure or active step")
        require(plan.get("schema") in {SHARED_PLAN, AUDIO_PLAN}, "unsupported resource plan")
        kind = "shared" if plan["schema"] == SHARED_PLAN else "audio-texture"
        chain = toolchain(lock, toolchain_data, receipt, kind)
        artifact = bound(lock, "shared_resource_plan" if kind == "shared" else "audio_texture_plan")
        require(artifact["bytes"] == len(plan_data) and artifact["sha256"] == digest(plan_data), "plan differs from lock")
        inventory_sha = bound(lock, "metadata_lock")["sha256"]
        if kind == "shared":
            require(receipt["metadata_lock_sha256"] == inventory_sha, "metadata lock identity mismatch")
            inputs, steps, summary = shared(receipt, plan)
        else:
            inputs, steps, summary = audio(receipt, plan, lock)
        proof = {"schema": "doom3-resource-run-proof-v1", "kind": kind,
                 "status": SHARED_STATUS if kind == "shared" else AUDIO_STATUS,
                 "receipt_sha256": digest(receipt_data), "toolchain": chain,
                 "plan_sha256": digest(plan_data), "metadata_lock_sha256": inventory_sha,
                 "authenticated_inputs": inputs, "steps": steps, "summary": summary,
                 "publication_checks": {"exact_planned_steps": True, "exact_planned_output_identities": True,
                                        "exact_planned_input_identities": True, "payload_files_opened": 0,
                                        "independent_payload_verification": False, "final_overlay_equivalence": False},
                 "limits": ["Typed projection of a completed execution receipt, not independent payload verification.",
                            "No commands, logs, local paths or payload content are published.",
                            "Original-member and historical-output witnesses do not establish final-overlay or gameplay acceptance."]}
        if kind == "audio-texture":
            proof["bindings_sha256"] = bound(lock, "audio_texture_bindings")["sha256"]
        return proof
    except (KeyError, TypeError, IndexError, AttributeError) as error:
        raise ValueError("malformed resource proof metadata") from error


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--receipt", type=Path, required=True)
    parser.add_argument("--toolchain-lock", type=Path, required=True)
    parser.add_argument("--plan", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args(argv)
    try:
        proof = publish(args.receipt.read_bytes(), args.toolchain_lock.read_bytes(), args.plan.read_bytes())
        output = args.output.absolute()
        require(output.parent.is_dir(), "output parent must already exist")
        for path in [output, *output.parents]:
            if path.exists() or path.is_symlink():
                require(not path.is_symlink() and not getattr(path.lstat(), "st_file_attributes", 0)
                        & getattr(stat, "FILE_ATTRIBUTE_REPARSE_POINT", 0x400), "reparse point in output path")
        with output.open("x", encoding="utf-8", newline="\n") as stream:
            json.dump(proof, stream, indent=2)
            stream.write("\n")
        print(json.dumps({"status": proof["status"], **proof["summary"]}))
        return 0
    except (OSError, ValueError) as error:
        # Error details and filenames may themselves contain private strings.
        print("error: resource publication rejected (" + type(error).__name__ + ")", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
