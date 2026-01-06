# -*- coding: utf-8 -*-
# Theme-Me/main/th4.py
# Credit by Zidan IDz
import os, sys, time, shutil
from support.echo import theme_me, abu, pxh, netral, putih, kuning, hijau, merah
from support.lib import load, message


def th4():
    os.system("clear")
    print(theme_me)
    print(f"          {abu}THEME-ME {pxh} Wings Gaming {netral} ")
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
\033[97m?!:                                              :!?
~YJ?!^.                                      .:!?JY!
 ^?YY5YJ7~.                ..            .^!?YYYYJ^ 
   ~?5PGBBBPY7^.       ^YPGG57:     .^7JPGBBGG5J~.  
    .:~?5B#@@@@#57.   !BBBBB5.   .!5B@@@@&BPJ!^.    
    ^?YYJJJYP&@@@@B7  ?BGPPGP.  !B@@@@&G5J?JJYJ^    
      :7YPGGB&&&&###? .Y57?5!  7###&&@&BBGPY7^      
         :7???J##BGGP. ..  .  .5GGB##Y???7:         
          :!YPB###BGP. .^!!:. .5GB###BGY7:          
              .^!?JY57J555555J7YYY?!^:              
                   ^G#BGGPPGGB#G:                   
                  !#@&#BBGGBB#&@#!                  
                 ~@@#!5&####&J?&@@!                 
                 .JP: B@&PP@@5 ~GJ:                 
                     ^&@&:^&@#.                     
                      ~G5  5P^             '''
run(logo)
print('''               \033[97m Username : \033[30;47m """+username+""" \033[0m''')
print('''             \033[97m Team :\033[90m """+team+""" \033[0m''') """
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
