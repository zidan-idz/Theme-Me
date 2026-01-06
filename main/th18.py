# -*- coding: utf-8 -*-
# Theme-Me/main/th18.py
# Credit by Zidan IDz
import os, sys, time, shutil
from support.echo import theme_me, abu, pxh, netral, putih, kuning, hijau, merah
from support.lib import load, message

def th18():
    os.system("clear")
    print(theme_me)
    print(f"          {abu}THEME-ME {pxh} Iluminate {netral}")
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
\033[38;5;214m             .~?Y7               7Y7^.          
          .!J5G5^       :!.       ~PG5J~.       
         ~PGGGJ.        .!.        .YGGG5:      
         YGPG?    .:~7?JJJJJ?7~:.    JGPGJ      
     :? :PPG?  :!JPGP5YJJ?JJY5PGPJ!:  YGPP.:?.  
    :5Y ~GGY ^JPGP?~:.       .:~?5GPJ:.5GP: 5Y. 
   .YGJ !GP~?PGGJ:   Y55YYY55Y   .~YGP7!PG^ YGJ 
   7GGY ~GYYGPGY     ^~~5G5~~^      7PGY5G: 5GG!
   5PPP.:PPGPGG!    .7?^JGJ^?77~:.   !GGPP.:PPG5
   5GPG! YGG5YGY.   .PG!JGJ!GG55PPJ~  YGG? 7GPG5
   :YGGP.~GG?.JGP?~::PG!JGJ!GP: :!5GY:?GG^:PGGJ.
   ..!PG5^5G5  :?5PPPGG!JGJ!GP:    YG55GP^5G5~..
   :Y~.7P55GG7    .^~~!:YGJ:!!.    7GGPG55P!:!Y.
    ~GY~:!YPGG?.     !!!5G5!!!    .5GPGPJ!:!5G^ 
     ~PG5?~^75G5!.   ?JJJJJJJ?   ^YGP57^~?PGP^  
      :YGGG5J?5GGPJ!^.       .^!YGGP5JJPGGGJ.   
        ~?YY5555555PGP5YYYYY5PGP5555555YJ?~     
           :!????JY5J!5GGGGGY!Y5YJ????!.        
            .^7YP57^^JGPPYPPP?:^?5PY7^.         
                .  :Y55P? JP55J.  .    '''
run(logo)
print('''              \033[97m Username : \033[30;48;5;208m """+username+""" \033[0m''')
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
