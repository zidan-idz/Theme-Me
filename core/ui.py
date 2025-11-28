import webbrowser
from core.utils import clear_screen, print_info, RESET, CYAN, WHITE, GREEN, GRAY
from core.handler import get_themes, get_fonts, get_backgrounds
from core.constants import THEMES_WEB_URL
from data.assets import BANNER

def show_menu():
    clear_screen()
    print(BANNER)
    print(f"\n{WHITE}Select an option:{RESET}")
    print(f"  1. Change Theme")
    print(f"  2. Change Font")
    print(f"  3. Change Background")
    print(f"  4. Restore Defaults")
    print(f"  5. Report Issue")
    print(f"  6. Update Tool")
    print(f"  7. About")
    print(f"  8. Exit")
    
def list_items(items, title):
    print(f"\n{WHITE}Available {title}:{RESET}")
    for item in items:
        print(f"  - {item['name']} ({GRAY}ID: {item['id']}{RESET})")

def show_preview(theme_id):
    themes = get_themes()
    theme = next((t for t in themes if t["id"] == theme_id), None)
    if theme:
        print(f"\n{CYAN}Opening preview for {theme['name']} in browser...{RESET}")
        # Construct specific URL if possible, otherwise fallback to general themes folder
        # Assuming themes might have a specific preview URL or we just point to the folder
        url = f"{THEMES_WEB_URL}/{theme['id']}.png" # Example assumption: images are stored as {id}.png
        # Or if we just want to open the general themes page as requested "khusus ke web themes"
        # The user said "misal kalo themes, khusus ke web themes".
        # Let's try to be specific if we can, but maybe just the folder is safer for now if we don't know the image structure.
        # Actually, user said "ganti aja biar redirect ke web. agar semua bisa. misal kalo themes, khusus ke web themes."
        # So for themes -> themes web.
        
        # Let's use the THEMES_WEB_URL.
        webbrowser.open(THEMES_WEB_URL)
        print(f"{GREEN}Opened {THEMES_WEB_URL}{RESET}")
    else:
        print(f"Theme {theme_id} not found.")
