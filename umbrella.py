# -*- coding: utf-8 -*-
# Theme-Me/umbrella.py
# Credit by Zidan IDz
import os, sys, time
from support import *
from main import *

def main():
    while True:
        os.system("clear")
        runntxt(theme_me)
        print(m_pg)
        select = input(f"{putih}[select options]{hijau} > ").lower()
        if select == "theme":
            theme1()
        elif select == "font":
            font1()
        elif select == "background":
            background1()
        elif select == "restore":
            message("coming")
        elif select == "feedback":
            os.system("xdg-open https://forms.gle/GNXkzSNYLQWh1N5q7")
            input(f"\n{abu} press enter to return ..")
        elif select == "about":
            message("about")
        elif select == "exit":
            message("exit")
        else:
            message("wrong")


def theme1():
    while True:
        os.system("clear")
        runntxt(theme_me)
        print(th1_pg)
        select = input(f"{putih}select options {hijau}>{putih} ")
        time.sleep(1)
        if select == "1" or select == "01":
            os.system("clear")
            print(theme_me)
            print(f"          {abu}THEME-ME {pxh} Infernal Reaper {netral}")
            bashrc()
            theme_y("A")
        elif select == "2" or select == "02":
            os.system("clear")
            print(theme_me)
            print(f"          {abu}THEME-ME {pxh} Team Liquid {netral}")
            bashrc()
            theme_y("B")
        elif select == "3" or select == "03":
            os.system("clear")
            print(theme_me)
            print(f"\            {abu}THEME-ME {pxh} Todak {netral}")
            bashrc()
            theme_y("C")
        elif select == "4" or select == "04":
            os.system("clear")
            print(theme_me)
            print(f"          {abu}THEME-ME {pxh} Wings Gaming {netral}")
            bashrc()
            theme_y("D")
        elif select == "5" or select == "05":
            os.system("clear")
            print(theme_me)
            print(f"            {abu}THEME-ME {pxh} Blacklist {netral}")
            bashrc()
            theme_y("E")
        elif select == "6" or select == "06":
            os.system("clear")
            print(theme_me)
            print(f"              {abu}THEME-ME {pxh} Onic {netral}")
            bashrc()
            theme_y("F")
        elif select == "7" or select == "07":
            os.system("clear")
            print(theme_me)
            print(f"             {abu}THEME-ME {pxh} Fnatic {netral}")
            bashrc()
            theme_y("G")
        elif select == "8" or select == "08":
            os.system("clear")
            print(theme_me)
            print(f"            {abu}THEME-ME {pxh} Faze Clan {netral}")
            bashrc()
            theme_y("H")
        elif select == "9" or select == "09":
            os.system("clear")
            print(theme_me)
            print(f"           {abu}THEME-ME {pxh} MegaStars {netral}")
            bashrc()
            theme_y("I")
        elif select == "10":
            os.system("clear")
            print(theme_me)
            print(f"         {abu}THEME-ME {pxh} 19esports {netral}")
            bashrc()
            theme_y("J")
        elif select == "77":
            theme2()
        elif select == "99":
            main()
        elif select == "00":
            message("exit")
        else:
            message("wrong")


def theme2():
    while True:
        os.system("clear")
        runntxt(theme_me)
        print(th2_pg)
        select = input(f"{putih}select options {hijau}>{putih} ")
        time.sleep(1)
        if select == "11":
            os.system("clear")
            print(theme_me)
            print(f"        {abu}THEME-ME {pxh} Ethereal Cranium {netral}")
            bashrc()
            theme_x("A")
        elif select == "12":
            os.system("clear")
            print(theme_me)
            print(f"           {abu}THEME-ME {pxh} Bigetron {netral}")
            bashrc()
            theme_x("B")
        elif select == "13":
            os.system("clear")
            print(theme_me)
            print(f"        {abu}THEME-ME {pxh} Evil Geniuses {netral}")
            bashrc()
            theme_x("C")
        elif select == "14":
            os.system("clear")
            print(theme_me)
            print(f"         {abu}THEME-ME {pxh} Team Spirit {netral}")
            bashrc()
            theme_x("D")
        elif select == "15":
            os.system("clear")
            print(theme_me)
            print(f"           {abu}THEME-ME {pxh} Cloud 9 {netral}")
            bashrc()
            theme_x("E")
        elif select == "16":
            os.system("clear")
            print(theme_me)
            print(f"       {abu}THEME-ME {pxh} KeepBest Gaming {netral}")
            bashrc()
            theme_x("F")
        elif select == "17":
            os.system("clear")
            print(theme_me)
            print(f"       {abu}THEME-ME {pxh} Invictus Gaming {netral}")
            bashrc()
            theme_x("G")
        elif select == "18":
            os.system("clear")
            print(theme_me)
            print(f"\n          {abu}THEME-ME {pxh} Iluminate {netral}")
            bashrc()
            theme_x("H")
        elif select == "19":
            os.system("clear")
            print(theme_me)
            print(f"         {abu}THEME-ME {pxh} 496 Gaming {netral}")
            bashrc()
            theme_x("I")
        elif select == "20":
            os.system("clear")
            print(theme_me)
            print(f"         {abu}THEME-ME {pxh} Team SoloMid {netral}")
            bashrc()
            theme_x("J")
        elif select == "88":
            theme1()
        elif select == "99":
            main()
        elif select == "00":
            message("exit")
        else:
            message("wrong")
            

