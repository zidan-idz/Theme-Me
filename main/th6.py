# -*- coding: utf-8 -*-
# Theme-Me/main/th6.py
# Credit by Zidan IDz
import os, sys, time, shutil
from support.echo import theme_me, abu, pxh, netral, putih, kuning, hijau, merah
from support.lib import load, message


def th6():
    os.system("clear")
    print(theme_me)
    print(f"              {abu}THEME-ME {pxh} Onic {netral}")
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
\033[93m                     :^^^^^^:..  ..                 
                     ^JPBBGGGGP5JJP5?~.             
                .:^~!77JGBBBPY5GBBBBBBGJ^           
              ~YPBBBBP5YYYYYY?:.~JGBGGGBB5~         
               :~?5GBP?^.    ..   .?GGYY5PGP55555PJ.
        .^!?Y5PGPP55YYJJ7:     .7Y55GBGGPPPBBBBBBY. 
    .^7YPGBBPJ7~^:.        .^!?YPBBBBGBBBBBBGPP5!   
   .7YPGBBBB5?~:         ^?PBBBBBBGGGGGGBBBB57:     
       .:~!J5BBBPY!.    :~?PBBGGGGGGGGGBBY7^.       
      .:!?Y5PPY7~:.  :75GBBBGGGGGGGGGGGBJ           
   :7YPBBBGJ~.       :7PBBGGGGGGGGGGGGB5            
 ^JPGGGGGGGP55Y!   ^JPBBGGGGGGGGGGGGGBP.            
 ......:7PBBGJ: :?PBBBBBGGGGGGGGGGGGBG:             
      .7JJJ7. ~5BBP55PGBBBGGGBBBBGGBG~              
            !PB5!^~7. .~JGBBBBYJYBBB!               
          JGBB? ^PBJ     ~GBBJ  JBB?                
          ^~^^  :~~:      ^~~.  ^^^   '''
run(logo)
print('''              \033[97m Username : \033[30;43m """+username+""" \033[0m''')
print('''            \033[97m Team :\033[90m """+team+""" \033[0m''') """
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
