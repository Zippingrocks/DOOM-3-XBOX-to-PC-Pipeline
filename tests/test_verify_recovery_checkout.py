import hashlib
import importlib.util
from pathlib import Path
import tempfile
import unittest

spec = importlib.util.spec_from_file_location("verify_recovery_checkout", Path(__file__).resolve().parents[1] / "tools/verify_recovery_checkout.py")
verify = importlib.util.module_from_spec(spec)
spec.loader.exec_module(verify)


class CheckoutVerifierTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name).resolve()

    def row(self, data=b"example\n", mode="bytes"):
        return {"path": "file.py", "mode": mode, "bytes": len(data), "sha256": hashlib.sha256(data).hexdigest()}

    def test_python_line_ending_normalization(self):
        (self.root / "file.py").write_bytes(b"example\r\n")
        verify.verify_files(self.root, [self.row(mode="lf")])

    def test_profile_bytes_are_not_normalized(self):
        (self.root / "file.py").write_bytes(b"example\r\n")
        with self.assertRaises(ValueError): verify.verify_files(self.root, [self.row()])

    def test_changed_source_fails(self):
        (self.root / "file.py").write_bytes(b"changed\n")
        with self.assertRaises(ValueError): verify.verify_files(self.root, [self.row()])

    def test_empty_duplicate_and_unknown_modes_fail(self):
        (self.root / "file.py").write_bytes(b"example\n")
        for records in ([], [self.row(), self.row()], [self.row(mode="unknown")]):
            with self.assertRaises(ValueError): verify.verify_files(self.root, records)

    def test_unsafe_paths_fail(self):
        for name in ("../x", "/absolute", "C:/absolute", "a\\b", "a/./b", "a//b", "a./b", "a /b"):
            with self.subTest(name=name), self.assertRaises(ValueError): verify.safe_path(self.root, name)

    def test_recipe_reference_must_be_verified_and_root_relative(self):
        for path in ("../outside", "/absolute", "evidence/not-verified.json"):
            with self.subTest(path=path), self.assertRaises(ValueError):
                verify.bound_artifact({"metadata_lock": path, "pipeline_artifacts": []}, "metadata_lock")
        lock = {"metadata_lock": "evidence/example.json", "pipeline_artifacts": [{"path": "evidence/example.json"}]}
        self.assertEqual(verify.bound_artifact(lock, "metadata_lock"), verify.PIPELINE / "evidence/example.json")

    def test_optional_resources_are_explicitly_bound_and_audio_is_paired(self):
        self.assertEqual(verify.resource_artifacts({}), {})
        for lock in ({"audio_texture_plan": "plan.json"}, {"audio_texture_bindings": "bindings.json"},
                     {"shared_resource_plan": "shared.json", "pipeline_artifacts": []}):
            with self.assertRaises(ValueError): verify.resource_artifacts(lock)
        lock = {"audio_texture_plan": "plan.json", "audio_texture_bindings": "bindings.json",
                "shared_resource_plan": "shared.json", "pipeline_artifacts": [
                    {"path": "plan.json"}, {"path": "bindings.json"}, {"path": "shared.json"}]}
        self.assertEqual(set(verify.resource_artifacts(lock)),
                         {"audio_texture_plan", "audio_texture_bindings", "shared_resource_plan"})

    def test_audio_producer_binding_must_match_pinned_source(self):
        (self.root / "file.py").write_bytes(b"example\r\n")
        bindings = {"current_recipe_tools": [self.row(mode="lf")]}
        verify.verify_producer_bindings(self.root, bindings)
        for rows in ([], [self.row(mode="bytes")], [self.row(mode="lf")] * 2):
            with self.assertRaises(ValueError): verify.verify_producer_bindings(self.root, {"current_recipe_tools": rows})
        (self.root / "file.py").write_bytes(b"changed\n")
        with self.assertRaises(ValueError): verify.verify_producer_bindings(self.root, bindings)


if __name__ == "__main__": unittest.main()
