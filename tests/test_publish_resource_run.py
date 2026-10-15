import copy
import hashlib
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch


spec = importlib.util.spec_from_file_location("publish_resource_run", Path(__file__).resolve().parents[1] / "tools/publish_resource_run.py")
publisher = importlib.util.module_from_spec(spec)
spec.loader.exec_module(publisher)


def data(value):
    return (json.dumps(value, indent=2) + "\n").encode()


def sha(value):
    return hashlib.sha256(value).hexdigest()


def file_row(path, number=1):
    return {"path": path, "bytes": number, "sha256": str(number % 10) * 64}


def fixtures(kind="shared"):
    tools = [{**file_row("tools/campaign_port/" + name), "mode": "lf"} for name in sorted(publisher.TOOLS)]
    lock = {"schema": "doom3-recovery-toolchain-lock-v1", "source_commit": "a" * 40,
            "files": tools, "metadata_lock": "evidence/inventory.json", "pipeline_artifacts": [file_row("evidence/inventory.json", 2)]}
    if kind == "shared":
        members = [{**file_row("base/def/example.def", 3), "member": "./base/def/example.def"}]
        original = file_row("{ARCHIVES}/shared/assets.gfc", 4)
        plan = {"schema": publisher.SHARED_PLAN, "extractions": [
            {"id": "shared-example", "inputs": {"gfc": original}, "expected_members": members}],
            "summary": {"extraction_roots": 1, "selected_member_occurrences": 1, "original_archive_files": 1}}
        lock["shared_resource_plan"] = "evidence/shared.json"
        receipt = {"schema": "doom3-shared-resource-run-v1", "status": publisher.SHARED_STATUS,
                   "metadata_lock_sha256": "2" * 64, "authenticated_inputs": [copy.deepcopy(original)],
                   "results": [{"id": "shared-example", "verified_files": 1, "members": copy.deepcopy(members)}],
                   "extraction_roots": 1, "verified_member_occurrences": 1}
    else:
        output = file_row("sound/example.wav", 3)
        plan = {"schema": publisher.AUDIO_PLAN,
                "original_disc": {"path": "{ISO}", "bytes": 1000, "sha256": "5" * 64},
                "producer_tools": [{k: row[k] for k in ("path", "mode", "sha256")} for row in tools],
                "bindings_sha256": "6" * 64,
                "steps": [{"id": "input-0001", "requires": [],
                           "argv": ["{PYTHON}", "{SOURCE}/tools/campaign_port/doom3_campaign_port.py", "extract",
                                    "--out", "{NEW}/inputs/input-0001"],
                           "authenticated_inputs": [file_row("{ORIGINALS}/work/shared-archives/assets.gfc", 4)],
                           "expected_outputs": [file_row("base/sound/example.xsndshd", 2)]},
                          {"id": "audio-0001", "requires": ["input-0001"],
                           "argv": ["{PYTHON}", "{SOURCE}/tools/campaign_port/xact_audio.py", "--output", "{NEW}/recovered/audio-0001"],
                           "authenticated_disc_extents": [{"offset": 10, "bytes": 200, "sha256": "7" * 64}],
                           "selected_input_spans": [{"input_extent": {"offset": 20, "bytes": 30, "sha256": "8" * 64}}],
                           "expected_outputs": [output]}],
                "targets": [{"mode": "coop", "map": "example", "path": output["path"],
                             "sha256": output["sha256"], "recipe_id": "audio-0001"}],
                "summary": {"steps": 2, "producer_steps": 1, "target_entries": 1, "bound_entries": 1, "unresolved_entries": 0}}
        lock.update(audio_texture_plan="evidence/audio.json", audio_texture_bindings="evidence/bindings.json")
        lock["pipeline_artifacts"].append(file_row("evidence/bindings.json", 6))
        receipt = {"schema": "doom3-audio-texture-run-v1", "status": publisher.AUDIO_STATUS,
                   "authenticated_inputs": {"iso": {"bytes": 1000, "sha256": "5" * 64},
                                            "archives": [file_row("shared/assets.gfc", 4)],
                                            "verified_disc_extents": [{"offset": 10, "bytes": 200, "sha256": "7" * 64},
                                                                      {"offset": 20, "bytes": 30, "sha256": "8" * 64}]},
                   "steps": [{"id": "input-0001", "status": publisher.AUDIO_STATUS,
                              "files": [file_row("inputs/input-0001/base/sound/example.xsndshd", 2)]},
                             {"id": "audio-0001", "status": publisher.AUDIO_STATUS,
                              "files": [file_row("recovered/audio-0001/sound/example.wav", 3)]}],
                   "summary": {"steps": 2, "files": 2, "target_entries": 1, "bound_target_entries": 1, "unresolved_target_entries": 0}}
    bind(receipt, lock, plan)
    return receipt, lock, plan


