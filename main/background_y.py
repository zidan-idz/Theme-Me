# -*- coding: utf-8 -*-
# Theme-Me/main/background_y.py
# Credit by Zidan IDz
import os, sys, time, requests, shutil
from support.echo import theme_me, abu, pxh, netral, putih, hijau, merah
from support.lib import load, message


def background_y(y, maxx=10, delay=2):
    if y == "A":
        url = "https://raw.githubusercontent.com/zidan-idz/hozon/master/Backgrounds/Bright-Dark/colors.properties"
        font = " Bright-Dark "
    elif y == "B":
        url = "https://raw.githubusercontent.com/zidan-idz/hozon/master/Backgrounds/Chalk-Dark/colors.properties"
        font = " Chalk-Dark "
    elif y == "C":
        url = "https://raw.githubusercontent.com/zidan-idz/hozon/master/Backgrounds/Codeschool-Dark/colors.properties"
        font = " Codeschool-Dark "
    elif y == "D":
        url = "https://raw.githubusercontent.com/zidan-idz/hozon/master/Backgrounds/Colors-Dark/colors.properties"
        font = " Colors-Dark "
    elif y == "E":
        url = "https://raw.githubusercontent.com/zidan-idz/hozon/master/Backgrounds/Default-Dark/colors.properties"
        font = " Default-Dark "
    elif y == "F":
        url = "https://raw.githubusercontent.com/zidan-idz/hozon/master/Backgrounds/Eighties-Dark/colors.properties"
        font = " Eighties-Dark "
    elif y == "G":
        url = "https://raw.githubusercontent.com/zidan-idz/hozon/master/Backgrounds/Flat-Dark/colors.properties"
        font = " Embers-Dark "
    elif y == "H":
        url = "https://raw.githubusercontent.com/zidan-idz/hozon/master/Backgrounds/Flat-Dark/colors.properties"
        font = " Flat-Dark "
    elif y == "I":
        url = "https://raw.githubusercontent.com/zidan-idz/hozon/master/Backgrounds/Google-Dark/colors.properties"
        font = " Google-Dark "
    elif y == "J":
        url = "https://raw.githubusercontent.com/zidan-idz/hozon/master/Backgrounds/Grayscale-Dark/colors.properties"
        font = " Grayscale-Dark "
    else:
        return
    
    attempt = 0
    while attempt < maxx:
        try:
            echo = requests.get(url)
            echo.raise_for_status()

            os.system("clear")
            print(theme_me)
            print(f"        {abu}THEME-ME {pxh}{font}{netral} ")
            time.sleep(0.5)
            print(f"\n{putih}[{hijau}!{putih}] changing the Termux background ")
            load()
            with open("colors.properties", "wb") as file:
                file.write(echo.content)
            
            into = os.path.join(os.environ["HOME"], ".termux")
            os.makedirs(into, exist_ok=True)
            shutil.move("colors.properties", os.path.join(into, "colors.properties"))

            message("font")
            return
        except (requests.exceptions.RequestException, IOError) as e:
            print(f"{putih}[{merah}∆{putih}] Cannot connect to the internet {merah}!!")
            print(f"{putih}[{oren}∆{putih}] Make sure you are connected to the internet \n")
            os.system("pause")
            attempt += 1
            time.sleep(delay)

    print(f"\n {putih}failed to customize the Termux background {merah}!!")
    time.sleep(1)
    message("exit")


