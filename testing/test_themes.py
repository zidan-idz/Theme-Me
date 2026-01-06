import unittest
import sys
import os
from pathlib import Path
from unittest.mock import patch, MagicMock

# Add project root to path
sys.path.append(str(Path(__file__).parent.parent))

from core.handler import get_themes, apply_theme

class TestThemes(unittest.TestCase):
    def test_list_themes(self):
        themes = get_themes()
        self.assertTrue(len(themes) > 0, "Should have themes available")
        self.assertIn("name", themes[0], "Theme should have a name")
        
    @patch('builtins.input', side_effect=['TestUser', 'TestTeam'])
    @patch('core.handler.loading_animation') # Mock animation to skip delay
    def test_apply_theme(self, mock_anim, mock_input):
        # Ensure we are in testing mode
        os.environ["THEME_ME_TESTING"] = "1"
        
        # Apply first available theme
        themes = get_themes()
        if themes:
            theme_name = themes[0]["name"]
            print(f"Testing application of theme: {theme_name}")
            success = apply_theme(theme_name)
            self.assertTrue(success, f"Failed to apply theme {theme_name}")
            
            # Check if files were generated in testing/ directory (since we are on Windows)
            # Note: handler.py falls back to 'testing' dir if USR_ETC doesn't exist
            # But wait, we modified handler.py to check env var for IS_TESTING, 
            # but the path logic (USR_ETC) is still based on existence.
            # If we are on Windows, USR_ETC won't exist, so it uses local 'testing' dir.
            
            local_out = Path("testing")
            self.assertTrue((local_out / "theme.py").exists(), "theme.py not created")
            self.assertTrue((local_out / "bashrc").exists(), "bashrc not created")
            self.assertTrue((local_out / "motd").exists(), "motd not created")

if __name__ == '__main__':
    unittest.main()
