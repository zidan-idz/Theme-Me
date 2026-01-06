# -*- coding: utf-8 -*-
# Theme-Me/main/background_x.py
# Credit by Zidan IDz
import os, sys, time, requests, shutil
from support.echo import theme_me, abu, pxh, netral, putih, hijau, merah
from support.lib import load, message


def background_x(y, maxx=10, delay=2):
    if y == "A":
        url = "https://raw.githubusercontent.com/zidan-idz/hozon/master/Backgrounds/3024-Dark/colors.properties"
        font = " 3024-Dark "
    elif y == "B":
        url = "https://raw.githubusercontent.com/zidan-idz/hozon/master/Backgrounds/Ashes-Dark/colors.properties"
        font = " Ashes-Dark "
    elif y == "C":
        url = "https://raw.githubusercontent.com/zidan-idz/hozon/master/Backgrounds/Atelierdune-Dark/colors.properties"
        font = " Atelierdune-Dark "
    elif y == "D":
        url = "https://raw.githubusercontent.com/zidan-idz/hozon/master/Backgrounds/Atelierforest-Dark/colors.properties"
        font = " Atelierforest-Dark "
    elif y == "E":
        url = "https://raw.githubusercontent.com/zidan-idz/hozon/master/Backgrounds/Atelierhealt-Dark/colors.properties"
        font = " Atelierhealt-Dark "
    elif y == "F":
        url = "https://raw.githubusercontent.com/zidan-idz/hozon/master/Backgrounds/Atelierlikeside-Dark/colors.properties"
        font = " Atelierlikeside-Dark "
    elif y == "G":
        url = "https://raw.githubusercontent.com/zidan-idz/hozon/master/Backgrounds/Flat-Dark/colors.properties"
        font = " Embers-Dark "
    elif y == "H":
        url = "https://raw.githubusercontent.com/zidan-idz/hozon/master/Backgrounds/Atelierseaside-Dark/colors.properties"
        font = " Atelierseaside-Dark "
    elif y == "I":
        url = "https://raw.githubusercontent.com/zidan-idz/hozon/master/Backgrounds/Bespin-Dark/colors.properties"
        font = " Bespin-Dark "
    elif y == "J":
        url = "https://raw.githubusercontent.com/zidan-idz/hozon/master/Backgrounds/Brewer-Dark/colors.properties"
        font = " Brewer-Dark "
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


