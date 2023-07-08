#!/bin/env bash

### Script written by Stavros Grigoriou ( github.com/unix121 )
### 20180505 Changes fully commented by James Shane ( github.com/jamesshane )
### 20180727 Python dependencies shifted to pacman by Graham Still ( github.com/adoxography )
### 20181009 Detection and Use of system AUR helpers by c0de ( github.com/alopexc0de )
### 20230707 Remove detection and use of AUR for poly, as it has moved into extra repo for Arch by Elijah Hopp

#refrsh pacman
sudo pacman -Syy

# Added binutils,gcc,make,pkg-config,fakeroot for compilations, removed yaourt
# Added python-yaml, removed pip install
# Added polybar, removed repeated "git" in package list.
sudo pacman -S git nitrogen rofi polybar python-pip ttf-font-awesome adobe-source-code-pro-fonts binutils gcc make pkg-config fakeroot python-yaml ttf-nerd-fonts-symbols --noconfirm

# File didn't exist for me, so test and touch
if [ -e "$HOME"/.Xresources ]; then
  echo "... .Xresources found."
else
  touch "$HOME"/.Xresources
fi

# File didn't exist for me, so test and touch
if [ -e "$HOME"/.config/nitrogen/bg-saved.cfg ]; then
  echo "... .bg-saved.cfg found."
else
  mkdir -p "$HOME"/.config/nitrogen
  touch "$HOME"/.config/nitrogen/bg-saved.cfg
fi

# File didn't exist for me, so test and touch
if [ -e "$HOME"/.config/polybar/config ]; then
  echo "... polybar/config found."
else
  mkdir -p "$HOME"/.config/polybar
  touch "$HOME"/.config/polybar/config
fi

# File didn't exist for me, so test and touch
if [ -e "$HOME"/.config/i3/config ]; then
  echo "... i3/config found."
else
  mkdir -p "$HOME"/.config/i3
  touch "$HOME"/.config/i3/config
fi

# Rework of user in config.yaml
rm -f config.yaml
cp defaults/config.yaml .
sed -i -e "s/USER/$USER/g" config.yaml

# Backup
mkdir "$HOME"/Backup
python3 i3wm-themer.py --config config.yaml --backup "$HOME"/Backup

# Configure and set theme to 000
cp -r scripts/* /home/"$USER"/.config/polybar/
python3 i3wm-themer.py --config config.yaml --install defaults/

echo ""
echo "Read the README.md"
