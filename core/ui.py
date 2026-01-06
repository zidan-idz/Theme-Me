import webbrowser
from core.utils import clear_screen, print_info, RESET, CYAN, WHITE, GREEN, GRAY
from core.handler import get_themes, get_fonts, get_backgrounds
from core.constants import THEMES_WEB_URL
from data.assets import BANNER, MENU

def show_menu():
    clear_screen()
    print(BANNER)
    print(MENU)
    
def list_items(items, title):
    print(f"\n{WHITE}Available {title}:{RESET}")
    for item in items:
        print(f"  - {item['name']} ({GRAY}ID: {item['id']}{RESET})")

def show_preview(theme_id):
    themes = get_themes()
    theme = next((t for t in themes if t["id"] == theme_id), None)
    if theme:
        print(f"\n{CYAN}Opening preview for {theme['name']} in browser...{RESET}")
        webbrowser.open(THEMES_WEB_URL)
        print(f"{GREEN}Opened {THEMES_WEB_URL}{RESET}")
    else:
        print(f"Theme {theme_id} not found.")
