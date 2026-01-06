# -*- coding: utf-8 -*-
# Theme-Me/main/th11.py
# Credit by Zidan IDz
import os, sys, time, shutil
from support.echo import theme_me, abu, pxh, netral, putih, kuning, hijau, merah
from support.lib import load, message


def th11():
    os.system("clear")
    print(theme_me)
    print(f"        {abu}THEME-ME {pxh} Ethereal Cranium {netral}")
    print(f"\n{putih}({kuning}*{putih}) {abu}'username' and 'team name' will be displayed below the logo")
    username = input(f"\n{putih}enter username   {hijau}>{putih} ")
    while not username.strip() or '"' in username or "'" in username:
        print(f"{abu}({merah}X{abu}) must not be blank or contain quotation marks {merah}!!")
        username = input(f"\n{putih}enter username   {hijau}>{putih} ")
        continue
    time.sleep(0.5)
    team = input(f"\n{putih}enter team name  {hijau}>{putih} ")
    while not team.strip() or '"' in team or "'" in team:
        print(f"{abu}({merah}X{abu}) must not be blank or contain quotation marks {merah}!! ")
        team = input(f"\n{putih}enter team name  {hijau}>{putih}")
        continue
    print(f"\n{putih}[{hijau}!{putih}] changing the Termux theme  ")
    load()
    file = "theme.py"
    fill = """#Created with the THEME-ME coded by Zidan IDz 
import os, sys, time

def run(a):
    for n in a + '\\n':
        sys.stdout.write(n)
        sys.stdout.flush()
        time.sleep(0.1/100)

logo = '''
\033[97m                    uuuuuuu
                uuSSSSSSSSSSSuu
             uuSSSSSSSSSSSSSSSSSuu
            uSSSSSSSSSSSSSSSSSSSSSu
           uSSSSSSSSSSSSSSSSSSSSSSSu
          uSSSSSSSSSSSSSSSSSSSSSSSSSu
          uSSSSSSSSSSSSSSSSSSSSSSSSSu
          uSSSSSS“   “SSS“   “SSSSSSu
          “SSSS“      uSu       SSSS“
           SSSu       uSu       uSSS
           SSSu      uSSSu      uSSS
            “SSSSuuSSS   SSSuuSSSS“
             “SSSSSSS“   “SSSSSSS“
               uSSSSSSSuSSSSSSSu
                uS“S“S“S“S“S“Su
     uuu        SSuS S S S SuSS       uuu
    uSSSS        SSSSSuSuSuSSS       uSSSS
     SSSSSuu      “SSSSSSSSS“     uuSSSSSS
   uSSSSSSSSSSSuu    “““““    uuuuSSSSSSSSSS
   SSSS“““SSSSSSSSSSuuu   uuSSSSSSSSS“““SSS“
    “““      ““SSSSSSSSSSSuu ““S“““
              uuuu ““SSSSSSSSSSuuu
     uSSSuuuSSSSSSSSSuu ““SSSSSSSSSSSuuuSSS
     SSSSSSSSSS““““           ““SSSSSSSSSSS“
      “SSSSS“                      ““SSSS““
        SSS“                         SSSS“         '''
        
run(logo)
print('''              \033[97m Username : \033[97;41m """+username+""" \033[0m''')
print('''            \033[97m Team :\033[90m """+team+""" \033[0m''')  """
    with open(file, "w") as y:
        y.write(fill)
    of = "theme.py"
    into = os.path.join(os.environ["HOME"], "..", "usr", "etc", "theme.py")
    und = os.path.join(os.environ["HOME"], "..", "usr", "etc", "motd")
    if os.path.exists(into):
        os.remove(into)
    elif os.path.exists(und):
        os.remove(und)

    while True:
        try:
            shutil.move(of, into)
            message("theme")
            break
        except Exception as e:
            with open(file, "w") as y:
                y.write(fill)
            time.sleep(1)
