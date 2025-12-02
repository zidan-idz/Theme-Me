import os
import sys
import logging
import time
import json
import random
import threading
from pathlib import Path

RESET = "\033[0m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
WHITE = "\033[37m"
GRAY = "\033[90m"
BLKONWHT = "\033[90;107m"
DIM = "\033[2m"

BG_GRAY = "\033[100m"

DATA_DIR = Path("data")
DATA_JSON = DATA_DIR / "data.json"

def load_tips():
    try:
        if DATA_JSON.exists():
            with open(DATA_JSON, "r", encoding="utf-8") as f:
                data = json.load(f)
                return data.get("tips", [])
        return []
    except Exception:
        return []

def loading_animation(duration=2, message=None):
    loading_text = "Loading..."
    if message:
        loading_text = message
    else:
        tips = load_tips()
        if tips:
            tip = random.choice(tips)
            print(f"\n{WHITE}[TIPS] {tip}{RESET}{WHITE}")
    chars = "|/-\\"
    start_time = time.time()
    sys.stdout.write("\033[?25l")
    try:
        while time.time() - start_time < duration:
            for char in chars:
                sys.stdout.write(f"\r{WHITE}{char} {loading_text}{RESET}")
                sys.stdout.flush()
                time.sleep(0.1)
                if time.time() - start_time >= duration:
                    break
    finally:
        sys.stdout.write("\r" + " " * (len(loading_text) + 4) + "\r")
        sys.stdout.write("\033[?25h")
        sys.stdout.flush()

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def setup_logging():
    logging.basicConfig(
        filename='theme-me.log',
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )

def print_error(message):
    print(f"\n{RED}[ERROR] {message}{RESET}")
    logging.error(message)

def print_success(message):
    print(f"\n{GREEN}[SUCCESS] {message}{RESET}")
    logging.info(message)

def print_info(message):
    print(f"\n{GRAY}[INFO] {message}{RESET}")
    logging.info(message)

def print_verbose(message):
    logging.info(message)

def print_warning(message):
    print(f"\n{YELLOW}[WARNING] {message}{RESET}")
    logging.warning(message)

def enter_to_continue():
    print(f"\n{GRAY}[INFO] Press Enter to continue")
    input(F"{RED}@root{WHITE}/{RED}Theme-Me{WHITE}/{RED}Themes{WHITE} # ")

def check_termux():
    if "PREFIX" not in os.environ and os.name != 'nt':
         print_warning("It seems you are not running in Termux. Some features might not work.")

def update_tool():
    print_info("Checking for updates...")
    loading_animation(duration=2)
    if os.path.isdir(".git"):
        try:
            print("")
            os.system("git pull")
            # print_success('The process completed without any issues')
            print_success("Update checked/applied.")
        except Exception as e:
            # print_error('The process completed with issues')
            print_error(f"Failed to update: {e}")
    else:
        print_warning("Not a git repository. Cannot auto-update.")
        print_info("Please clone the repository again or download the latest release.")
