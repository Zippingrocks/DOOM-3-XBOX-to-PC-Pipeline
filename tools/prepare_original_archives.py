#!/usr/bin/env python3
"""Prepare exactly 124 campaign archives from the pinned original ISO.

Default is read-only preflight. --execute extracts once per solo/coop/shared
group into PREFIX-solo, PREFIX-coop and PREFIX-shared under an existing parent.
All destinations must be fresh. No old ports, arbitrary argv, game, native
build, overwrite, deletion or upload. Raw extractor manifests/logs stay private;
the separate session receipt contains only logical identities and statuses.
"""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import tempfile
import uuid

sys.dont_write_bytecode = True
sys.pycache_prefix = str(Path(tempfile.gettempdir()) / ("doom3-archive-no-cache-" + uuid.uuid4().hex))
import verify_recovery_checkout as checkout

GROUPS = ("solo", "coop", "shared")
COUNTS = {"solo": 82, "coop": 40, "shared": 2}
SECTOR = 2048
MANIFEST = "xdvdfs-extraction-manifest.json"


def read_json(data):
    def pairs(values):
        result = {}
        for key, value in values:
            if key in result:
                raise ValueError("duplicate JSON key")
            result[key] = value
        return result
    return json.loads(data, object_pairs_hook=pairs,
                      parse_constant=lambda value: (_ for _ in ()).throw(ValueError("nonfinite JSON number")))


def equal(actual, expected):
    return json.dumps(actual, sort_keys=True, allow_nan=False) == json.dumps(expected, sort_keys=True, allow_nan=False)


def sha(value):
    if not isinstance(value, str) or not re.fullmatch(r"[0-9a-f]{64}", value):
        raise ValueError("invalid SHA-256")
    return value


def integer(value, minimum=0):
    if type(value) is not int or value < minimum:
        raise ValueError("invalid nonnegative integer")
    return value


def absolute(path):
    path = Path(os.path.abspath(path))
    return checkout.safe_path(path.parent, path.name)


def digest(path):
    result = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            result.update(block)
    return result.hexdigest()


def derive_groups(plan):
    if plan.get("schema") != "doom3-raw-structural-recipe-plan-v1":
        raise ValueError("unsupported structural plan")
    selected = {group: {} for group in GROUPS}
    maps = {"solo": set(), "coop": set()}
    for row in plan["maps"]:
        mode, name = row["mode"], row["map"]
        if mode not in maps or not re.fullmatch(r"[a-z][a-z0-9_]*", name) or name in maps[mode]:
            raise ValueError("invalid or duplicate planned campaign map")
        maps[mode].add(name)
        keys = set(row["inputs"])
        if keys not in ({"gfc", "gob"}, {"gfc", "gob", "shared_gfc", "shared_gob"}):
            raise ValueError("unexpected or missing original archive roles")
        for role, item in row["inputs"].items():
            group = "shared" if role.startswith("shared_") else mode
            member = ("assets" if group == "shared" else name) + "." + role.removeprefix("shared_")
            if item["path"] != "{ARCHIVES}/" + group + "/" + member or item["disc_member"] != member:
                raise ValueError("archive target/member does not match its canonical role")
            identity = {"member": member, "bytes": integer(item["bytes"], 1), "sha256": sha(item["sha256"])}
            previous = selected[group].get(member.casefold())
            if previous is not None and not equal(previous, identity):
                raise ValueError("conflicting duplicate original archive identity")
            selected[group][member.casefold()] = identity
    if {key: len(value) for key, value in maps.items()} != {"solo": 41, "coop": 20}:
        raise ValueError("structural plan must contain exactly 41 solo and 20 co-op maps")
    groups = {group: sorted(rows.values(), key=lambda row: row["member"]) for group, rows in selected.items()}
    if {group: len(rows) for group, rows in groups.items()} != COUNTS:
        raise ValueError("structural plan must select exactly 124 original archive files")
    all_names = [row["member"].casefold() for rows in groups.values() for row in rows]
    if len(set(all_names)) != 124:
        raise ValueError("disc member reused across archive groups")
    return groups


