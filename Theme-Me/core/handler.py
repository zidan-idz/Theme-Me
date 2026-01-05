import os
import json
import shutil
import time
from pathlib import Path
from core.utils import print_error, print_success, print_info, print_verbose, loading_animation
from core.config import update_config
from core.utils import RED, WHITE
from core.constants import VERSION, VERSION_TAG

DATA_DIR = Path("data")
THEMES_FILE = DATA_DIR / "themes.json"
FONTS_FILE = DATA_DIR / "fonts.json"
BACKGROUNDS_FILE = DATA_DIR / "backgrounds.json"
TEMPLATES_DIR = DATA_DIR / "templates"

TERMUX_DIR = Path.home() / ".termux"
TERMUX_COLORS = TERMUX_DIR / "colors.properties"
TERMUX_FONT = TERMUX_DIR / "font.ttf"
USR_ETC = (Path.home() / "../usr/etc").resolve()
THEME_PY = USR_ETC / "theme.py"
MOTD_FILE = USR_ETC / "motd"
BASHRC_FILE = USR_ETC / "bash.bashrc"

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

def copy_to_lf(src, dst):
    """Salin file dari src ke dst, paksa akhiran baris LF saja."""
    try:
        with open(src, "r", encoding="utf-8") as f_src:
            content = f_src.read()
        # Secara eksplisit ganti CRLF dengan LF, lalu hapus sisa CR
        content = content.replace("\r\n", "\n").replace("\r", "\n")
        with open(dst, "w", encoding="utf-8", newline="\n") as f_dst:
            f_dst.write(content)
        return True
    except Exception as e:
        print_error(f"Failed to copy {src} to {dst}: {e}")
        return False

def apply_theme(theme_name, username="User", team="Termux"):
    themes = get_themes()
    theme = next((t for t in themes if t["name"].lower() == theme_name.lower() or t["id"] == theme_name), None)
    if not theme:
        print_error(f"Theme '{theme_name}' not found.")
        return False
    
    print_info("Enter custom username (default: User):")
    username = input(f"{RED}@root{WHITE}/{RED}Theme-Me{WHITE}/{RED}Username{WHITE} # ") or "User"
    print_info("Enter custom team name (default: Termux):")
    team = input(f"{RED}@root{WHITE}/{RED}Theme-Me{WHITE}/{RED}Team{WHITE} # ") or "Termux"
    
    print_info(f"Applying theme: {theme['name']}...")
    loading_animation(duration=2)
    
    logo = ""
    theme_path = theme.get("path")
    if theme_path and os.path.exists(theme_path):
        try:
            with open(theme_path, "r", encoding="utf-8") as f:
                logo = f.read()
                logo = logo.replace('"""', '\\"\\"\\"')
        except Exception as e:
            print_error(f"Failed to read theme file: {e}")
    else:
        logo = theme.get("ascii_art", "Logo missing")
    
    theme_py_content = f'''# Created with THEME-ME v{VERSION} ({VERSION_TAG})
import os, sys, time

def run(a):
    for n in a + '\\n':
        sys.stdout.write(n)
        sys.stdout.flush()
        time.sleep(0.001)

logo = """{logo}"""

run(logo)
print(f"             \033[97m Username : \033[97;41m {username} \033[0m")
print(f"           \033[97m Team :\033[90m {team} \033[0m")
'''

    try:
        if not USR_ETC.exists():
            local_out = Path("test_output")
            local_out.mkdir(exist_ok=True)
            target_file = local_out / "theme.py"
            target_motd = local_out / "motd"
            target_bashrc = local_out / "bash.bashrc"
        else:
            target_file = THEME_PY
            target_motd = MOTD_FILE
            target_bashrc = BASHRC_FILE

        # STRATEGI BACKUP: Buat cadangan bash.bashrc jika ada dan backup belum ada
        if target_bashrc.exists():
            backup_path = target_bashrc.parent / "bash.bashrc.bak"
            if not backup_path.exists():
                try:
                    shutil.copy2(target_bashrc, backup_path)
                    print_info(f"Backup created at {backup_path}")
                except Exception as e:
                    print_error(f"Failed to create backup: {e}") 
                    # Kita lanjutkan, tapi beri peringatan. Mode ketat mungkin akan berhenti.

        with open(target_file, "w", encoding="utf-8", newline="\n") as f:
            f.write(theme_py_content)

        # Salin motd & bashrc bertema
        motd_template = TEMPLATES_DIR / "motd_themed.txt"
        bashrc_template = TEMPLATES_DIR / "bashrc_themed.txt"
        if motd_template.exists():
            copy_to_lf(motd_template, target_motd)
        if bashrc_template.exists():
            copy_to_lf(bashrc_template, target_bashrc)

        update_config("current_theme", theme["name"])
        print_success('The process completed without any issues')
        print_success(f"Theme '{theme['name']}' applied successfully!")
        return True
    except Exception as e:
        print_error('The process completed with issues')
        print_error(f"Failed to apply theme: {e}")
        return False

