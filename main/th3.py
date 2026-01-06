# -*- coding: utf-8 -*-
# Theme-Me/main/th3.py
# Credit by Zidan IDz
import os, sys, time, shutil
from support.echo import theme_me, abu, pxh, netral, putih, kuning, hijau, merah
from support.lib import load, message


def th3():
    os.system("clear")
    print(theme_me)
    print(f"             {abu}THEME-ME {pxh} Todak {netral} ")
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
\033[37m            YJ:                            
            ?@&J.                          
            !@@@#7                   .:^:  
            !@@@@@Y             .^7JYJ~:   
            7@@@@@@P.^~^.  :~?5B#BY!.      
            J@@@@@@@&@@@#PB&@@#J~!~        
            G@@@@@@@@@@@@@@@@5^.J@@#Y^     
          .5@@@@@@@@@@@@@@@P~7P&@@@@@@5:   
         :B@@@@@@@@@@@@@B5! :YB@@@@@@@@&7  
       :!#@@@@@@@@@@#&@G       ^Y&@@@@@@@? 
     ~5G@@@@@@@@@&&#:Y@B         ^B@@@@@@@~
   :7?^:#@@@@@@@P^#! .B#.         :&@@@@@@G
   ^.  ^@@@@@@@J :G   :G:          5@@@@@@@
       ^@@@@@@7  .!    ::          5@@@@@@@
        B@@@@Y.^                  ^&@@@@@@G
        7@@@@:7@!          .     ^#@@@@@@@~
         Y@@@~~@@P^   :!JYJ!.  ^5@@@@@@@@7 
          J@@#^!J7!?P##P?!~~7YB@@@@@@@@&!  
           ^P@@P5#@@B?~?G&@@@@@@@@@@@&5:   
             ~Y&@@@?^5&@@@@@@@@@@@@BJ:     
               ^@@&.?@@@@@@@@@&#P?^        
                J@@Y !7????7!~:.           
                 P@@!                      
                 .P@@!                     
                   J@@!                    
                    ~B@?                   
                      7B5.                 
                        7?.  '''
run(logo)
print('''              \033[97m Username : \033[30;47m """+username+""" \033[0m''')
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
