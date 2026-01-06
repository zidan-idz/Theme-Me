# -*- coding: utf-8 -*-
# Theme-Me/main/th12.py
# Credit by Zidan IDz
import os, sys, time, shutil
from support.echo import theme_me, abu, pxh, netral, putih, kuning, hijau, merah
from support.lib import load, message


def th12():
    os.system("clear")
    print(theme_me)
    print(f"           {abu}THEME-ME {pxh} Bigetron {netral}")
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
\033[31m                      ......                  
       !!       .^!7??????????7!^.       7!   
      ~P?    :!?J7~^..      ..^~7J?!:    JP^  
      7P?  .?J!:                  :!J?.  ?P!  
      JP7.!^Y                       .Y^7:?P?  
     .YPY5Y^5.                      :5^Y5YPY  
     :55PPY^5?       .:^~~^:.       ?5^5P555. 
    .JP555P^JP!   .!J55YJJY55J!.   7P?~P5555?.
    !P5555PJ^PP7  !PP!.    .!PP! .7P5^JP5555P!
    5555555P!!PPY~.JP?      ?PJ:~YPP!7P5555555
    555555555!!555J?5PY!^^!YP5?J555!!P55555555
    !PP555555P?^..:^?5PPPPPP5?^:..^?P555555PP!
    .?J5P55555P5~    ?PPPPPP?    !5P55555P5J?.
       ~5P55PPY77J?~.!JYYYYJ!.~??!?5P555P5~   
       ^5PPY7!J5PPP5YJJJJJJY5PPP5?~?5PP5~    
         :?77YPP5555JJJJJJJJJJ5555P5?!??:     
           :?5PP55P7~JJJJJJJJ~7P55PP5?.       
             .!?5PJ^5PPPPPPPP5^YP5J!.         
                .^.~?JYYYYYYJ?~:^.            
                       ....              '''
        
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
