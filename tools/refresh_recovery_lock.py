#!/usr/bin/env python3
"""Maintainer-only metadata lock creation after a reviewed, committed tool change.

Never run merely to bypass verification failures. No game inputs are accessed.
"""
import argparse
import hashlib
import json
from pathlib import Path
import subprocess
import sys

PIPELINE = Path(__file__).resolve().parents[1]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--git", default="git")
    args = parser.parse_args()
    if args.output.exists() or args.output.is_symlink():
        raise ValueError("refusing to overwrite an existing lock")
    source = args.source.resolve()
    command = [args.git, "-c", "safe.directory=" + str(source), "-C", str(source)]
    commit = subprocess.check_output(command + ["rev-parse", "HEAD"], text=True).strip()
    status = subprocess.check_output(command + ["status", "--porcelain", "--untracked-files=all", "--", "tools/campaign_port"], text=True)
    if status:
        raise ValueError("commit reviewed source changes before locking the toolchain")
    sys.path.insert(0, str(source / "tools/campaign_port"))
    import recovery_toolchain
    artifacts = []
    for path in ("evidence/checkpoint-085-recovery-lock.json",
                 "evidence/checkpoint-085-recovery-selectors.json",
                 "evidence/checkpoint-085-raw-structural-plan.json",
                 "evidence/checkpoint-085-asset-free-recovery.json",
                 "evidence/checkpoint-086-provenance-trace.json"):
        data = (PIPELINE / path).read_bytes()
        artifacts.append({"path": path, "bytes": len(data), "sha256": hashlib.sha256(data).hexdigest()})
    result = {"schema": "doom3-recovery-toolchain-lock-v1",
              "source_repository": "https://github.com/Zippingrocks/doom3-gpl-xbox-reconstruction",
              "source_commit": commit, "source_lineage": "master-not-main",
              "metadata_lock": artifacts[0]["path"], "structural_plan": artifacts[2]["path"],
              "provenance_trace": artifacts[4]["path"],
              "pipeline_artifacts": artifacts, "files": recovery_toolchain.identities(source),
              "runtime_contract": {"python_minimum": "3.10", "python_dependencies": "standard-library-only",
                                   "native_engine_required": False, "licensed_assets_required_for_verification": False},
              "limits": ["Does not include engine build toolchains or retail inputs.",
                         "Does not prove full final-overlay composition.",
                         "Python/PowerShell line endings normalized; profiles remain byte-exact."]}
    recovery_toolchain.verify(source, result)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("x", encoding="utf-8", newline="\n") as stream:
        json.dump(result, stream, indent=2)
        stream.write("\n")
    print(json.dumps({"source_commit": commit, "source_files": len(result["files"]),
                      "pipeline_artifacts": len(artifacts)}))


if __name__ == "__main__": main()