def background1():
    while True:
        os.system("clear")
        runntxt(theme_me)
        print(bkg1_pg)
        select = input(f"{putih}select options {hijau}>{putih} ")
        time.sleep(1)
        if select == "1" or select == "01":
            background_x("A")
        elif select == "2" or select == "02":
            background_x("B")
        elif select == "3" or select == "03":
            background_x("C")
        elif select == "4" or select == "04":
            background_x("D")
        elif select == "5" or select == "05":
            background_x("E")
        elif select == "6" or select == "06":
            background_x("F")
        elif select == "7" or select == "07":
            background_x("G")
        elif select == "8" or select == "08":
            background_x("H")
        elif select == "9" or select == "09":
            background_x("I")
        elif select == "10":
            background_x("J")
        elif select == "77":
            background2()
        elif select == "99":
            main()
        elif select == "00":
            message("exit")
        else:
            message("wrong")
            	

def background2():
    while True:
        os.system("clear")
        runntxt(theme_me)
        print(bkg2_pg)
        select = input(f"{putih}select options {hijau}>{putih} ")
        time.sleep(1)
        if select == "11":
            background_y("A")
        elif select == "12":
            background_y("B")
        elif select == "13":
            background_y("C")
        elif select == "14":
            background_y("D")
        elif select == "15":
            background_y("E")
        elif select == "16":
            background_y("F")
        elif select == "17":
            background_y("G")
        elif select == "18":
            background_y("H")
        elif select == "19":
            background_y("I")
        elif select == "20":
            background_y("J")
        elif select == "88":
            background1()
        elif select == "99":
            main()
        elif select == "00":
            message("exit")
        else:
            message("wrong")


def font1():
    while True:
        os.system("clear")
        runntxt(theme_me)
        print(fnt1_pg)
        select = input(f"{putih}select options {hijau}>{putih} ")
        time.sleep(1)
        if select == "1" or select == "01":
            font_y("A")
        elif select == "2" or select == "02":
            font_y("B")
        elif select == "3" or select == "03":
            font_y("C")
        elif select == "4" or select == "04":
            font_y("D")
        elif select == "5" or select == "05":
            font_y("E")
        elif select == "6" or select == "06":
            font_y("F")
        elif select == "7" or select == "07":
            font_y("G")
        elif select == "8" or select == "08":
            font_y("H")
        elif select == "9" or select == "09":
            font_y("I")
        elif select == "10":
            font_y("J")
        elif select == "77":
            font2()
        elif select == "99":
            main()
        elif select == "00":
            message("exit")
        else:
            message("wrong")


def font2():
    while True:
        os.system("clear")
        runntxt(theme_me)
        print(fnt2_pg)
        select = input(f"{putih}select options {hijau}>{putih} ")
        time.sleep(1)
        if select == "11":
            font_x("A")
        elif select == "12":
            font_x("B")
        elif select == "13":
            font_x("C")
        elif select == "14":
            font_x("D")
        elif select == "15":
            font_x("E")
        elif select == "16":
            font_x("F")
        elif select == "17":
            font_x("G")
        elif select == "18":
            font_x("H")
        elif select == "19":
            font_x("I")
        elif select == "20":
            font_x("J")
        elif select == "88":
            font1()
        elif select == "99":
            main()
        elif select == "00":
            message("exit")
        else:
            message("wrong")



if __name__ == "__main__":
    now = "v0.3.7"
    version(now)
    entry()
    main()
