from core.utils import RED, WHITE, GRAY, CYAN, YELLOW, RESET
from core.constants import TOOL_NAME, VERSION, VERSION_TAG, AUTHOR, GITHUB_URL, DESCRIPTION, TOTAL_THEMES, TOTAL_FONTS, TOTAL_BACKGROUNDS
import os

def show_about():
    """Display about information"""

    if os.path.exists("since.txt"):
        with open("since.txt", "r", encoding="utf-8") as f:
            since = f.read().strip()
    else:
        since = "2020 - 2025"
    
    about_text = f"""
{GRAY}+-------------------------------------------------------+
|{RESET}                   ABOUT {TOOL_NAME.upper()}                      {GRAY}|
+-------------------------------------------------------+{RESET}

  {TOOL_NAME} is a simple {DESCRIPTION}
  that allows you to personalize your Termux experience.
  
  {WHITE}Features:{RESET}
  * {TOTAL_THEMES} unique themes with custom ASCII art
  * {TOTAL_FONTS} professional fonts
  * {TOTAL_BACKGROUNDS} color schemes (backgrounds)
  * Easy restore to defaults
  * Full offline support
  
  {WHITE}Version:{RESET} {YELLOW}{VERSION}{RESET} ({VERSION_TAG})
  {WHITE}Author:{RESET}  {AUTHOR}
  {WHITE}Since:{RESET}   {since}
  {WHITE}GitHub:{RESET}  {CYAN}{GITHUB_URL}{RESET}

{GRAY}+-------------------------------------------------------+{RESET}
"""
    print(about_text)
