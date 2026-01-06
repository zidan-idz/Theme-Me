# -*- coding: utf-8 -*-
# Theme-Me/main/th17.py
# Credit by Zidan IDz
import os, sys, time, shutil
from support.echo import theme_me, abu, pxh, netral, putih, kuning, hijau, merah
from support.lib import load, message


def th17():
    os.system("clear")
    print(theme_me)
    print(f"       {abu}THEME-ME {pxh} Invictus Gaming {netral}")
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
\033[97m                     .:^^^^^:.                   
               .!5B&&&&#B####&&&B5!.             
            ^P&@&5!:.. ~PBBP! .:!5#@&P^          
          ?&@B~..~YB&!G@@@@@@G.GJ^. !B@&J        
        ?@@Y..?#@@@@@!&@@@@@@&^@@@@P  .Y@@?      
      .#@G .P@@@@@@@@@G#&&&&#P@@@@@@Y    P@&.    
     :@@! 7@@@@@@@@&GJJ?JYY?7?5&@@@@G  .? ~@@:   
    .@@~ 5@@@@@@@&J?G&@@@@@@@@G^:B@@^  ^@P ^@@.  
    G@5 ?@@@@@@@B?&@@@@@@@@@@@@@^ ?J   #@@J J@B  
   .@@. @@@@@@@&YP?!P@@@@@@@@@@@B    .#@@@@. @@. 
   ~@& ^@@@@@@@P     @@@@@@@@@@@?  .5@@@@@@~ #@! 
   ~@& ^@@@@@@@G    Y@@@@@@@@@@P  5@@@@@@@@! #@! 
   .@@. @@@@@@@@~  ~@@@@@@@@@@G. !@@@@@@@@@. @@. 
    G@5 Y@@@@@@@@~ @@@@@@@@@@@?&:7@@@@@@@@P J@B  
    .@@~ B@@@@@@@^5@@@@@@@@@@@@@7:@@@@@@@B ^@@.  
     :@@! Y@@@@@@.@@@@@@@@@@@@@@G.@@@@@@5 ~@@^   
      .#@P :B@@@@.&@@@@@@@@@@@@@P7@@@@#: P@&.    
        7@@Y.:5&@B?@@@@@@@@@@@@@J@@@P:.J@@?      
          ?&@B~.^J??#@@@@@@@@@&PPJ^.~G@&?        
            ^5&@#57^..:~!!~^^::^!5#@&P^          
               .!5B&&&##BBB##&&&B5!.             
                     .:^^^^^:.                   '''
run(logo)
print('''              \033[97m Username : \033[30;47m """+username+""" \033[0m''')
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