def context_from_lock(lock_name):
    lock_data = checkout.safe_path(checkout.PIPELINE, lock_name).read_bytes()
    lock = read_json(lock_data)
    plan_data = checkout.bound_artifact(lock, "structural_plan").read_bytes()
    inventory_data = checkout.bound_artifact(lock, "metadata_lock").read_bytes()
    bindings_data = checkout.bound_artifact(lock, "audio_texture_bindings").read_bytes()
    bindings, inventory = read_json(bindings_data), read_json(inventory_data)
    if bindings.get("metadata_lock_sha256") != hashlib.sha256(inventory_data).hexdigest():
        raise ValueError("ISO bindings reference another metadata lock")
    original = bindings["original_disc"]
    witness = original["inventory_receipt"]
    records = [row for row in inventory["records"] if row["root"] == witness["root"] and row["path"] == witness["path"]]
    if len(records) != 1 or any(records[0][key] != witness[key] for key in ("bytes", "sha256")):
        raise ValueError("original ISO inventory witness is not uniquely bound")
    return {"source_commit": lock["source_commit"], "toolchain_lock_sha256": hashlib.sha256(lock_data).hexdigest(),
            "structural_plan_sha256": hashlib.sha256(plan_data).hexdigest(),
            "iso": {"bytes": integer(original["bytes"], 1), "sha256": sha(original["sha256"])},
            "inventory": records[0]["metadata"], "groups": derive_groups(read_json(plan_data))}


def fresh_paths(parent, prefix, source, iso):
    parent = absolute(parent)
    if not parent.is_dir() or not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9_-]{0,47}", prefix):
        raise ValueError("existing output parent and safe 1-48 character ASCII prefix are required")
    paths = {group: checkout.safe_path(parent, prefix + "-" + group) for group in (*GROUPS, "logs")}
    paths["session"] = checkout.safe_path(parent, prefix + "-session.json")
    for path in paths.values():
        if path.exists() or path.is_symlink():
            raise ValueError("preparation output already exists; no overwrite or resume")
        for protected in (source, checkout.PIPELINE):
            if path.is_relative_to(protected) or protected.is_relative_to(path):
                raise ValueError("preparation output overlaps a source checkout")
        if iso == path or iso.is_relative_to(path):
            raise ValueError("preparation output overlaps the original ISO")
    return paths


def load_inventory_reader(source):
    path = checkout.safe_path(source, "tools/campaign_port/xdvdfs.py")
    name = "_doom3_archive_inventory_" + uuid.uuid4().hex
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    if module.SECTOR != SECTOR:
        raise ValueError("unsupported pinned ISO sector size")
    return module.inventory


def authenticate_iso(iso, identity):
    iso = absolute(iso)
    if not iso.is_file() or iso.stat().st_size != identity["bytes"] or digest(iso) != identity["sha256"]:
        raise ValueError("original ISO identity mismatch")


def selected_extents(inventory, groups, iso_size):
    if inventory.get("kind") != "xdvdfs-inventory":
        raise ValueError("unsupported ISO inventory")
    entries = {}
    for row in inventory["entries"]:
        # The locked metadata projection omits the names of two directory
        # records. Directories cannot be any of the 124 selected root files.
        if "path" not in row and row.get("directory") is True:
            continue
        name = row["path"]
        if not isinstance(name, str) or name.casefold() in entries:
            raise ValueError("duplicate or invalid ISO member")
        entries[name.casefold()] = row
    chosen = {}
    for rows in groups.values():
        for item in rows:
            row = entries.get(item["member"].casefold())
            if row is None or row["path"] != item["member"] or row["directory"] is not False:
                raise ValueError("missing or case-aliased original archive member")
            size, offset = integer(row["size"], 1), integer(row["sector"]) * SECTOR
            if size != item["bytes"] or offset + size > iso_size:
                raise ValueError("archive size/extent does not fit original ISO")
            chosen[item["member"]] = {key: row[key] for key in
                                      ("path", "sector", "size", "attributes", "directory", "descriptor_offset")}
    return chosen


def preflight(iso, context, inventory_reader):
    authenticate_iso(iso, context["iso"])
    expected = selected_extents(context["inventory"], context["groups"], context["iso"]["bytes"])
    current = inventory_reader(iso)
    if not equal(current["image"], context["iso"]) or current["volume"]["sector_size"] != SECTOR:
        raise ValueError("current ISO inventory identity differs from locked source")
    if not equal(selected_extents(current, context["groups"], context["iso"]["bytes"]), expected):
        raise ValueError("current archive extents differ from locked ISO inventory")
    with iso.open("rb") as stream:
        for rows in context["groups"].values():
            for row in rows:
                stream.seek(expected[row["member"]]["sector"] * SECTOR)
                remaining, result = row["bytes"], hashlib.sha256()
                while remaining:
                    block = stream.read(min(remaining, 1024 * 1024))
                    if not block:
                        raise ValueError("short original archive extent")
                    result.update(block)
                    remaining -= len(block)
                if result.hexdigest() != row["sha256"]:
                    raise ValueError("original archive extent hash differs from plan")
    return expected


