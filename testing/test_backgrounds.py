import unittest
import sys
from pathlib import Path

# Add project root to path
sys.path.append(str(Path(__file__).parent.parent))

from core.handler import get_backgrounds

class TestBackgrounds(unittest.TestCase):
    def test_list_backgrounds(self):
        bgs = get_backgrounds()
        self.assertTrue(len(bgs) > 0, "Should have backgrounds available")
        self.assertIn("name", bgs[0], "Background should have a name")
        
    def test_background_files_exist(self):
        bgs = get_backgrounds()
        for bg in bgs:
            if bg.get("is_local") and bg.get("url"):
                path = Path(bg["url"])
                self.assertTrue(path.exists(), f"Background file missing: {path}")

if __name__ == '__main__':
    unittest.main()
