"""Synthetic orchestration only: no original files or converters are opened."""
import copy
import hashlib
import importlib.util
import inspect
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest import mock

TOOLS = Path(__file__).resolve().parents[1] / "tools"
sys.path.insert(0, str(TOOLS))
spec = importlib.util.spec_from_file_location("recover_original_inputs", TOOLS / "recover_original_inputs.py")
recover = importlib.util.module_from_spec(spec)
spec.loader.exec_module(recover)


class OriginalInputRecoveryTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name).resolve()
        self.source = self.root / "source"
        self.source.mkdir()
        self.iso = self.root / "synthetic.iso"
        self.iso.write_bytes(b"synthetic input")
        self.roots = {}
        for name in ("solo", "coop", "shared"):
            self.roots[name] = self.root / name
            self.roots[name].mkdir()
        self.context = {"commands": {stage: [stage] for stage in recover.STAGES},
                        "source_commit": "a" * 40, "toolchain_lock_sha256": "b" * 64,
                        "metadata_lock_sha256": "c" * 64, "bindings_sha256": "d" * 64,
                        "plans": {"raw": {"maps": [{"mode": "solo", "map": "example", "inputs": {
                            "gfc": {"path": "{ARCHIVES}/solo/example.gfc", "bytes": 1, "sha256": "e" * 64}},
                            "steps": [{"id": "map-crc"}, {"id": "cm"}]}]},
                            "shared": {"extractions": [{"id": "example", "inputs": {
                                "gfc": {"path": "{ARCHIVES}/shared/assets.gfc", "bytes": 1, "sha256": "e" * 64}},
                                "expected_members": [{"member": "./base/example", "path": "base/example",
                                                      "bytes": 1, "sha256": "e" * 64}]}]},
                            "audio": {"original_disc": {"bytes": 10, "sha256": "e" * 64},
                                "summary": {"target_entries": 1, "bound_entries": 1, "unresolved_entries": 0},
                                "steps": [{"id": "example", "argv": ["tool", "--output", "{NEW}/audio/example"],
                                    "authenticated_inputs": [{"path": "{ORIGINALS}/work/shared-archives/assets.gfc",
                                                               "bytes": 1, "sha256": "e" * 64}],
                                    "authenticated_disc_extents": [{"offset": 0, "bytes": 10, "sha256": "e" * 64}],
                                    "expected_outputs": [{"path": "sound/example.wav", "bytes": 1, "sha256": "e" * 64}]}]}}}
        self.calls = []

    def receipt(self, stage, raw_failure=False):
        identity = {"source_commit": self.context["source_commit"],
                    "lock_sha256": self.context["toolchain_lock_sha256"]}
        authenticated = recover.planned_inputs(stage, self.context["plans"][stage])
        if stage == "raw":
            companion = {"map_crc": 1, "header_crc": 2 if raw_failure else 1, "matches": not raw_failure}
            issues = [{"mode": "solo", "map": "example", "step": "cm", "map_crc": 1,
                       "header_crc": 2}] if raw_failure else []
            return {"schema": "doom3-raw-structural-run-v1", "toolchain": identity, "authenticated_inputs": authenticated,
                    "metadata_lock_sha256": self.context["metadata_lock_sha256"],
                    "status": "completed-with-companion-identity-failures" if raw_failure else "structural-witnesses-verified",
                    "steps": [{"mode": "solo", "map": "example", "step": "map-crc", "geometry_crc": 1, "historical_witness_verified": True},
                              {"mode": "solo", "map": "example", "step": "cm", "historical_witness_verified": True,
                               "companion_identity": companion}],
                    "unwitnessed_steps": [], "companion_identity_issues": issues}
        if stage == "shared":
            return {"schema": "doom3-shared-resource-run-v1", "toolchain": identity, "authenticated_inputs": authenticated,
                    "metadata_lock_sha256": self.context["metadata_lock_sha256"],
                    "extraction_roots": 1, "verified_member_occurrences": 1,
                    "status": "original-member-witnesses-verified", "results": [
                        {"id": "example", "verified_files": 1, "members": copy.deepcopy(self.context["plans"]["shared"]["extractions"][0]["expected_members"])}]}
        return {"schema": "doom3-audio-texture-run-v1", "authenticated_inputs": authenticated, "provenance": {
                    "source_commit": self.context["source_commit"], "toolchain_lock_sha256": self.context["toolchain_lock_sha256"],
                    "bindings_sha256": self.context["bindings_sha256"]},
                "summary": {"steps": 1, "files": 1, "target_entries": 1, "bound_target_entries": 1, "unresolved_target_entries": 0},
                "status": "historical-output-witnesses-verified", "steps": [
                    {"id": "example", "status": "historical-output-witnesses-verified",
                     "files": [{"path": "audio/example/sound/example.wav", "bytes": 1, "sha256": "e" * 64}]}]}

    def write_receipt(self, stage, receipt):
        output = self.root / ("recovery-" + stage)
        output.mkdir(exist_ok=True)
        (output / recover.RECEIPTS[stage]).write_text(json.dumps(receipt), encoding="utf-8")
        return output

    def fake_run(self, command, cwd):
        self.calls.append(command)
        if "--execute" in command:
            self.write_receipt(command[0], self.receipt(command[0]))
        return 0

    def perform(self, execute=False, run=None):
        with mock.patch.object(recover.checkout, "verify") as check, mock.patch.object(recover, "prepare", return_value=self.context), \
                mock.patch.object(recover, "run", side_effect=run or self.fake_run):
            result = recover.recover(self.source, "lock.json", self.iso, self.roots, self.root, execute=execute)
            check.assert_called_once_with(self.source, git="git", lock_name="lock.json")
            return result

    def test_default_preflights_all_stages_and_creates_nothing(self):
        before = set(self.root.iterdir())
        result, code = self.perform()
        self.assertEqual(code, 0)
        self.assertEqual(result["status"], "preflight-only-no-output-created")
        self.assertEqual(self.calls, [["raw"], ["shared"], ["audio"]])
        self.assertEqual(set(self.root.iterdir()), before)

    def test_all_preflights_run_before_any_conversion(self):
        result, code = self.perform(execute=True)
        self.assertEqual(code, 0)
        self.assertEqual(result["status"], "offline-input-recovery-completed")
        self.assertEqual(self.calls, [["raw"], ["shared"], ["audio"],
                                     ["raw", "--execute"], ["shared", "--execute"], ["audio", "--execute"]])
        saved = (self.root / "recovery-session.json").read_text()
        self.assertNotIn(str(self.root), saved)
        self.assertNotIn("commands", saved)
        self.assertNotIn("active_stage", saved)

    def test_failed_last_preflight_creates_no_output_or_session(self):
        def run(command, cwd):
            self.calls.append(command)
            return 2 if command == ["audio"] else 0
        before = set(self.root.iterdir())
        with self.assertRaisesRegex(ValueError, "preflight failed: audio"):
            self.perform(execute=True, run=run)
        self.assertEqual(self.calls, [["raw"], ["shared"], ["audio"]])
        self.assertEqual(set(self.root.iterdir()), before)

    def test_unexpected_preflight_output_is_rejected(self):
        def run(command, cwd):
            if command == ["audio"]:
                (self.root / "recovery-audio").mkdir()
            return 0
        with self.assertRaisesRegex(ValueError, "existing recovery output"):
            self.perform(execute=True, run=run)
        self.assertFalse((self.root / "recovery-session.json").exists())

    def test_validated_raw_exit_one_continues_but_overall_is_nonzero(self):
        def run(command, cwd):
            if command == ["raw", "--execute"]:
                self.calls.append(command)
                self.write_receipt("raw", self.receipt("raw", raw_failure=True))
                return 1
            return self.fake_run(command, cwd)
        result, code = self.perform(execute=True, run=run)
        self.assertEqual(code, 1)
        self.assertEqual(result["status"], "completed-with-known-issues")
        self.assertEqual(result["stages"][0]["companion_identity_failures"], 1)
        self.assertEqual(len(result["stages"]), 3)

    def test_exit_one_without_matching_complete_receipt_stops(self):
        def run(command, cwd):
            value = self.fake_run(command, cwd)
            return 1 if command == ["raw", "--execute"] else value
        with self.assertRaisesRegex(ValueError, "raw exit/status"):
            self.perform(execute=True, run=run)
        receipt = json.loads((self.root / "recovery-session.json").read_bytes())
        self.assertEqual(receipt["status"], "incomplete")
        self.assertEqual(receipt["active_stage"], "raw")
        self.assertEqual(receipt["failure_type"], "ValueError")
        self.assertNotIn(["shared", "--execute"], self.calls)

    def test_other_nonzero_exit_stops_and_persists_incomplete_session(self):
        def run(command, cwd):
            self.calls.append(command)
            return 2 if command == ["raw", "--execute"] else 0
        with self.assertRaisesRegex(ValueError, "recovery stage failed: raw"):
            self.perform(execute=True, run=run)
        receipt = json.loads((self.root / "recovery-session.json").read_bytes())
        self.assertEqual(receipt["status"], "incomplete")
        self.assertEqual(receipt["stages"], [])
        self.assertNotIn(["shared", "--execute"], self.calls)

    def test_raw_receipt_rejects_missing_duplicate_and_inconsistent_steps(self):
        base = self.receipt("raw", raw_failure=True)
        cases = []
        missing = copy.deepcopy(base); missing["steps"].pop(); cases.append(missing)
        duplicate = copy.deepcopy(base); duplicate["steps"].append(duplicate["steps"][0]); cases.append(duplicate)
        false_issues = copy.deepcopy(base); false_issues["companion_identity_issues"] = []; cases.append(false_issues)
        stale = copy.deepcopy(base); stale["toolchain"]["source_commit"] = "e" * 40; cases.append(stale)
        for row in cases:
            with self.subTest(receipt=row):
                output = self.write_receipt("raw", row)
                with self.assertRaises(ValueError):
                    recover.completed_receipt("raw", output, self.context, 1)

    def test_shared_audio_and_incomplete_receipts_fail_closed(self):
        for stage in ("shared", "audio"):
            for mutation in ("incomplete", "wrong-source", "missing-step"):
                row = self.receipt(stage)
                if mutation == "incomplete": row["failure_type"] = "ValueError"
                elif mutation == "wrong-source":
                    row["provenance" if stage == "audio" else "toolchain"]["source_commit"] = "e" * 40
                else: row["steps" if stage == "audio" else "results"] = []
                output = self.write_receipt(stage, row)
                with self.subTest(stage=stage, mutation=mutation), self.assertRaises(ValueError):
                    recover.completed_receipt(stage, output, self.context, 0)

    def test_companion_crc_must_match_own_map_and_witness_flags_are_boolean(self):
        for mutation in ("wrong-map-crc", "integer-flag"):
            row = self.receipt("raw")
            if mutation == "wrong-map-crc": row["steps"][0]["geometry_crc"] = 3
            else: row["steps"][0]["historical_witness_verified"] = 1
            with self.subTest(mutation=mutation), self.assertRaises(ValueError):
                recover.completed_receipt("raw", self.write_receipt("raw", row), self.context, 0)

    def test_authenticated_inputs_must_exactly_match_all_planned_identities(self):
        for stage in recover.STAGES:
            for mutation in ("missing", "size-bool", "extra"):
                row = self.receipt(stage)
                inputs = row["authenticated_inputs"]["archives"] if stage == "audio" else row["authenticated_inputs"]
                if mutation == "missing": inputs.clear()
                elif mutation == "extra": inputs.append(copy.deepcopy(inputs[0]))
                else: inputs[0]["bytes"] = True
                with self.subTest(stage=stage, mutation=mutation), self.assertRaises(ValueError):
                    recover.completed_receipt(stage, self.write_receipt(stage, row), self.context, 0)
        row = self.receipt("audio")
        row["authenticated_inputs"]["verified_disc_extents"][0]["sha256"] = "f" * 64
        with self.assertRaises(ValueError):
            recover.completed_receipt("audio", self.write_receipt("audio", row), self.context, 0)

    def test_audio_requires_exact_output_paths_hashes_sizes_and_summary(self):
        for field, value in (("path", "sound/example.wav"), ("sha256", "f" * 64), ("bytes", True)):
            row = self.receipt("audio")
            row["steps"][0]["files"][0][field] = value
            with self.subTest(field=field), self.assertRaises(ValueError):
                recover.completed_receipt("audio", self.write_receipt("audio", row), self.context, 0)
        row = self.receipt("audio"); row["summary"]["files"] = True
        with self.assertRaises(ValueError):
            recover.completed_receipt("audio", self.write_receipt("audio", row), self.context, 0)

    def test_shared_member_sizes_and_count_summaries_reject_boolean_integers(self):
        for mutation in ("member-bytes", "verified-files", "roots", "occurrences"):
            row = self.receipt("shared")
            if mutation == "member-bytes": row["results"][0]["members"][0]["bytes"] = True
            elif mutation == "verified-files": row["results"][0]["verified_files"] = True
            elif mutation == "roots": row["extraction_roots"] = True
            else: row["verified_member_occurrences"] = True
            with self.subTest(mutation=mutation), self.assertRaises(ValueError):
                recover.completed_receipt("shared", self.write_receipt("shared", row), self.context, 0)

    def test_quickstart_markdown_links_resolve_to_real_headings(self):
        import re
        doc = TOOLS.parent / "docs/NEXT_MACHINE_QUICKSTART.md"
        for target in re.findall(r"\]\(([^)]+)\)", doc.read_text()):
            if "://" in target: continue
            name, separator, anchor = target.partition("#")
            path = doc.parent / name
            self.assertTrue(path.is_file(), target)
            if separator:
                headings = re.findall(r"^#+ (.+)$", path.read_text(), re.MULTILINE)
                slugs = {re.sub(r"[^\w -]", "", heading.lower()).replace(" ", "-") for heading in headings}
                self.assertIn(anchor, slugs, target)

    def test_safe_prefix_roots_and_existing_outputs(self):
        for prefix in ("../bad", "a/b", "a\\b", "", " name", "a:b", "a" * 49, "é"):
            with self.subTest(prefix=prefix), self.assertRaises(ValueError):
                recover.destinations(self.root, prefix)
        bindings = [name + "=" + str(path) for name, path in self.roots.items()]
        self.assertEqual(recover.archive_roots(bindings), self.roots)
        for values in (bindings[:-1], bindings + [bindings[0]], ["unknown=" + str(self.root)]):
            with self.assertRaises(ValueError): recover.archive_roots(values)
        (self.root / "recovery-session.json").write_text("preserve")
        with self.assertRaises(ValueError): self.perform(execute=True)
        self.assertEqual((self.root / "recovery-session.json").read_text(), "preserve")

    def test_prepare_uses_only_fixed_typed_runner_flags(self):
        pipeline = self.root / "pipeline"
        pipeline.mkdir()
        files = {"metadata.json": {}, "raw.json": self.context["plans"]["raw"],
                 "shared.json": self.context["plans"]["shared"], "audio.json": self.context["plans"]["audio"],
                 "bindings.json": {"unused_arbitrary_argv": ["do-not-execute"]}}
        for name, value in files.items(): (pipeline / name).write_text(json.dumps(value))
        lock = {"source_commit": "a" * 40, "metadata_lock": "metadata.json", "structural_plan": "raw.json",
                "shared_resource_plan": "shared.json", "audio_texture_plan": "audio.json",
                "audio_texture_bindings": "bindings.json", "pipeline_artifacts": [{"path": name} for name in files]}
        (pipeline / "lock.json").write_text(json.dumps(lock))
        tools = self.source / "tools/campaign_port"
        tools.mkdir(parents=True)
        for name in recover.RUNNERS.values(): (tools / name).write_text("# synthetic\n")
        outputs, _ = recover.destinations(self.root, "recovery")
        with mock.patch.object(recover.checkout, "PIPELINE", pipeline):
            context = recover.prepare(self.source, "lock.json", self.iso, self.roots, outputs)
        for stage, command in context["commands"].items():
            self.assertEqual(command[6], str(tools / recover.RUNNERS[stage]))
            self.assertNotIn("do-not-execute", command)
            self.assertNotIn("--execute", command)
            self.assertEqual(command.count("--archive-root"), 3)
            self.assertEqual(command[command.index("--output") + 1], str(outputs[stage]))
        audio = context["commands"]["audio"]
        self.assertEqual(audio[audio.index("--iso") + 1], str(self.iso))
        self.assertEqual(audio[audio.index("--bindings-sha256") + 1],
                         hashlib.sha256((pipeline / "bindings.json").read_bytes()).hexdigest())

    def test_cli_and_workflow_share_verifier_default_lock(self):
        self.assertEqual(inspect.signature(recover.checkout.verify).parameters["lock_name"].default, recover.checkout.LOCK)
        workflow = (TOOLS.parent / ".github/workflows/asset-free-recovery.yml").read_text()
        self.assertIn("from verify_recovery_checkout import LOCK", workflow)
        self.assertIn("Path(LOCK).read_text()", workflow)
        self.assertIn("tools/verify_recovery_checkout.py --source reconstruction --tests", workflow)
        with mock.patch.object(sys, "argv", ["recover", "--source", str(self.source), "--iso", str(self.iso),
             "--archive-root", "solo=" + str(self.roots["solo"]), "--archive-root", "coop=" + str(self.roots["coop"]),
             "--archive-root", "shared=" + str(self.roots["shared"]), "--output-parent", str(self.root)]), \
             mock.patch.object(recover, "recover", return_value=({"status": "synthetic"}, 0)) as run, \
             mock.patch("builtins.print"):
            self.assertEqual(recover.main(), 0)
        self.assertEqual(run.call_args.args[1], recover.checkout.LOCK)
        self.assertFalse(run.call_args.args[6])


if __name__ == "__main__": unittest.main()
