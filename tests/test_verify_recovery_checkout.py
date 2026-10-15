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


if __name__ == "__main__": unittest.main()
