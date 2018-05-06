#!/bin/env sh

### Script written by Stavros Grigoriou ( github.com/unix121 )
### Changes fully commented by James Shane ( github.com/jamesshane )

sudo pacman -S git nitrogen rofi python-pip ttf-font-awesome adobe-source-code-pro-fonts 
#added -B to prevent __pycache__
sudo pip install -B -r requirements.txt

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

#directory may not be needed, but it makes a cleaner install
sudo mkdir /usr/share/fonts/OTF
git clone https://aur.archlinux.org/nerd-fonts-complete.git
cd nerd-fonts-complete
makepkg -si --noconfirm
cd ..
rm -fr nerd-fonts-complete

install -Dm644 /usr/share/doc/polybar/config $HOME/.config/polybar/config

#file didn't excist for me, so test and touch
if [ -e $HOME/.Xresources ]
then
	echo ".Xresources found."
else
	touch $HOME/.Xresources
fi

#rework of user in config.yaml
cd src
rm -f config.yaml
cp defaults/config.yaml .
sed -i -e "s/USER/$USER/g" config.yaml

#backup, confire and set theme to 000
#cp -r ../scripts/* /home/$USER/.config/polybar/
mkdir $HOME/Backup
python i3wm-themer.py --config config.yaml --backup $HOME/Backup
python i3wm-themer.py --config config.yaml --install defaults/
python i3wm-themer.py --config config.yaml --load themes/000.json
