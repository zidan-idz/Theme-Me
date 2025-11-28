import argparse
import sys
import webbrowser
from core.constants import TOOL_NAME, VERSION, ISSUES_URL
from core.handler import apply_theme, apply_font, apply_background, restore_defaults, get_themes, get_fonts, get_backgrounds
from core.ui import show_menu, list_items, show_preview
from core.about import show_about
from core.utils import setup_logging, check_termux, print_error, print_success, update_tool

def main():
    setup_logging()
    check_termux()
    
    parser = argparse.ArgumentParser(description=f"{TOOL_NAME} v{VERSION} - Termux Customization Tool")
    
    parser.add_argument("--theme", help="Apply a specific theme by name or ID")
    parser.add_argument("--font", help="Apply a specific font by name or ID")
    parser.add_argument("--background", help="Apply a specific background by name or ID")
    parser.add_argument("--list", choices=["theme", "font", "background"], help="List available options")
    parser.add_argument("--preview", help="Preview a theme by ID")
    parser.add_argument("--restore", action="store_true", help="Restore default settings")
    parser.add_argument("--about", action="store_true", help="Show about information")
    parser.add_argument("--version", action="store_true", help="Show version")
    
    args = parser.parse_args()
    
    if args.version:
        print(f"{TOOL_NAME} v{VERSION}")
        return

    if args.list:
        if args.list == "theme":
            list_items(get_themes(), "Themes")
        elif args.list == "font":
            list_items(get_fonts(), "Fonts")
        elif args.list == "background":
            list_items(get_backgrounds(), "Backgrounds")
        return

    if args.preview:
        show_preview(args.preview)
        return

    if args.theme:
        apply_theme(args.theme)
        return

    if args.font:
        apply_font(args.font)
        return

    if args.background:
        apply_background(args.background)
        return

    if args.restore:
        restore_defaults()
        return

    if args.about:
        show_about()
        return

    # Interactive Mode
    while True:
        show_menu()
        choice = input("\nEnter your choice: ")
        
        if choice == "1":
            list_items(get_themes(), "Themes")
            t = input("\nEnter theme ID/Name to apply (or enter to go back): ")
            if t: apply_theme(t)
        elif choice == "2":
            list_items(get_fonts(), "Fonts")
            f = input("\nEnter font ID/Name to apply (or enter to go back): ")
            if f: apply_font(f)
        elif choice == "3":
            list_items(get_backgrounds(), "Backgrounds")
            b = input("\nEnter background ID/Name to apply (or enter to go back): ")
            if b: apply_background(b)
        elif choice == "4":
            restore_defaults()
            input("\nPress Enter to continue...")
        elif choice == "5":
            print(f"Opening issues page: {ISSUES_URL}")
            webbrowser.open(ISSUES_URL)
            input("\nPress Enter to continue...")
        elif choice == "6":
            update_tool()
            input("\nPress Enter to continue...")
        elif choice == "7":
            show_about()
            input("\nPress Enter to continue...")
        elif choice == "8":
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")
            input("\nPress Enter to continue...")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nExiting...")
        sys.exit(0)
