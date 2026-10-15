"""Only synthetic ISO bytes/receipts; no game data or real extractor execution."""
import copy
import hashlib
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest import mock

TOOLS = Path(__file__).resolve().parents[1] / "tools"
sys.path.insert(0, str(TOOLS))
spec = importlib.util.spec_from_file_location("prepare_original_archives", TOOLS / "prepare_original_archives.py")
prepare = importlib.util.module_from_spec(spec)
spec.loader.exec_module(prepare)


class OriginalArchivePreparationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name).resolve()
        self.source = self.root / "source"; self.source.mkdir()
        self.iso = self.root / "synthetic.iso"
        self.payload = b"x"
        self.payload_sha = hashlib.sha256(self.payload).hexdigest()
        self.plan = {"schema": "doom3-raw-structural-recipe-plan-v1", "maps": []}
        def item(group, name):
            return {"path": "{ARCHIVES}/" + group + "/" + name, "disc_member": name,
                    "bytes": 1, "sha256": self.payload_sha}
        for mode, count in (("solo", 41), ("coop", 20)):
            for number in range(count):
                name = ("solo" if mode == "solo" else "xc") + str(number)
                self.plan["maps"].append({"mode": mode, "map": name,
                    "inputs": {ext: item(mode, name + "." + ext) for ext in ("gfc", "gob")}})
        self.plan["maps"][0]["inputs"].update({"shared_" + ext: item("shared", "assets." + ext) for ext in ("gfc", "gob")})
        groups = prepare.derive_groups(self.plan)
        entries = []
        iso = bytearray(125 * prepare.SECTOR)
        for index, row in enumerate([row for group in prepare.GROUPS for row in groups[group]], 1):
            entries.append({"path": row["member"], "sector": index, "size": 1, "attributes": 32,
                            "directory": False, "descriptor_offset": index * 16})
            iso[index * prepare.SECTOR] = ord("x")
        self.iso.write_bytes(iso)
        identity = {"bytes": len(iso), "sha256": hashlib.sha256(iso).hexdigest()}
        self.inventory = {"kind": "xdvdfs-inventory", "image": identity, "entries": entries,
                          "volume": {"sector_size": prepare.SECTOR}}
        self.context = {"source_commit": "a" * 40, "toolchain_lock_sha256": "b" * 64,
                        "structural_plan_sha256": "c" * 64, "iso": identity,
                        "inventory": self.inventory, "groups": groups}
        self.extents = prepare.selected_extents(self.inventory, groups, len(iso))
        self.calls = []

    def fake_extract(self, source, iso, destination, members, log):
        self.calls.append(destination.name)
        destination.mkdir()
        log.write_text("private synthetic extractor log")
        for row in members: (destination / row["member"]).write_bytes(self.payload)
        manifest = {"schema": 1, "kind": "xdvdfs-extraction", "image": self.context["iso"],
                    "files": [{**self.extents[row["member"]], "sha256": row["sha256"]} for row in members]}
        (destination / prepare.MANIFEST).write_text(json.dumps(manifest))

    def perform(self, execute=False, extract=None):
        with mock.patch.object(prepare.checkout, "verify") as verified, \
             mock.patch.object(prepare, "context_from_lock", return_value=self.context), \
             mock.patch.object(prepare, "load_inventory_reader", return_value=lambda iso: self.inventory), \
             mock.patch.object(prepare, "extract_group", side_effect=extract or self.fake_extract):
            result = prepare.prepare(self.source, "lock.json", self.iso, self.root, execute=execute)
            verified.assert_called_once_with(self.source, git="git", lock_name="lock.json")
            return result

    def test_derives_exact_124_targets_in_three_groups(self):
        groups = prepare.derive_groups(self.plan)
        self.assertEqual({name: len(rows) for name, rows in groups.items()}, prepare.COUNTS)
        self.assertEqual([row["member"] for row in groups["shared"]], ["assets.gfc", "assets.gob"])

    def test_missing_extra_duplicate_or_renamed_targets_fail(self):
        cases = []
        missing = copy.deepcopy(self.plan); missing["maps"].pop(); cases.append(missing)
        extra = copy.deepcopy(self.plan); extra["maps"].append(extra["maps"][0]); cases.append(extra)
        role = copy.deepcopy(self.plan); role["maps"][0]["inputs"]["unexpected"] = {}; cases.append(role)
        missing_role = copy.deepcopy(self.plan); del missing_role["maps"][0]["inputs"]["gob"]; cases.append(missing_role)
        renamed = copy.deepcopy(self.plan); renamed["maps"][0]["inputs"]["gfc"]["disc_member"] = "other.gfc"; cases.append(renamed)
        escape = copy.deepcopy(self.plan); escape["maps"][0]["inputs"]["gfc"]["path"] = "../x"; cases.append(escape)
        for plan in cases:
            with self.subTest(plan=plan), self.assertRaises(ValueError): prepare.derive_groups(plan)

    def test_conflicting_shared_targets_and_boolean_size_fail(self):
        conflict = copy.deepcopy(self.plan)
        conflict["maps"][1]["inputs"].update(copy.deepcopy(conflict["maps"][0]["inputs"]))
        # Keep this map's own pair canonical; conflict only in the shared witness.
        conflict["maps"][1]["inputs"]["gfc"] = self.plan["maps"][1]["inputs"]["gfc"]
        conflict["maps"][1]["inputs"]["gob"] = self.plan["maps"][1]["inputs"]["gob"]
        conflict["maps"][1]["inputs"]["shared_gfc"]["sha256"] = "f" * 64
        with self.assertRaisesRegex(ValueError, "conflicting"): prepare.derive_groups(conflict)
        invalid = copy.deepcopy(self.plan); invalid["maps"][0]["inputs"]["gfc"]["bytes"] = True
        with self.assertRaises(ValueError): prepare.derive_groups(invalid)

    def test_read_only_preflight_hashes_every_extent_without_outputs(self):
        before = set(self.root.iterdir())
        result = self.perform()
        self.assertEqual(result["archives_verified"], 124)
        self.assertEqual(result["status"], "preflight-only-no-output-created")
        self.assertEqual(before, set(self.root.iterdir()))
        self.assertEqual(self.calls, [])

    def test_iso_mutation_fails_before_any_output(self):
        with self.iso.open("r+b") as stream: stream.write(b"changed")
        before = set(self.root.iterdir())
        with self.assertRaisesRegex(ValueError, "ISO identity mismatch"): self.perform(execute=True)
        self.assertEqual(before, set(self.root.iterdir()))
        self.assertEqual(self.calls, [])

    def test_missing_duplicate_wrong_size_and_outside_inventory_extents_fail(self):
        for mutation in ("missing", "duplicate", "size", "outside", "case", "directory"):
            inventory = copy.deepcopy(self.inventory)
            if mutation == "missing": inventory["entries"].pop()
            elif mutation == "duplicate": inventory["entries"].append(inventory["entries"][0])
            elif mutation == "size": inventory["entries"][0]["size"] = 2
            elif mutation == "outside": inventory["entries"][0]["sector"] = 999999
            elif mutation == "case": inventory["entries"][0]["path"] = inventory["entries"][0]["path"].upper()
            else: inventory["entries"][0]["directory"] = 0
            with self.subTest(mutation=mutation), self.assertRaises(ValueError):
                prepare.selected_extents(inventory, self.context["groups"], self.context["iso"]["bytes"])

    def test_current_extent_or_original_member_hash_mismatch_fails_preflight(self):
        current = copy.deepcopy(self.inventory); current["entries"][0]["sector"] += 1
        with self.assertRaisesRegex(ValueError, "extents differ"):
            prepare.preflight(self.iso, self.context, lambda iso: current)
        context = copy.deepcopy(self.context); context["groups"]["solo"][0]["sha256"] = "f" * 64
        with self.assertRaisesRegex(ValueError, "extent hash"):
            prepare.preflight(self.iso, context, lambda iso: self.inventory)

    def test_unnamed_sanitized_directories_are_not_required_archive_members(self):
        inventory = copy.deepcopy(self.inventory)
        inventory["entries"].append({"directory": True, "sector": 0, "size": 10})
        self.assertEqual(prepare.selected_extents(inventory, self.context["groups"], self.context["iso"]["bytes"]), self.extents)
        inventory["entries"][-1]["directory"] = False
        with self.assertRaises((KeyError, ValueError)):
            prepare.selected_extents(inventory, self.context["groups"], self.context["iso"]["bytes"])

    def test_fresh_paths_reject_existing_overlap_unsafe_prefix_and_reparse(self):
        for prefix in ("../bad", "a/b", "a:b", "", "x" * 49):
            with self.assertRaises(ValueError): prepare.fresh_paths(self.root, prefix, self.source, self.iso)
        with self.assertRaisesRegex(ValueError, "overlaps"):
            prepare.fresh_paths(self.source, "originals", self.source, self.iso)
        (self.root / "originals-solo").mkdir()
        with self.assertRaisesRegex(ValueError, "already exists"):
            prepare.fresh_paths(self.root, "originals", self.source, self.iso)
        with mock.patch.object(prepare.checkout, "safe_path", side_effect=ValueError("reparse point")):
            with self.assertRaisesRegex(ValueError, "reparse"): prepare.absolute(self.root)

    def test_execute_extracts_once_per_group_and_writes_metadata_only_session(self):
        result = self.perform(execute=True)
        self.assertEqual(result["status"], "original-archive-witnesses-verified")
        self.assertEqual(result["archives_verified"], 124)
        self.assertEqual(self.calls, ["originals-solo", "originals-coop", "originals-shared"])
        session = (self.root / "originals-session.json").read_text()
        self.assertNotIn(str(self.root), session)
        self.assertNotIn("private synthetic", session)
        self.assertNotIn("command", session)
        self.assertNotIn("active_group", session)

    def test_failed_extraction_stops_and_preserves_incomplete_session(self):
        def failing(source, iso, destination, members, log):
            self.calls.append(destination.name)
            raise subprocess.CalledProcessError(2, ["synthetic private command"])
        with self.assertRaises(subprocess.CalledProcessError): self.perform(execute=True, extract=failing)
        self.assertEqual(self.calls, ["originals-solo"])
        session = json.loads((self.root / "originals-session.json").read_bytes())
        self.assertEqual(session["status"], "incomplete")
        self.assertEqual(session["active_group"], "solo")
        self.assertEqual(session["failure_type"], "CalledProcessError")

    def test_iso_mutation_during_extraction_is_rejected_at_end(self):
        def mutate(source, iso, destination, members, log):
            self.fake_extract(source, iso, destination, members, log)
            if destination.name.endswith("shared"):
                with self.iso.open("r+b") as stream: stream.write(b"changed")
        with self.assertRaisesRegex(ValueError, "ISO identity mismatch"): self.perform(execute=True, extract=mutate)
        session = json.loads((self.root / "originals-session.json").read_bytes())
        self.assertEqual(session["status"], "incomplete")
        self.assertEqual(len(session["groups"]), 3)

    def test_physical_extra_files_and_wrong_hash_stop_before_next_group(self):
        for mutation in ("extra", "hash"):
            with self.subTest(mutation=mutation), tempfile.TemporaryDirectory() as folder:
                destination = Path(folder) / "group"
                log = Path(folder) / "log"
                members = self.context["groups"]["shared"]
                self.fake_extract(self.source, self.iso, destination, members, log)
                if mutation == "extra": (destination / "extra.txt").write_text("unexpected")
                else: (destination / members[0]["member"]).write_bytes(b"z")
                with self.assertRaises(ValueError):
                    prepare.verify_group("shared", destination, members, self.extents, self.context["iso"])

    def test_receipt_missing_extra_conflicting_member_or_iso_rejected(self):
        for mutation in ("missing", "extra", "size-bool", "iso"):
            with self.subTest(mutation=mutation), tempfile.TemporaryDirectory() as folder:
                destination = Path(folder) / "group"
                members = self.context["groups"]["shared"]
                self.fake_extract(self.source, self.iso, destination, members, Path(folder) / "log")
                path = destination / prepare.MANIFEST
                row = json.loads(path.read_bytes())
                if mutation == "missing": row["files"].pop()
                elif mutation == "extra": row["files"].append(row["files"][0])
                elif mutation == "size-bool": row["files"][0]["size"] = True
                else: row["image"]["sha256"] = "f" * 64
                path.write_text(json.dumps(row))
                with self.assertRaises(ValueError):
                    prepare.verify_group("shared", destination, members, self.extents, self.context["iso"])

    def test_fixed_extractor_flags_no_shell_and_no_arbitrary_plan_argv(self):
        members = self.context["groups"]["shared"]
        with mock.patch.object(prepare.subprocess, "run") as run:
            prepare.extract_group(self.source, self.iso, self.root / "fresh", members, self.root / "log")
        args, kwargs = run.call_args
        command = args[0]
        self.assertIn("extract", command)
        self.assertEqual(command.count("--include"), 2)
        self.assertEqual(command[-4:], ["--include", "assets.gfc", "--include", "assets.gob"])
        self.assertFalse(kwargs["shell"])
        self.assertTrue(kwargs["check"])

    def test_json_rejects_duplicate_keys_and_nan(self):
        for value in ('{"a":1,"a":2}', '{"a":NaN}'):
            with self.assertRaises(ValueError): prepare.read_json(value)

    def test_cli_default_is_preflight_and_uses_current_lock(self):
        with mock.patch.object(sys, "argv", ["prepare", "--source", str(self.source), "--iso", str(self.iso),
                                              "--output-parent", str(self.root)]), \
             mock.patch.object(prepare, "prepare", return_value={"status": "synthetic", "archives_verified": 124}) as run, \
             mock.patch("builtins.print"):
            self.assertEqual(prepare.main(), 0)
        self.assertFalse(run.call_args.args[5])
        self.assertEqual(run.call_args.args[1], prepare.checkout.LOCK)


if __name__ == "__main__": unittest.main()
