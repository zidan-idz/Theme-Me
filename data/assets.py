# -*- coding: utf-8 -*-
from core.utils import CYAN, WHITE, GRAY, RED, BLKONWHT, RESET
from core.constants import DESCRIPTION, GITHUB_URL, VERSION

BANNER = f"""{CYAN}
{WHITE}████████╗██╗  ██╗███████╗{RED}███╗   ███╗███████╗
{WHITE}╚══██╔══╝██║  ██║██╔════╝{RED}████╗ ████║██╔════╝
{WHITE}   ██║   ███████║█████╗  {RED}██╔████╔██║█████╗  
{WHITE}   ██║   ██╔══██║██╔══╝  {RED}██║╚██╔╝██║██╔══╝  
{WHITE}   ██║   ██║  ██║███████╗{RED}██║ ╚═╝ ██║███████╗
{WHITE}   ╚═╝   ╚═╝  ╚═╝╚══════╝{RED}╚═╝     ╚═╝╚══════╝
  {BLKONWHT} THEME-ME {DESCRIPTION} v{VERSION} {RESET} {GRAY}
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃   {GRAY}{GITHUB_URL}   {GRAY}┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛"""

MENU = f"""{WHITE}┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃              Select an option:            ┃
┣━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
┃ 1 ┃ Change Theme                          ┃
┃ 2 ┃ Change Font                           ┃
┃ 3 ┃ Change Background                     ┃
┃ 4 ┃ Restore Defaults                      ┃
┃ 5 ┃ Report Issue                          ┃
┃ 6 ┃ Update Tool                           ┃
┃ 7 ┃ About                                 ┃
┃ {RED}8{RESET} ┃ {RED}Exit{RESET}                                  ┃
┗━━━┻━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛"""
