#!/usr/bin/env python3
"""Asset-free checkout/recipe verification. Does not find or open game inputs.

Use a trusted checkout. This checks reproducibility identities, not hostile-code
isolation. No downloads, package installs, conversions, or game launches occur.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import re
import stat
import subprocess
import sys
import tempfile

PIPELINE = Path(__file__).resolve().parents[1]
LOCK = "evidence/checkpoint-087-resource-toolchain-lock.json"


def safe_path(root: Path, relative: str) -> Path:
    parts = relative.split("/")
    if (not relative or PurePosixPath(relative).is_absolute() or "\\" in relative
            or ":" in relative or any(p in {"", ".", ".."} or p.endswith((".", " ")) for p in parts)):
        raise ValueError("unsafe lock-relative path")
    path = root.joinpath(*parts)
    for item in [*reversed(path.parents), path]:
        if item.exists() or item.is_symlink():
            if item.is_symlink() or getattr(item.lstat(), "st_file_attributes", 0) & getattr(stat, "FILE_ATTRIBUTE_REPARSE_POINT", 0x400):
                raise ValueError("reparse point in selected checkout")
    return path


def verify_files(root: Path, records: list[dict]) -> None:
    seen = set()
    if not records:
        raise ValueError("empty identity list")
    for row in records:
        key = row["path"].casefold()
        if key in seen:
            raise ValueError("duplicate identity")
        seen.add(key)
        data = safe_path(root, row["path"]).read_bytes()
        if row.get("mode", "bytes") == "lf":
            data = data.replace(b"\r\n", b"\n")
        elif row.get("mode", "bytes") != "bytes":
            raise ValueError("unknown byte identity mode")
        if len(data) != row["bytes"] or hashlib.sha256(data).hexdigest() != row["sha256"]:
            raise ValueError("file identity mismatch: " + row["path"])


def run(command: list[str], cwd: Path) -> None:
    subprocess.run(command, cwd=cwd, check=True, shell=False, stdin=subprocess.DEVNULL,
                   creationflags=0x08000000 if os.name == "nt" else 0)


def bound_artifact(lock: dict, name: str) -> Path:
    path = safe_path(PIPELINE, lock[name])
    matches = [row for row in lock["pipeline_artifacts"] if row["path"] == lock[name]]
    if len(matches) != 1:
        raise ValueError("recipe reference must have exactly one verified artifact identity")
    return path


def resource_artifacts(lock: dict) -> dict[str, Path]:
    fields = ("shared_resource_plan", "audio_texture_bindings", "audio_texture_plan")
    if ("audio_texture_bindings" in lock) != ("audio_texture_plan" in lock):
        raise ValueError("audio bindings and plan must be locked together")
    return {name: bound_artifact(lock, name) for name in fields if name in lock}


def verify_producer_bindings(source: Path, bindings: dict) -> None:
    rows = bindings.get("current_recipe_tools")
    if not isinstance(rows, list) or not rows:
        raise ValueError("audio bindings have no producer source identities")
    seen = set()
    for row in rows:
        name = row["path"]
        if name.casefold() in seen or row.get("mode") != "lf":
            raise ValueError("duplicate or invalid producer identity")
        seen.add(name.casefold())
        data = safe_path(source, name).read_bytes().replace(b"\r\n", b"\n")
        if hashlib.sha256(data).hexdigest() != row["sha256"]:
            raise ValueError("audio producer source differs from captured bindings")


def verify(source: Path, tests: bool = False, git: str = "git", lock_name: str = LOCK) -> dict:
    lock_data = safe_path(PIPELINE, lock_name).read_bytes()
    lock = json.loads(lock_data)
    if lock.get("schema") != "doom3-recovery-toolchain-lock-v1" or not re.fullmatch(r"[0-9a-f]{40}", lock.get("source_commit", "")):
        raise ValueError("unsupported source/toolchain lock")
    verify_files(PIPELINE, lock["pipeline_artifacts"])
    verify_files(source, lock["files"])
    metadata_path = bound_artifact(lock, "metadata_lock")
    plan_path = bound_artifact(lock, "structural_plan")
    provenance_path = bound_artifact(lock, "provenance_trace")
    resources = resource_artifacts(lock)
    commit = subprocess.check_output([git, "-c", "safe.directory=" + str(source), "-C", str(source),
                                      "rev-parse", "HEAD"], text=True).strip()
    if commit != lock["source_commit"]:
        raise ValueError("wrong source commit; use pinned master lineage, not source main")
    with tempfile.TemporaryDirectory(prefix="doom3-recipe-proof-") as folder:
        # Ignore existing bytecode caches; -B alone only disables cache writes.
        sys.dont_write_bytecode = True
        sys.pycache_prefix = str(Path(folder) / "isolated-python-cache")
        # All source bytes are checked before importing even the verifier helper.
        sys.path.insert(0, str(source / "tools/campaign_port"))
        import recovery_toolchain
        recovery_toolchain.verify(source, lock)
        python = [sys.executable, "-E", "-s", "-B", "-X", "pycache_prefix=" + sys.pycache_prefix]
        output = Path(folder) / "plan.json"
        run([*python, str(source / "tools/campaign_port/plan_raw_structural_recipes.py"),
             "--inventory", str(metadata_path), "--output", str(output),
             "--require-solo", "41", "--require-coop", "20"], Path(folder))
        expected = plan_path.read_bytes()
        if output.read_bytes() != expected:
            raise ValueError("metadata-only plan regeneration is not byte-identical")
        trace_output = Path(folder) / "trace.json"
        run([*python, str(source / "tools/campaign_port/trace_recovery_provenance.py"),
             "--inventory", str(metadata_path), "--output", str(trace_output),
             "--require-solo", "41", "--require-coop", "20"], Path(folder))
        if trace_output.read_bytes() != provenance_path.read_bytes():
            raise ValueError("metadata-only provenance regeneration is not byte-identical")
        if "shared_resource_plan" in resources:
            shared_output = Path(folder) / "shared.json"
            run([*python, str(source / "tools/campaign_port/plan_shared_resource_recipes.py"),
                 "--inventory", str(metadata_path), "--output", str(shared_output)], Path(folder))
            if shared_output.read_bytes() != resources["shared_resource_plan"].read_bytes():
                raise ValueError("shared-resource plan regeneration is not byte-identical")
        if "audio_texture_bindings" in resources:
            bindings = json.loads(resources["audio_texture_bindings"].read_bytes())
            if bindings.get("metadata_lock_sha256") != hashlib.sha256(metadata_path.read_bytes()).hexdigest():
                raise ValueError("audio bindings reference another metadata lock")
            verify_producer_bindings(source, bindings)
            audio_output = Path(folder) / "audio.json"
            run([*python, str(source / "tools/campaign_port/audio_texture_recovery_recipes.py"),
                 "plan", "--bindings", str(resources["audio_texture_bindings"]),
                 "--output", str(audio_output)], Path(folder))
            if audio_output.read_bytes() != resources["audio_texture_plan"].read_bytes():
                raise ValueError("audio/texture plan regeneration is not byte-identical")
        if tests:
            run([*python, "-m", "unittest", "discover", "-s",
                 "tools/campaign_port/tests", "-p", "test_*.py", "-q"], source)
    return {"status": "asset-free-verification-passed", "source_commit": commit,
            "toolchain_lock": lock_name, "toolchain_lock_sha256": hashlib.sha256(lock_data).hexdigest(),
            "source_files_verified": len(lock["files"]),
            "pipeline_artifacts_verified": len(lock["pipeline_artifacts"]),
            "plan_byte_identical": True, "provenance_byte_identical": True,
            "optional_resource_artifacts_verified": sorted(resources),
            "offline_tests_requested": tests,
            "python": sys.version.split()[0], "game_inputs_opened": 0,
            "converted_assets_written": 0, "full_rebuild_proved": False}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, required=True)
    parser.add_argument("--tests", action="store_true")
    parser.add_argument("--git", default="git")
    parser.add_argument("--lock", default=LOCK, help="pipeline-relative versioned toolchain lock")
    args = parser.parse_args()
    try:
        result = verify(Path(os.path.abspath(args.source)), args.tests, args.git, args.lock)
        print(json.dumps(result, indent=2))
        return 0
    except (OSError, ValueError, KeyError, subprocess.CalledProcessError) as error:
        print("error: " + str(error), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
