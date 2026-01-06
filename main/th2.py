# -*- coding: utf-8 -*-
# Theme-Me/main/th2.py
# Credit by Zidan IDz
import os, sys, time, shutil
from support.echo import theme_me, abu, pxh, netral, putih, kuning, hijau, merah
from support.lib import load, message


def th2():
    os.system("clear")
    print(theme_me)
    print(f"          {abu}THEME-ME {pxh} Team Liquid {netral} ")
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
\033[90m                    ..:^^^^^^::.                    
              .::^:::^::...!~^^:^^^::.              
        .:::::^:::\033[37m7YPB?\033[90m...~\033[37m@@&BPY7!\033[90m^^^^^^::..       
    ^^^^^^~\033[37m!?J:\033[90m...\033[37mJ@@@#\033[90m:..\033[37m?@@@P!B@@&BPY?!\033[90m~^^:^^^.   
   .!....\033[37m7&@@@B!\033[90m...\033[37m?@@@Y\033[90m..\033[37m!&5\033[90m~. \033[37m5@@@@@@@@&#G5\033[90m~.!:   
   .!.....~\033[37m5&@@@5\033[90m^..!\033[37m&@G\033[90m^.:^..:\033[37mY@@@@@@@@@@@@@\033[90mJ !:   
   .!.~!:.  ^\033[37mJB@@&Y\033[90m:.^^.......:!\033[37mYB@@@@@@@@@@@\033[90mJ !:   
   .!.?\033[37m@#P?\033[90m~. .~\033[37mYBY:\033[90m..............^\033[37mJG&@@@@@@@\033[90mJ !:   
   .!.7\033[37m@@@@@#PJ\033[90m~.................\033[37m!!\033[90m..\033[37mP@@@@@@@\033[90mJ !:   
   .!.:^\033[37m!?YPG##7.\033[90m................\033[37m^7^\033[90m.\033[37m!&@@@@@@\033[90mJ !:   
   .!.::.....::............\033[37m^:\033[90m.........\033[37m!&@@@@@\033[90m?.!:   
   .!.!\033[37m&#####7\033[90m.............\033[37m?? \033[90m.........~\033[37m#@@@@\033[90m?.!.   
    !.~\033[37m&#BGPY\033[90m:.............\033[37m7@J\033[90m~:........^\033[37mB@@@\033[90m!.!.   
    !:.:.. .................\033[37mP@@&BJ\033[90m....:!::\033[37mB@&\033[90m^.!    
    ~^.:\033[37m!?5BP\033[90m................\033[37m7P&@@Y\033[90m.^7~^^\033[37mY&@G\033[90m.^~    
    .7.^\033[37m&@@@5\033[90m..................^\033[37m5@@Y7P@B#@@@\033[90m!.!.    
     ^~.\033[37m7G?\033[90m^.....................\033[37m!G@@@@@@@@?\033[90m.~^     
      ^~....\033[37m^?\033[90m.....................\033[37m?#@@@@B!\033[90m.~^      
       :~^\033[37m.:5@7\033[90m.....................:\033[37mY&G7\033[90m::~:       
         :~^\033[37m:^!\033[90m.......................\033[37m::\033[90m:^:         
           .:^^^:..................:^^^:.           
               :^^^^::........::^^^:.               
                   .:^^^^::^^^^:.                   
                        .::.                        '''
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
