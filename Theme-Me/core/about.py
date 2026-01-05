from core.utils import RED, WHITE, GRAY, CYAN, YELLOW, RESET
from core.constants import TOOL_NAME, VERSION, VERSION_TAG, AUTHOR, GITHUB_URL, DESCRIPTION, TOTAL_THEMES, TOTAL_FONTS, TOTAL_BACKGROUNDS
import os

def show_about():
    if os.path.exists("since.txt"):
        with open("since.txt", "r", encoding="utf-8") as f:
            since = f.read().strip()
    else:
        return
    
    about_text = f"""{GRAY}
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃              ABOUT {TOOL_NAME.upper():<17}      ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
{RESET}{TOOL_NAME} is a simple {DESCRIPTION}
that allows you to personalize your Termux experience

{WHITE}Features:{RESET}
* {TOTAL_THEMES} unique themes with ASCII art
* {TOTAL_FONTS} professional fonts
* {TOTAL_BACKGROUNDS} color schemes
* Dual mode: menu & CLI arguments
* Personalization: custom username/team
* Restore defaults
* Update tool
* Full offline support

{WHITE}Version:{RESET} {YELLOW}{VERSION}{RESET} ({VERSION_TAG})
{WHITE}Author:{RESET}  {AUTHOR}
{WHITE}Since:{RESET}   {since}
{WHITE}GitHub:{RESET}  {CYAN}{GITHUB_URL}
{RESET}"""

    print(about_text)
