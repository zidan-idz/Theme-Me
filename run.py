# -*- coding: utf-8 -*-
from core.utils import print_error
import sys
import os

# Set UTF-8 encoding for stdout/stderr (Windows compatibility)
if sys.platform == 'win32':
    import codecs
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')
    sys.stderr = codecs.getwriter('utf-8')(sys.stderr.buffer, 'strict')

from core.utils import print_info
from core.utils import RED, WHITE, GRAY
import argparse
import webbrowser
from core.constants import TOOL_NAME, VERSION, ISSUES_URL
from core.handler import apply_theme, apply_font, apply_background, restore_defaults, get_themes, get_fonts, get_backgrounds
from core.ui import show_menu, list_items, show_preview
from core.about import show_about
from core.utils import setup_logging, check_termux, print_info, update_tool, enter_to_continue

def main():
    setup_logging()
    check_termux()
    
    parser = argparse.ArgumentParser(description=f"{TOOL_NAME} v{VERSION} - Termux Customization Tool")
    
    parser.add_argument("--theme", help="Apply a specific theme by name or ID")
    parser.add_argument("--font", help="Apply a specific font by name or ID")
    parser.add_argument("--background", help="Apply a specific background by name or ID")
    parser.add_argument("--list", choices=["theme", "font", "background"], help="List available options")
    # parser.add_argument("--preview", help="Preview a theme by ID")
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

    # if args.preview:
    #     show_preview(args.preview)
    #     return

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
        choice = input(F"\n{RED}@root{WHITE}/{RED}Theme-Me{WHITE} # ")

        
        if choice == "1":
            list_items(get_themes(), "Themes")
            print_info(f"Enter theme ID/Name to apply (or enter to go back)")
            t = input(F"{RED}@root{WHITE}/{RED}Theme-Me{WHITE}/{RED}Themes{WHITE} # ")
            if t: 
                apply_theme(t)
                enter_to_continue()
        elif choice == "2":
            list_items(get_fonts(), "Fonts")
            print_info("Enter font ID/Name to apply (or enter to go back): ")
            f = input(F"{RED}@root{WHITE}/{RED}Theme-Me{WHITE}/{RED}Fonts{WHITE} # ")
            if f: 
                apply_font(f)
                enter_to_continue()
        elif choice == "3":
            list_items(get_backgrounds(), "Backgrounds")
            print_info("Enter background ID/Name to apply (or enter to go back): ")
            b = input(F"{RED}@root{WHITE}/{RED}Theme-Me{WHITE}/{RED}Backgrounds{WHITE} # ")
            if b: 
                apply_background(b)
                enter_to_continue()
        elif choice == "4":
            restore_defaults()
            enter_to_continue()
        elif choice == "5":
            print_info("If the page doesn’t open automatically, you can open it manually using the link provided.")
            print(f"Issues page: {ISSUES_URL}")
            os.system(f"xdg-open {ISSUES_URL}")
            enter_to_continue()
        elif choice == "6":
            update_tool()
            enter_to_continue()
        elif choice == "7":
            show_about()
            enter_to_continue()
        elif choice == "8":
            print("See you later!")
            break
        else:
            print_error("Invalid choice!")
            enter_to_continue()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nExiting...")
        sys.exit(0)
