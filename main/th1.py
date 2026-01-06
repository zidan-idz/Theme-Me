# -*- coding: utf-8 -*-
# Theme-Me/main/th1.py
# Credit by Zidan IDz
import os, sys, time, shutil
from support.echo import theme_me, abu, pxh, netral, putih, kuning, hijau, merah
from support.lib import load, message


def th1():
    os.system("clear")
    print(theme_me)
    print(f"          {abu}THEME-ME {pxh} Infernal Reaper{netral}")
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
\033[91m                  ...:::::::::...
              ..:::\033[97maad8888888baa\033[91m:::..
           .::::\033[97md\033[91m:?\033[97m88888888888\033[91m?::\033[97m8b\033[91m::::.
         .:::\033[97md8888\033[91m:?\033[97m88888888\033[91m??\033[97ma888888b\033[91m:::.
       .:::\033[97md8888888a8888888aa8888888888b\033[91m:::.
      ::::\033[97mdP\033[91m::::::::\033[97m88888888888\033[91m::::::::\033[97mYb\033[91m::::
     ::::\033[97mdP\033[91m:::::::::\033[97mY888888888P\033[91m:::::::::\033[97mYb\033[91m::::
    ::::\033[97md8\033[91m:::::::::::\033[97mY8888888P\033[91m:::::::::::\033[97m8b\033[91m::::
   .::::\033[97m88\033[91m::::::::::::\033[97mY88888P\033[91m::::::::::::\033[97m88\033[91m::::.
   :::::\033[97mY8baaaaaaaaaa88P\033[91m:\033[97mT\033[91m:\033[97mY88aaaaaaaaaad8P\033[91m:::::
   :::::::\033[97mY88888888888P\033[91m::\033[97m|\033[91m::\033[97mY88888888888P\033[91m:::::::
   ::::::::::::::::\033[97m888\033[91m:::\033[97m|\033[91m:::\033[97m888\033[91m::::::::::::::::
   `:::::::::::::::\033[97m8888888888888b\033[91m::::::::::::::'
    :::::::::::::::\033[97m88888888888888\033[91m::::::::::::::
     :::::::::::::\033[97md88888888888888\033[91m:::::::::::::
      ::::::::::::\033[97m88\033[91m::\033[97m88\033[91m::\033[97m88\033[91m:::\033[97m88\033[91m::::::::::::
       `::::::::::\033[97m88\033[91m::\033[97m88\033[91m::\033[97m88\033[91m:::\033[97m88\033[91m::::::::::'
         `::::::::\033[97m88\033[91m::\033[97m88\033[91m::\033[97mP\033[91m::::\033[97m88\033[91m::::::::'
           `::::::\033[97m88\033[91m::\033[97m88\033[91m:::::::\033[97m88\033[91m::::::'
              ``:::::::::::::::::::''
                   ``:::::::::''     '''
run(logo)
print('''             \033[97m Username : \033[97;41m """+username+""" \033[0m''')
print('''           \033[97m Team :\033[90m """+team+""" \033[0m''') """
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
