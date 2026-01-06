# -*- coding: utf-8 -*-
# Theme-Me/main/th16.py
# Credit by Zidan IDz
import os, sys, time, shutil
from support.echo import theme_me, abu, pxh, netral, putih, kuning, hijau, merah
from support.lib import load, message


def th16():
    os.system("clear")
    print(theme_me)
    print(f"       {abu}THEME-ME {pxh} KeepBest Gaming {netral}")
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
\033[38;5;214m ^?YJ??JJ~\033[38;5;129m:^~~~~^.\033[38;5;214m:?YJJJJJJJJJYJ!.\033[38;5;129m.^~~~~^:\033[38;5;214m~JJ??JY?^
 \033[38;5;214m :75J^::: \033[38;5;129m.:^~~~~^:\033[38;5;214m!5PPPPPGGPJ^\033[38;5;129m:^~~~~^:\033[38;5;214m  :::^J57: 
  \033[38;5;214m  .!Y?:     \033[38;5;129m:^~~~~^:\033[38;5;214m....^5?:\033[38;5;129m.^~~~~^.    \033[38;5;214m :?Y!.   
     \033[38;5;214m  ~YJ^    \033[38;5;129m .^~~~~^ \033[38;5;214m?5P?\033[38;5;129m ^~~~~^.   \033[38;5;214m  ^JY~      
        \033[38;5;214m ~JY~   \033[38;5;129m.^~~~~^ \033[38;5;214m75P?\033[38;5;129m ^~~~~^.  \033[38;5;214m.~YJ~        
        \033[38;5;214m   ^7:\033[38;5;129m:^~~~^^:\033[38;5;214m:...^5?^\033[38;5;129m:^~~~~^.\033[38;5;214m:7^          
            \033[38;5;129m:^~~~^:\033[38;5;214m^?PPPPPGGGGY~\033[38;5;129m:^~~~~^.           
         \033[38;5;129m.:^~^^^:^\033[38;5;214mJY????????????J!\033[38;5;129m:^^^^~^:.        
         \033[38;5;129m .     \033[38;5;214m :?5J^        ~Y5!      \033[38;5;129m .         
               \033[38;5;214m    .755!.  .75Y~                   
                \033[38;5;214m     .!557?5J^                     
                    \033[38;5;214m    ~Y?:       '''
run(logo)
print('''              \033[97m Username : \033[38;5;15m\033[48;5;93m """+username+""" \033[0m''')
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
