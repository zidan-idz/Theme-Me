import os
import sys
import logging
from pathlib import Path

# ANSI Colors - Flat & Professional Palette
RESET = "\033[0m"
RED = "\033[31m"      # Darker red (not bright)
GREEN = "\033[32m"    # Darker green
YELLOW = "\033[33m"   # Darker yellow
BLUE = "\033[34m"     # Darker blue
MAGENTA = "\033[35m"  # Darker magenta
CYAN = "\033[36m"     # Darker cyan
WHITE = "\033[37m"    # Normal white (not bright)
GRAY = "\033[90m"     # Dark gray
DIM = "\033[2m"       # Dim text

# Backgrounds (minimal use)
BG_GRAY = "\033[100m"

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def setup_logging():
    logging.basicConfig(
        filename='theme-me.log',
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )

def print_error(message):
    print(f"{RED}[ERROR] {message}{RESET}")
    logging.error(message)

def print_success(message):
    print(f"{GREEN}[SUCCESS] {message}{RESET}")
    logging.info(message)

def print_info(message):
    print(f"{BLUE}[INFO] {message}{RESET}")
    logging.info(message)

def print_warning(message):
    print(f"{YELLOW}[WARNING] {message}{RESET}")
    logging.warning(message)

def check_termux():
    # Simple check, though might not be 100% accurate in all envs
    # But good enough for now.
    if "PREFIX" not in os.environ and os.name != 'nt': # 'nt' for testing on windows
         print_warning("It seems you are not running in Termux. Some features might not work.")

def update_tool():
    print_info("Checking for updates...")
    if os.path.isdir(".git"):
        try:
            os.system("git pull")
            print_success("Update checked/applied.")
        except Exception as e:
            print_error(f"Failed to update: {e}")
    else:
        print_warning("Not a git repository. Cannot auto-update.")
        print_info("Please clone the repository again or download the latest release.")
