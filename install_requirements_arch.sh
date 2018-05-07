#!/bin/env sh

### Script written by Stavros Grigoriou ( github.com/unix121 )
### 20180505 Changes fully commented by James Shane ( github.com/jamesshane )


#added binutils,gcc,make,pkg-config,fakeroot for compilations, removed yaourt
sudo pacman -S git nitrogen rofi python-pip ttf-font-awesome adobe-source-code-pro-fonts binutils gcc make pkg-config fakeroot

#added PYTHONDONTWRITEBYTECODE to prevent __pycache__
export PYTHONDONTWRITEBYTECODE=1
sudo pip install -r requirements.txt

#install yaourt by source
git clone https://aur.archlinux.org/package-query.git
cd package-query
makepkg -si --noconfirm
cd ..
rm -fr package-query
git clone https://aur.archlinux.org/yaourt.git
cd yaourt
makepkg -si --noconfirm
cd ..
rm -fr yaourt
yaourt -S polybar-git --noconfirm

#directory may not be needed, but it makes a cleaner install, went with nerd-fonts-git, other is outta date
sudo mkdir /usr/share/fonts/OTF
#git clone https://aur.archlinux.org/nerd-fonts-git.git
#cd nerd-fonts-git
#makepkg -si --noconfirm
#cd ..
#rm -fr nerd-fonts-git

#install -Dm644 /usr/share/doc/polybar/config $HOME/.config/polybar/config

#file didn't exist for me, so test and touch
if [ -e $HOME/.Xresources ]
then
	echo "... .Xresources found."
else
	touch $HOME/.Xresources
fi

