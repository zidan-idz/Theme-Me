# -*- coding: utf-8 -*-
# Theme-Me/main/font_x.py
# Credit by Zidan IDz
import os, sys, time, requests, shutil
from support.echo import theme_me, abu, pxh, netral, putih, hijau, merah
from support.lib import load, message


def font_x(y, maxx=10, delay=2):
    if y == "A":
        url = "https://raw.githubusercontent.com/zidan-idz/hozon/master/Fonts/Inconsolata/font.ttf"
        font = " Inconsolata "
    elif y == "B":
        url = "https://raw.githubusercontent.com/zidan-idz/hozon/master/Fonts/Iosevka/font.ttf"
        font = " Iosevka "
    elif y == "C":
        url = "https://raw.githubusercontent.com/zidan-idz/hozon/master/Fonts/LiberationMono/font.ttf"
        font = " LiberationMono "
    elif y == "D":
        url = "https://raw.githubusercontent.com/zidan-idz/hozon/master/Fonts/Meslo/font.ttf"
        font = " Meslo "
    elif y == "E":
        url = "https://raw.githubusercontent.com/zidan-idz/hozon/master/Fonts/Monofur/font.ttf"
        font = " Monofur "
    elif y == "F":
        url = "https://raw.githubusercontent.com/zidan-idz/hozon/master/Fonts/Monoid/font.ttf"
        font = " Monoid "
    elif y == "G":
        url = "https://raw.githubusercontent.com/zidan-idz/hozon/master/Fonts/OpenDyslexic/font.ttf"
        font = " OpenDyslexic "
    elif y == "H":
        url = "https://raw.githubusercontent.com/zidan-idz/hozon/master/Fonts/Roboto/font.ttf"
        font = " Roboto "
    elif y == "I":
        url = "https://raw.githubusercontent.com/zidan-idz/hozon/master/Fonts/Source-Code-Pro/font.ttf"
        font = " Source-Code-Pro "
    elif y == "J":
        url = "https://raw.githubusercontent.com/zidan-idz/hozon/master/Fonts/Ubuntu/font.ttf"
        font = " Ubuntu "
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


