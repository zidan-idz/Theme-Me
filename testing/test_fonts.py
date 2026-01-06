import unittest
import sys
from pathlib import Path

# Add project root to path
sys.path.append(str(Path(__file__).parent.parent))

from core.handler import get_fonts

class TestFonts(unittest.TestCase):
    def test_list_fonts(self):
        fonts = get_fonts()
        self.assertTrue(len(fonts) > 0, "Should have fonts available")
        self.assertIn("name", fonts[0], "Font should have a name")
        
    def test_font_files_exist(self):
        fonts = get_fonts()
        for font in fonts:
            if font.get("is_local") and font.get("url"):
                path = Path(font["url"])
                self.assertTrue(path.exists(), f"Font file missing: {path}")

if __name__ == '__main__':
    unittest.main()
