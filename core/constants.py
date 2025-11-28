# Theme-Me Configuration
# This file contains global constants used throughout the application

# Application Info
TOOL_NAME = "Theme-Me"
VERSION = "3.0"
VERSION_TAG = "YuzuKi-stable"
AUTHOR = "Zidan IDz"
GITHUB_URL = "https://github.com/zidan-idz/Theme-Me"
DESCRIPTION = "Termux Customization Tool"
ISSUES_URL = f"{GITHUB_URL}/issues"
THEMES_WEB_URL = f"{GITHUB_URL}/tree/main/data/themes" # Fallback to repo folder for now

# Paths
DATA_DIR = "data"
THEMES_DIR = f"{DATA_DIR}/themes"
FONTS_DIR = f"{DATA_DIR}/fonts"
BACKGROUNDS_DIR = f"{DATA_DIR}/backgrounds"
TEMPLATES_DIR = f"{DATA_DIR}/templates"

# File names
THEMES_JSON = "themes.json"
FONTS_JSON = "fonts.json"
BACKGROUNDS_JSON = "backgrounds.json"

# Termux paths (will be used in handler)
TERMUX_DIR = "~/.termux"
USR_ETC = "~/usr/etc"

# Feature counts
TOTAL_THEMES = 20
TOTAL_FONTS = 20
TOTAL_BACKGROUNDS = 20
