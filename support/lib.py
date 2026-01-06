# -*- coding: utf-8 -*-
# Theme-Me/support/lib.py
# Credit By Zidan IDz
import os, sys, time, requests, getpass
from .echo import theme_me, note
from .echo import merah, putih, pxh, hijau, oren, netral, kuning, abu


now = "v0.3.7"
url = "https://api.github.com/repos/Zidan-ID17/Theme-Me/releases"


def version(now):
    try:
        response = requests.get(url)
        response.raise_for_status()
        dat_up = response.json()
        new_ver = dat_up[0]["name"]
        if new_ver > now:
            print(f"{putih}[{oren}∆{putih}] new version is available, please update now {oren}!!")
            print(f"{putih}[{oren}∆{putih}] current version {now}, latest version {new_ver} \n")
            ask = input(f"{abu}do you want to read update help? (y/n) > ").lower()
            if ask == "y":
                os.system("nano update.txt")
            else:
                sys.exit()
        else:
            return
    except requests.exceptions.RequestException:
        print(f"{putih}[{merah}∆{putih}] cannot connect to the internet {merah}!!")
        print(f"{putih}[{oren}∆{putih}] make sure you are connected to the internet")
        sys.exit()


def runntxt(x):
    for i in x + "\n":
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.1 / 100)


def entry():
    while True:
        time.sleep(1)
        os.system("clear")
        runntxt(theme_me)
        print(f"\n{pxh}for tokens, you can check YouTube Zeyshyy {netral}")
        code = getpass.getpass(f"{putih}enter token {hijau}>{putih} ").lower()
        if code == "emotebangga":
            time.sleep(1)
            print(f"\n{putih}login successfully [{hijau}✓{putih}]")
            time.sleep(1)
            break
        else:
            time.sleep(1)
            print(f"\n{putih}login failed [{merah}X{putih}]")
            time.sleep(1)
            ask = input(f"\n{putih}want to try again? {kuning}(y/n) > ").lower()
            if ask == "n":
                message("exit")



def load(duration=7, interval=0.1):
    animation_chars = "[★*******]","[*★******]","[**★*****]","[***★****]","[****★***]","[*****★**]","[******★*]","[*******★]"
    num_frames = int(duration / interval)
    for i in range(num_frames):
        sys.stdout.write(f"\r{putih}[{hijau}∆{putih}] please wait{hijau} {animation_chars[i % len(animation_chars)]}")
        sys.stdout.flush()
        time.sleep(interval)


def message(x):
    if x == "font":
        os.system("clear")
        os.system("termux-reload-settings")
        print(theme_me)
        time.sleep(0.5)
        print(f"\n\n{putih}[{hijau}✓{putih}] successfully changed Termux font")
        time.sleep(1)
        print(f"{abu}[{hijau}~{abu}] open a new session to see changes")
        time.sleep(0.5)
        print(f"\n\n{abu}[{kuning}*{abu}] if You want to exit press CTRL + Z")
        time.sleep(1)
        input(f"\n{abu} press enter to return ..")
        return
    elif x == "background":
        os.system("clear")
        os.system("termux-reload-settings")
        print(theme_me)
        time.sleep(0.5)
        print(f"\n\n{putih}[{hijau}✓{putih}] successfully changed Termux background")
        time.sleep(1)
        print(f"{abu}[{hijau}~{abu}] open a new session to see changes")
        time.sleep(0.5)
        print(f"\n\n{abu}[{kuning}*{abu}] if You want to exit press CTRL + Z")
        time.sleep(1)
        input(f"\n{abu} press enter to continue ..")
        return
    elif x == "theme":
        os.system("clear")
        os.system("termux-reload-settings")
        print(theme_me)
        time.sleep(0.5)
        print(f"\n\n{putih}[{hijau}✓{putih}] successfully changed Termux theme")
        time.sleep(1)
        print(f"{abu}[{hijau}~{abu}] open a new session to see changes")
        time.sleep(0.5)
        print(f"\n\n{abu}[{kuning}*{abu}] if You want to exit press CTRL + Z")
        time.sleep(1)
        input(f"\n{abu} press enter to return ..")
        return
    elif x == "wrong":
        print(f"\n{putih}please input the correct choice [{merah}!{putih}]")
        time.sleep(1.5)
        return
    elif x == "exit":
        time.sleep(1)
        print(f"\n{putih}thank you for using Theme-Me")
        time.sleep(1)
        print(f"\n{putih}bye bye {netral}👋\n")
        time.sleep(1)
        sys.exit()
    elif x == "about":
        os.system("clear")
        print(note)
        input(f"\n{abu} press enter to return ..")
        return
    if x == "coming":
        os.system("clear")
        print(theme_me)
        time.sleep(0.5)
        print(f"\n\n{putih}[{hijau}✓{putih}] sorry, this funnction has not been added")
        time.sleep(1)
        print(f"{abu}[{hijau}~{abu}] this function will be added in the next update")
        time.sleep(1)
        input(f"\n{abu} press enter to return ..")
        return
    else:
        return