def bind(receipt, lock, plan):
    kind = "shared_resource_plan" if plan["schema"] == publisher.SHARED_PLAN else "audio_texture_plan"
    plan_data = data(plan)
    lock["pipeline_artifacts"] = [row for row in lock["pipeline_artifacts"] if row["path"] != lock[kind]]
    lock["pipeline_artifacts"].append({"path": lock[kind], "bytes": len(plan_data), "sha256": sha(plan_data)})
    if kind == "shared_resource_plan":
        receipt["toolchain"] = {"source_commit": lock["source_commit"], "files_verified": len(lock["files"]),
                                "lock_sha256": sha(data(lock))}
    else:
        receipt["provenance"] = {"source_commit": lock["source_commit"], "toolchain_files_verified": len(lock["files"]),
                                "toolchain_lock_sha256": sha(data(lock)), "bindings_sha256": plan["bindings_sha256"]}


def publish(receipt, lock, plan):
    return publisher.publish(data(receipt), data(lock), data(plan))


class ResourcePublicationTests(unittest.TestCase):
    def test_shared_complete_typed_projection(self):
        receipt, lock, plan = fixtures()
        with patch.object(Path, "read_bytes", side_effect=AssertionError("no asset IO")):
            proof = publish(receipt, lock, plan)
        self.assertEqual(proof["summary"]["verified_member_occurrences"], 1)
        self.assertEqual(proof["authenticated_inputs"]["archives"][0]["path"], "shared/assets.gfc")
        self.assertFalse(proof["publication_checks"]["independent_payload_verification"])
        self.assertEqual(proof["receipt_sha256"], sha(data(receipt)))

    def test_audio_paths_extents_and_counts(self):
        receipt, lock, plan = fixtures("audio")
        proof = publish(receipt, lock, plan)
        self.assertEqual(proof["summary"]["files"], 2)
        self.assertEqual(proof["summary"]["verified_disc_extents"], 2)
        self.assertEqual(proof["steps"][1]["files"][0]["path"], "recovered/audio-0001/sound/example.wav")
        self.assertEqual(proof["bindings_sha256"], "6" * 64)

    def test_same_payload_in_separate_shared_roots_is_not_collapsed(self):
        receipt, lock, plan = fixtures()
        extra = copy.deepcopy(plan["extractions"][0])
        extra["id"] = "shared-other"
        plan["extractions"].append(extra)
        recorded = copy.deepcopy(receipt["results"][0])
        recorded["id"] = extra["id"]
        receipt["results"].append(recorded)
        receipt.update(extraction_roots=2, verified_member_occurrences=2)
        plan["summary"].update(extraction_roots=2, selected_member_occurrences=2)
        bind(receipt, lock, plan)
        proof = publish(receipt, lock, plan)
        self.assertEqual(proof["summary"]["verified_member_occurrences"], 2)
        self.assertEqual(proof["summary"]["original_archive_files"], 1)

    def test_audio_destination_comes_from_locked_argv_not_id_guess(self):
        receipt, lock, plan = fixtures("audio")
        plan["steps"][1]["argv"][-1] = "{NEW}/separate/accepted-output"
        receipt["steps"][1]["files"][0]["path"] = "separate/accepted-output/sound/example.wav"
        bind(receipt, lock, plan)
        proof = publish(receipt, lock, plan)
        self.assertEqual(proof["steps"][1]["files"][0]["path"], "separate/accepted-output/sound/example.wav")

    def test_audio_repeated_extent_is_deduplicated_and_targets_are_per_map(self):
        receipt, lock, plan = fixtures("audio")
        plan["steps"][1]["authenticated_disc_extents"] *= 2
        target = copy.deepcopy(plan["targets"][0])
        target["map"] = "another_map"
        plan["targets"].append(target)
        plan["summary"].update(target_entries=2, bound_entries=2)
        receipt["summary"].update(target_entries=2, bound_target_entries=2)
        bind(receipt, lock, plan)
        proof = publish(receipt, lock, plan)
        self.assertEqual(proof["summary"]["verified_disc_extents"], 2)
        self.assertEqual(proof["summary"]["bound_target_entries"], 2)

    def test_private_untyped_fields_are_dropped_at_every_level(self):
        for kind in ("shared", "audio"):
            receipt, lock, plan = fixtures(kind)
            private = "C:\\secret\\game-payload-content command --password"
            receipt.update(commands=[private], runtime={"python": private}, logs=private, limits=[private])
            chain = receipt["toolchain"] if kind == "shared" else receipt["provenance"]
            chain["private"] = private
            step = receipt["results"][0] if kind == "shared" else receipt["steps"][0]
            step["commands"] = [private]
            file = step["members"][0] if kind == "shared" else step["files"][0]
            file["payload"] = private
            self.assertNotIn(private, json.dumps(publish(receipt, lock, plan)))

    def test_incomplete_and_stale_failure_state_rejected(self):
        for kind in ("shared", "audio"):
            for key, value in (("status", "incomplete"), ("failure_type", "ValueError"), ("active_step", "input-0001")):
                receipt, lock, plan = fixtures(kind)
                receipt[key] = value
                with self.subTest(kind=kind, key=key), self.assertRaises(ValueError): publish(receipt, lock, plan)

    def test_wrong_toolchain_binding_and_boolean_counts(self):
        for kind in ("shared", "audio"):
            for field, value in (("source_commit", "b" * 40),
                                 ("lock_sha256" if kind == "shared" else "toolchain_lock_sha256", "b" * 64),
                                 ("files_verified" if kind == "shared" else "toolchain_files_verified", True)):
                receipt, lock, plan = fixtures(kind)
                receipt["toolchain" if kind == "shared" else "provenance"][field] = value
                with self.subTest(kind=kind, field=field), self.assertRaises(ValueError): publish(receipt, lock, plan)

    def test_plan_and_metadata_and_binding_hash_mismatches(self):
        for kind in ("shared", "audio"):
            receipt, lock, plan = fixtures(kind)
            plan["changed"] = True
            with self.assertRaises(ValueError): publish(receipt, lock, plan)
            receipt, lock, plan = fixtures(kind)
            if kind == "shared": receipt["metadata_lock_sha256"] = "b" * 64
            else: receipt["provenance"]["bindings_sha256"] = "b" * 64
            with self.assertRaises(ValueError): publish(receipt, lock, plan)

    def test_missing_extra_duplicate_and_reordered_steps(self):
        for kind in ("shared", "audio"):
            for mutation in ("missing", "extra", "wrong"):
                receipt, lock, plan = fixtures(kind)
                steps = receipt["results" if kind == "shared" else "steps"]
                if mutation == "missing": steps.pop()
                elif mutation == "extra": steps.append(copy.deepcopy(steps[0]))
                else: steps[0]["id"] = "unknown"
                with self.subTest(kind=kind, mutation=mutation), self.assertRaises(ValueError): publish(receipt, lock, plan)
        receipt, lock, plan = fixtures("audio")
        receipt["steps"].reverse()
        with self.assertRaises(ValueError): publish(receipt, lock, plan)

    def test_exact_output_set_and_typed_identity(self):
        for kind in ("shared", "audio"):
            for field, value in (("path", "../private"), ("path", "C:/private"), ("sha256", "b" * 64), ("bytes", True), ("bytes", 999)):
                receipt, lock, plan = fixtures(kind)
                selected = receipt["results"][0]["members"] if kind == "shared" else receipt["steps"][0]["files"]
                selected[0][field] = value
                with self.subTest(kind=kind, field=field, value=value), self.assertRaises(ValueError): publish(receipt, lock, plan)
            for mutation in ("duplicate", "missing"):
                receipt, lock, plan = fixtures(kind)
                selected = receipt["results"][0]["members"] if kind == "shared" else receipt["steps"][0]["files"]
                if mutation == "duplicate": selected.append(copy.deepcopy(selected[0]))
                else: selected.clear()
                with self.assertRaises(ValueError): publish(receipt, lock, plan)

    def test_exact_authenticated_input_sets(self):
        for kind in ("shared", "audio"):
            for mutation in ("duplicate", "missing", "hash", "path", "boolean"):
                receipt, lock, plan = fixtures(kind)
                selected = receipt["authenticated_inputs"] if kind == "shared" else receipt["authenticated_inputs"]["archives"]
                if mutation == "duplicate": selected.append(copy.deepcopy(selected[0]))
                elif mutation == "missing": selected.clear()
                elif mutation == "hash": selected[0]["sha256"] = "b" * 64
                elif mutation == "path": selected[0]["path"] = "shared/not-selected.gfc"
                else: selected[0]["bytes"] = True
                with self.subTest(kind=kind, mutation=mutation), self.assertRaises(ValueError): publish(receipt, lock, plan)

    def test_audio_exact_extent_set_and_iso(self):
        for mutation in ("missing", "duplicate", "hash", "offset", "iso"):
            receipt, lock, plan = fixtures("audio")
            selected = receipt["authenticated_inputs"]["verified_disc_extents"]
            if mutation == "missing": selected.pop()
            elif mutation == "duplicate": selected.append(copy.deepcopy(selected[0]))
            elif mutation == "hash": selected[0]["sha256"] = "b" * 64
            elif mutation == "offset": selected[0]["offset"] += 1
            else: receipt["authenticated_inputs"]["iso"]["sha256"] = "b" * 64
            with self.subTest(mutation=mutation), self.assertRaises(ValueError): publish(receipt, lock, plan)

    def test_wrong_and_boolean_summary_counts(self):
        for kind in ("shared", "audio"):
            receipt, lock, plan = fixtures(kind)
            for value in (True, 99):
                mutated = copy.deepcopy(receipt)
                if kind == "shared": mutated["verified_member_occurrences"] = value
                else: mutated["summary"]["files"] = value
                with self.assertRaises(ValueError): publish(mutated, lock, plan)

    def test_audio_dependencies_producers_and_targets_rejected_even_when_relocked(self):
        for mutation in ("dependency", "producer", "target", "summary", "output-root", "extent-conflict"):
            receipt, lock, plan = fixtures("audio")
            if mutation == "dependency": plan["steps"][0]["requires"] = ["audio-0001"]
            elif mutation == "producer": plan["producer_tools"][0]["sha256"] = "b" * 64
            elif mutation == "target": plan["targets"][0]["sha256"] = "b" * 64
            elif mutation == "summary": plan["summary"]["steps"] = True
            elif mutation == "output-root": plan["steps"][0]["argv"][-1] = "{NEW}/../private"
            else: plan["steps"][1]["authenticated_disc_extents"].append({"offset": 10, "bytes": 200, "sha256": "b" * 64})
            bind(receipt, lock, plan)
            with self.subTest(mutation=mutation), self.assertRaises(ValueError): publish(receipt, lock, plan)

    def test_success_does_not_promote_unresolved_targets(self):
        receipt, lock, plan = fixtures("audio")
        plan["targets"][0]["recipe_id"] = None
        plan["summary"].update(bound_entries=0, unresolved_entries=1)
        receipt["summary"].update(bound_target_entries=0, unresolved_target_entries=1)
        bind(receipt, lock, plan)
        proof = publish(receipt, lock, plan)
        self.assertEqual(proof["summary"]["unresolved_target_entries"], 1)
        self.assertFalse(proof["publication_checks"]["final_overlay_equivalence"])

    def test_duplicate_json_keys_and_nonfinite_numbers_rejected(self):
        receipt, lock, plan = fixtures()
        for invalid in (b'{"status":1,"status":2}', b'{"extra":NaN}', b'[]'):
            with self.assertRaises(ValueError): publisher.publish(invalid, data(lock), data(plan))

    def test_cli_exclusive_output_and_only_explicit_metadata_reads(self):
        receipt, lock, plan = fixtures()
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            paths = [root / name for name in ("receipt.json", "lock.json", "plan.json")]
            for path, value in zip(paths, (receipt, lock, plan)): path.write_bytes(data(value))
            output = root / "proof.json"
            argv = ["--receipt", str(paths[0]), "--toolchain-lock", str(paths[1]), "--plan", str(paths[2]), "--output", str(output)]
            read_bytes = Path.read_bytes
            opened = []
            def checked_read(path):
                opened.append(path)
                self.assertIn(path, paths)
                return read_bytes(path)
            with patch.object(Path, "read_bytes", checked_read):
                self.assertEqual(publisher.main(argv), 0)
            self.assertEqual(opened, paths)
            original = output.read_bytes()
            self.assertEqual(publisher.main(argv), 2)
            self.assertEqual(output.read_bytes(), original)


if __name__ == "__main__":
    unittest.main()
