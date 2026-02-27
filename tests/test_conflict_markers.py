import subprocess
import unittest


class TestConflictMarkers(unittest.TestCase):
    def test_no_conflict_markers(self):
        proc = subprocess.run(
            ["python", "tools/check_conflict_markers.py"],
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(proc.returncode, 0, msg=proc.stdout + proc.stderr)


if __name__ == "__main__":
    unittest.main()
