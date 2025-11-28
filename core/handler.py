import os
import json
import shutil
import time
from pathlib import Path
from core.utils import print_error, print_success, print_info, print_warning
from core.config import update_config

DATA_DIR = Path("data")
THEMES_FILE = DATA_DIR / "themes.json"
FONTS_FILE = DATA_DIR / "fonts.json"
BACKGROUNDS_FILE = DATA_DIR / "backgrounds.json"
TEMPLATES_DIR = DATA_DIR / "templates"

TERMUX_DIR = Path.home() / ".termux"
TERMUX_COLORS = TERMUX_DIR / "colors.properties"
TERMUX_FONT = TERMUX_DIR / "font.ttf"
USR_ETC = Path.home() / "../usr/etc"
THEME_PY = USR_ETC / "theme.py"
MOTD_FILE = USR_ETC / "motd"
BASHRC_FILE = USR_ETC / "bashrc"  # Updated to use new standardized name

def load_json(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        print_error(f"Failed to load {file_path}: {e}")
        return []

def get_themes():
    return load_json(THEMES_FILE)

def get_fonts():
    return load_json(FONTS_FILE)

def get_backgrounds():
    return load_json(BACKGROUNDS_FILE)

def apply_theme(theme_name):
    themes = get_themes()
    theme = next((t for t in themes if t["name"].lower() == theme_name.lower() or t["id"] == theme_name), None)
    
    if not theme:
        print_error(f"Theme '{theme_name}' not found.")
        return False

    print_info(f"Applying theme: {theme['name']}...")
    
    # Use default username/team for now, or could prompt if interactive
    username = "User" 
    team = "Termux"
    
    # Read ASCII art from file
    logo = ""
    if theme.get("path") and os.path.exists(theme["path"]):
        try:
            with open(theme["path"], "r", encoding="utf-8") as f:
                logo = f.read()
                # Escape backslashes for python string literal in theme.py
                # Actually, we are putting it into a triple quoted string.
                # We just need to be careful about triple quotes inside the logo.
                logo = logo.replace("'''", "\\'\\'\\'") 
        except Exception as e:
            print_error(f"Failed to read theme file: {e}")
    else:
        # Fallback if path missing (shouldn't happen if migration worked)
        logo = theme.get("ascii_art", "Logo missing")
    
    theme_py_content = f"""# Created with THEME-ME v3.0
import os, sys, time

def run(a):
    for n in a + '\\n':
        sys.stdout.write(n)
        sys.stdout.flush()
        time.sleep(0.001)

logo = '''{logo}'''

run(logo)
print('''             \033[97m Username : \033[97;41m {username} \033[0m''')
print('''           \033[97m Team :\033[90m {team} \033[0m''')
"""

    try:
        if not USR_ETC.exists():
             # Fallback for non-termux testing
             print_warning(f"{USR_ETC} does not exist. Using local 'test_output' directory.")
             local_out = Path("test_output")
             local_out.mkdir(exist_ok=True)
             target_file = local_out / "theme.py"
        else:
             target_file = THEME_PY

        with open(target_file, "w", encoding="utf-8") as f:
            f.write(theme_py_content)
            
        update_config("current_theme", theme["name"])
        print_success(f"Theme '{theme['name']}' applied successfully!")
        return True
        
    except Exception as e:
        print_error(f"Failed to apply theme: {e}")
        return False

def apply_font(font_name):
    fonts = get_fonts()
    font = next((f for f in fonts if f["name"].lower() == font_name.lower() or f["id"] == font_name), None)
    
    if not font:
        print_error(f"Font '{font_name}' not found.")
        return False
        
    print_info(f"Applying font: {font['name']}...")
    
    try:
        # Check if local file exists
        if font.get("is_local") and font.get("url"):
             # The URL in json points to .txt file
             source_path = Path(font["url"])
             if not source_path.exists():
                 print_error(f"Local font file missing: {source_path}")
                 return False
             
             if not TERMUX_DIR.exists():
                TERMUX_DIR.mkdir(parents=True, exist_ok=True)
                
             # Copy .txt file and rename to .ttf
             shutil.copy(source_path, TERMUX_FONT)
             print_info(f"Converted {source_path.name} -> font.ttf")
        else:
            print_error("Font is not available locally. Please run setup to download resources.")
            return False

        os.system("termux-reload-settings")
        update_config("current_font", font["name"])
        print_success(f"Font '{font['name']}' applied successfully!")
        return True
    except Exception as e:
        print_error(f"Failed to apply font: {e}")
        return False

def apply_background(bg_name):
    bgs = get_backgrounds()
    bg = next((b for b in bgs if b["name"].lower() == bg_name.lower() or b["id"] == bg_name), None)
    
    if not bg:
        print_error(f"Background '{bg_name}' not found.")
        return False
        
    print_info(f"Applying background: {bg['name']}...")
    
    try:
        if bg.get("is_local") and bg.get("url"):
             # The URL in json points to .txt file
             source_path = Path(bg["url"])
             if not source_path.exists():
                 print_error(f"Local background file missing: {source_path}")
                 return False
             
             if not TERMUX_DIR.exists():
                TERMUX_DIR.mkdir(parents=True, exist_ok=True)
                
             # Copy .txt file and rename to colors.properties
             shutil.copy(source_path, TERMUX_COLORS)
             print_info(f"Converted {source_path.name} -> colors.properties")
        else:
            print_error("Background is not available locally. Please run setup to download resources.")
            return False
            
        os.system("termux-reload-settings")
        update_config("current_background", bg["name"])
        print_success(f"Background '{bg['name']}' applied successfully!")
        return True
    except Exception as e:
        print_error(f"Failed to apply background: {e}")
        return False

def restore_defaults():
    print_info("Restoring defaults...")
    try:
        if TERMUX_FONT.exists():
            TERMUX_FONT.unlink()
        if TERMUX_COLORS.exists():
            TERMUX_COLORS.unlink()
            
        if THEME_PY.exists():
            THEME_PY.unlink()
            
        # Restore motd and bashrc from templates (.txt files)
        if (TEMPLATES_DIR / "motd.txt").exists():
            shutil.copy(TEMPLATES_DIR / "motd.txt", MOTD_FILE)
            print_info("Restored motd from template")
            
        if (TEMPLATES_DIR / "bashrc.txt").exists():
            shutil.copy(TEMPLATES_DIR / "bashrc.txt", BASHRC_FILE)
            print_info("Restored bashrc from template")
            
        os.system("termux-reload-settings")
        print_success("Restored to default settings.")
        
        update_config("current_theme", None)
        update_config("current_font", None)
        update_config("current_background", None)
        return True
    except Exception as e:
        print_error(f"Failed to restore: {e}")
        return False
