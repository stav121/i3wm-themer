#!/bin/env bash

### Script written by Stavros Grigoriou ( github.com/unix121 )
### 20180505 Changes fully commented by James Shane ( github.com/jamesshane )
### 20180727 Python dependencies shifted to pacman by Graham Still ( github.com/adoxography )
### 20181009 Detection and Use of system AUR helpers by c0de ( github.com/alopexc0de )

#refrsh pacman
sudo pacman -Syy

#added binutils,gcc,make,pkg-config,fakeroot for compilations, removed yaourt
#added python-yaml, removed pip install
sudo pacman -S git nitrogen rofi python-pip ttf-font-awesome adobe-source-code-pro-fonts binutils gcc make pkg-config fakeroot python-yaml --noconfirm

# Look for and use common AUR helpers from https://wiki.archlinux.org/index.php/AUR_helpers#Pacman_wrappers
if [ -x "$(command -v yay)" ]; then
    yay -S polybar-git ttf-nerd-fonts-symbols
elif [ -x "$(command -v trizen)" ]; then
    trizen -S polybar-git ttf-nerd-fonts-symbols
elif [ -x "$(command -v pikaur)" ]; then
    pikaur -S polybar-git ttf-nerd-fonts-symbols
elif [ -x "$(command -v pakku)" ]; then
    pakku -S polybar-git ttf-nerd-fonts-symbols
elif [ -x "$(command -v aura)" ]; then
    aura -SA polybar-git ttf-nerd-fonts-symbols
elif [ -x "$(command -v pacaur)" ]; then
    pacaur -S polybar-git ttf-nerd-fonts-symbols
else
    echo "No common AUR Helpers found!"
    echo "This script requires an AUR Helper to install the following packages: polybar-git ttf-nerd-fonts-symbols"
    echo "Please install an AUR helper and try again"
    exit 1
fi


#file didn't exist for me, so test and touch
if [ -e $HOME/.Xresources ]
then
	echo "... .Xresources found."
else
	touch $HOME/.Xresources
fi

#file didn't exist for me, so test and touch
if [ -e $HOME/.config/nitrogen/bg-saved.cfg ]
then
	echo "... .bg-saved.cfg found."
else
	mkdir -p $HOME/.config/nitrogen
	touch $HOME/.config/nitrogen/bg-saved.cfg
fi

#file didn't exist for me, so test and touch
if [ -e $HOME/.config/polybar/config ]
then
        echo "... polybar/config found."
else
	mkdir -p $HOME/.config/polybar
        touch $HOME/.config/polybar/config
fi

#file didn't exist for me, so test and touch
if [ -e $HOME/.config/i3/config ]
then
        echo "... i3/config found."
else
        mkdir -p $HOME/.config/i3
        touch $HOME/.config/i3/config
fi

#rework of user in config.yaml
cd src
rm -f config.yaml
cp defaults/config.yaml .
sed -i -e "s/USER/$USER/g" config.yaml

#backup
mkdir $HOME/Backup
python i3wm-themer.py --config config.yaml --backup $HOME/Backup

#configure and set theme to 000
cp -r ../scripts/* /home/$USER/.config/polybar/
python i3wm-themer.py --config config.yaml --install defaults/

echo ""
echo "Read the README.md"