def apply_font(font_name):
    fonts = get_fonts()
    font = next((f for f in fonts if f["name"].lower() == font_name.lower() or f["id"] == font_name), None)
    if not font:
        print_error(f"Font '{font_name}' not found.")
        return False
    
    print_info(f"Applying font: {font['name']}...")
    loading_animation(duration=2)
    
    try:
        if font.get("is_local") and font.get("url"):
            source_path = Path(font["url"])
            if not source_path.exists():
                print_error(f"Local font file missing: {source_path}")
                return False
            if not TERMUX_DIR.exists():
                TERMUX_DIR.mkdir(parents=True, exist_ok=True)
            shutil.copy(source_path, TERMUX_FONT)
        else:
            print_error("Font is not available locally. Please run setup to download resources.")
            return False

        os.system("termux-reload-settings")
        update_config("current_font", font["name"])
        print_success('The process completed without any issues')
        print_success(f"Font '{font['name']}' applied successfully!")
        return True
    except Exception as e:
        print_error('The process completed with issues')
        print_error(f"Failed to apply font: {e}")
        return False

def apply_background(bg_name):
    bgs = get_backgrounds()
    bg = next((b for b in bgs if b["name"].lower() == bg_name.lower() or b["id"] == bg_name), None)
    if not bg:
        print_error(f"Background '{bg_name}' not found.")
        return False
        
    print_info(f"Applying background: {bg['name']}...")
    loading_animation(duration=2)
    
    try:
        if bg.get("is_local") and bg.get("url"):
            source_path = Path(bg["url"])
            if not source_path.exists():
                print_error(f"Local background file missing: {source_path}")
                return False
            if not TERMUX_DIR.exists():
                TERMUX_DIR.mkdir(parents=True, exist_ok=True)
            shutil.copy(source_path, TERMUX_COLORS)
        else:
            print_error("Background is not available locally. Please run setup to download resources.")
            return False
            
        os.system("termux-reload-settings")
        update_config("current_background", bg["name"])
        print_success('The process completed without any issues')
        print_success(f"Background '{bg['name']}' applied successfully!")
        return True
    except Exception as e:
        print_error('The process completed with issues')
        print_error(f"Failed to apply background: {e}")
        return False

def restore_defaults():
    print_info("Restoring defaults...")
    loading_animation(duration=2)
    try:
        if not USR_ETC.exists():
            local_out = Path("test_output")
            local_out.mkdir(exist_ok=True)
            target_motd = local_out / "motd"
            target_bashrc = local_out / "bash.bashrc"
        else:
            target_motd = MOTD_FILE
            target_bashrc = BASHRC_FILE

        if TERMUX_FONT.exists():
            TERMUX_FONT.unlink()
        if TERMUX_COLORS.exists():
            TERMUX_COLORS.unlink()
        if THEME_PY.exists():
            THEME_PY.unlink()

        # Salin template bawaan
        motd_default = TEMPLATES_DIR / "motd.txt"
        bashrc_default = TEMPLATES_DIR / "bashrc.txt"
        if motd_default.exists():
            copy_to_lf(motd_default, target_motd)
        if bashrc_default.exists():
            copy_to_lf(bashrc_default, target_bashrc)

        if USR_ETC.exists():
            os.system("termux-reload-settings")

        print_success('The process completed without any issues')
        print_success("Restored to default settings.")
        update_config("current_theme", None)
        update_config("current_font", None)
        update_config("current_background", None)
        return True
    except Exception as e:
        print_error('The process completed with issues')
        print_error(f"Failed to restore: {e}")
        return False
