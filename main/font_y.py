# -*- coding: utf-8 -*-
# Theme-Me/main/font_y.py
# Credit by Zidan IDz
import os, sys, time, requests, shutil
from support.echo import theme_me, abu, pxh, netral, putih, hijau, merah
from support.lib import load, message


def font_y(y, maxx=10, delay=2):
    if y == "A":
        url = "https://raw.githubusercontent.com/zidan-idz/hozon/master/Fonts/Anonymous-Pro/font.ttf"
        font = " Anonymous-Pro "
    elif y == "B":
        url = "https://raw.githubusercontent.com/zidan-idz/hozon/master/Fonts/Courier-Prime/font.ttf"
        font = " Courier-Prime "
    elif y == "C":
        url = "https://raw.githubusercontent.com/zidan-idz/hozon/master/Fonts/DejaVu/font.ttf"
        font = " DejaVu "
    elif y == "D":
        url = "https://raw.githubusercontent.com/zidan-idz/hozon/master/Fonts/Fantasque/font.ttf"
        font = " Fantasque "
    elif y == "E":
        url = "https://raw.githubusercontent.com/zidan-idz/hozon/master/Fonts/Fira/font.ttf"
        font = " Fira "
    elif y == "F":
        url = "https://raw.githubusercontent.com/zidan-idz/hozon/master/Fonts/FiraCode/font.ttf"
        font = " FIraCode "
    elif y == "G":
        url = "https://raw.githubusercontent.com/zidan-idz/hozon/master/Fonts/GNU-FreeFont/font.ttf"
        font = " GNU-FreeFont "
    elif y == "H":
        url = "https://raw.githubusercontent.com/zidan-idz/hozon/master/Fonts/Go/font.ttf"
        font = " Go "
    elif y == "I":
        url = "https://raw.githubusercontent.com/zidan-idz/hozon/master/Fonts/Hack/font.ttf"
        font = " Hack "
    elif y == "J":
        url = "https://raw.githubusercontent.com/zidan-idz/hozon/master/Fonts/Hermit/font.ttf"
        font = " Hermit "
    else:
        return
    
    attempt = 0
    while attempt < maxx:
        try:
            echo = requests.get(url)
            echo.raise_for_status()

            os.system("clear")
            print(theme_me)
            print(f"          {abu}THEME-ME {pxh}{font}{netral} ")
            time.sleep(0.5)
            print(f"\n{putih}[{hijau}!{putih}] changing the Termux font ")
            load()
            with open("font.ttf", "wb") as file:
                file.write(echo.content)
            
            into = os.path.join(os.environ["HOME"], ".termux")
            os.makedirs(into, exist_ok=True)
            shutil.move("font.ttf", os.path.join(into, "font.ttf"))

            message("font")
            return
        except (requests.exceptions.RequestException, IOError) as e:
            print(f"{putih}[{merah}∆{putih}] Cannot connect to the internet {merah}!!")
            print(f"{putih}[{oren}∆{putih}] Make sure you are connected to the internet \n")
            os.system("pause")
            attempt += 1
            time.sleep(delay)

    print(f"\n {putih}failed to customize the Termux font {merah}!!")
    time.sleep(1)
    message("exit")