def extract_group(source, iso, destination, members, log):
    command = [sys.executable, "-E", "-s", "-B", "-X", "pycache_prefix=" + sys.pycache_prefix,
               str(checkout.safe_path(source, "tools/campaign_port/xdvdfs.py")), "extract", str(iso),
               "--out", str(destination)]
    for row in members:
        command.extend(("--include", row["member"]))
    with log.open("xb") as stream:
        subprocess.run(command, cwd=source, check=True, shell=False, stdin=subprocess.DEVNULL,
                       stdout=stream, stderr=subprocess.STDOUT,
                       creationflags=0x08000000 if os.name == "nt" else 0)


def verify_group(group, destination, members, expected_extents, iso_identity):
    manifest = read_json(checkout.safe_path(destination, MANIFEST).read_bytes())
    if manifest.get("kind") != "xdvdfs-extraction" or not equal(manifest.get("image"), iso_identity):
        raise ValueError("extractor receipt references a different original ISO")
    expected = [{**expected_extents[row["member"]], "sha256": row["sha256"]} for row in members]
    if not equal(sorted(manifest["files"], key=lambda row: row["path"]), expected):
        raise ValueError("extractor receipt member set/identities differ from plan")
    paths = list(destination.rglob("*"))
    for path in paths:
        checkout.safe_path(destination, path.relative_to(destination).as_posix())
        if not path.is_file():
            raise ValueError("unexpected directory in flat original archive output")
    if {path.name for path in paths} != {MANIFEST, *(row["member"] for row in members)} or len(paths) != len(members) + 1:
        raise ValueError("unexpected or missing physical original archive file")
    verified = []
    for row in members:
        path = checkout.safe_path(destination, row["member"])
        if path.stat().st_size != row["bytes"] or digest(path) != row["sha256"]:
            raise ValueError("extracted original archive differs from pinned witness")
        verified.append({"path": group + "/" + row["member"], "bytes": row["bytes"], "sha256": row["sha256"]})
    return {"group": group, "status": "original-archive-witnesses-verified", "archives": verified}


def prepare(source, lock_name, iso, parent, prefix="originals", execute=False, git="git"):
    source, iso = absolute(source), absolute(iso)
    paths = fresh_paths(parent, prefix, source, iso)
    checkout.verify(source, git=git, lock_name=lock_name)
    context = context_from_lock(lock_name)
    extents = preflight(iso, context, load_inventory_reader(source))
    paths = fresh_paths(parent, prefix, source, iso)
    if not execute:
        return {"status": "preflight-only-no-output-created", "archives_verified": 124, "groups": COUNTS,
                "original_iso": context["iso"]}
    receipt = {"schema": "doom3-original-archive-preparation-v1", "status": "incomplete",
               "source_commit": context["source_commit"], "toolchain_lock_sha256": context["toolchain_lock_sha256"],
               "structural_plan_sha256": context["structural_plan_sha256"], "original_iso": context["iso"],
               "outputs": {group: paths[group].name for group in GROUPS}, "groups": [],
               "limits": ["Original archive preparation only, not decoded maps or final overlays.",
                          "Original archives and raw extractor manifests/logs must remain private."]}
    with paths["session"].open("x+", encoding="utf-8", newline="\n") as stream:
        def persist():
            stream.seek(0); json.dump(receipt, stream, indent=2); stream.write("\n")
            stream.truncate(); stream.flush(); os.fsync(stream.fileno())
        persist()
        try:
            paths["logs"].mkdir()
            for group in GROUPS:
                receipt["active_group"] = group; persist()
                extract_group(source, iso, paths[group], context["groups"][group], paths["logs"] / (group + ".log"))
                receipt["groups"].append(verify_group(group, paths[group], context["groups"][group], extents, context["iso"]))
                persist()
            authenticate_iso(iso, context["iso"])
            receipt.pop("active_group", None)
            receipt["status"] = "original-archive-witnesses-verified"
            receipt["archives_verified"] = sum(len(row["archives"]) for row in receipt["groups"])
            return receipt
        except BaseException as error:
            receipt["failure_type"] = type(error).__name__
            raise
        finally:
            persist()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, required=True)
    parser.add_argument("--lock", default=checkout.LOCK, help="pipeline-relative resource toolchain lock")
    parser.add_argument("--iso", type=Path, required=True)
    parser.add_argument("--output-parent", type=Path, required=True)
    parser.add_argument("--prefix", default="originals")
    parser.add_argument("--git", default="git")
    parser.add_argument("--execute", action="store_true", help="opt in to three exact archive extractions after preflight")
    args = parser.parse_args()
    try:
        result = prepare(args.source, args.lock, args.iso, args.output_parent, args.prefix, args.execute, args.git)
        print(json.dumps({key: result[key] for key in ("status", "archives_verified")}, indent=2))
        return 0
    except (OSError, ValueError, KeyError, TypeError, subprocess.CalledProcessError) as error:
        print("error: " + str(error), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
