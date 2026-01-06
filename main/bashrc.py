# -*- coding: utf-8 -*-
# Theme-Me/main/bashrc.py
# Credit by Zidan IDz
import os, sys, time,shutil
from support.echo import putih, kuning, merah, abu, hijau, lst_clr

def bashrc():
    print(lst_clr)
    time.sleep(0.3)
    print(f"{putih}({kuning}*{putih}) {abu}HTML color code for the cursor color to be displayed")
    color = input(f"\n{putih}enter coler code {hijau}>{putih} ")
    while not color.strip() or '"' in color or "'" in color:
        print(f"{abu}({merah}X{abu}) must not be blank or contain quotation marks {merah}!!")
        color = input(f"\n{putih}enter coler code {hijau}>{putih} ")
        continue
    time.sleep(0.3)
    file = "bash.bashrc"
    fill = """#Created with THEME-ME, coded by Zidan IDz
#Subscribe YouTube Zeyshyy
#
clear
# Command history tweaks:
# - Append history instead of overwriting
#   when shell exits.
# - When using history substitution, do not
#   exec command immediately.
# - Do not save to history commands starting
#   with space.
# - Do not save duplicated commands.
shopt -s histappend
python $HOME/../usr/etc/theme.py
shopt -s histverify
export HISTCONTROL=ignoreboth

# Default command line prompt.
PROMPT_DIRTRIM=2
PS1='\\n\[\e[97;100m\] \[\e[91m\]●\[\e[93m\]●\[\e[92m\]●\e[30m\]\w\[\e[0m\] \[\e[92m\]'
# Handles nonexistent commands.
# If user has entered command which invokes non-available
# utility, command-not-found will give a package suggestions.
if [ -x /data/data/com.termux/files/usr/libexec/termux/command-not-found ]; then
    command_not_found_handle() {
        /data/data/com.termux/files/usr/libexec/termux/command-not-found '$1'
    }
fi

[ -r /data/data/com.termux/files/usr/share/bash-completion/bash_completion ] && . /data/data/com.termux/files/usr/share/bash-completion/bash_completion
echo -e '\e[4 q'
echo -ne '\033]12;"""+color+"""\007'   """
    with open(file, "w") as x:
        x.write(fill)
    of = "bash.bashrc"
    into = os.path.join(os.environ["HOME"], "..", "usr", "etc", "bash.bashrc")
    if os.path.exists(into):
        os.remove(into)

    while True:
        try:
            shutil.move(of, into)
            break
        except Exception as e:
            with open(file, "w") as x:
                x.write(fill)
            time.sleep(1)






