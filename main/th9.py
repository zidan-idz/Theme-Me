# -*- coding: utf-8 -*-
# Theme-Me/main/th9.py
# Credit by Zidan IDz
import os, sys, time, shutil
from support.echo import theme_me, abu, pxh, netral, putih, kuning, hijau, merah
from support.lib import load, message


def th9():
    os.system("clear")
    print(theme_me)
    print(f"           {abu}THEME-ME {pxh} MegaStars {netral}")
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
\033[31m
      ~.                                  .~        
     .&&G?:                            :?G&&.       
     .#&&&&BY~.                    .~YB&&&&#.       
     .#&&######5!.              :7P#######&#.       
     .####G?G#####G?^       .^JG#####G?G##&#.       
     .####Y  .!5B####BY~..!5B####B5!.  Y####.       
     .####5      ^JG####BB###BPJ^.     Y####.       
     .####5  ^5!.   :75BBBB##G!.       Y####.       
     .####5  ~###P?:   .~YGBB##BP7:    Y####.       
     .####Y  :PB####GY~.   :?PB####B^  Y####.       
     .####G~.  .~YB####B57:   .!5B##!  Y####.       
      5######P7.   :?P#####GJ^    ^Y^  Y####.       
        ^JG#####GJ^   .!5B####B5!.     ?##&#.       
      7:   .7P#####B5!.   ^JG#####G?^   .~5B.       
     .&&BJ^   .~YB#####G?:   :7P#####B5~.           
     .#&&&&#5!.   :?P######5^   .~5##&&&&GJ.        
      .~5B&&&&#G?:   .~5BB5!.   :?G#&&&&B5!.        
          :?G&&&&&B5~.      .~5B&&&&#G?:            
             .!5#&&&&#P7.:7P#&&&&#5!.               
                .^JG##########GJ^                   
                    .!5B##B5!.                      
                       .~~.         
'''
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
