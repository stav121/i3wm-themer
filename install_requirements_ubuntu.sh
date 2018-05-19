#!/usr/bin/env sh

### 201805 Script written and fully commented by James Shane ( github.com/jamesshane )

#refrsh apt
sudo apt update

#adobe-source-code-pro-fonts **
#added binutils,gcc,make,pkg-config,fakeroot for compilations, removed yaourt
sudo apt install git nitrogen rofi python-pip binutils gcc make pkg-config fakeroot fonts-font-awesome -y

#added PYTHONDONTWRITEBYTECODE to prevent __pycache__
export PYTHONDONTWRITEBYTECODE=1
sudo pip install -r requirements.txt

[ -d /usr/share/fonts/opentype ] || sudo mkdir /usr/share/fonts/opentype
sudo git clone https://github.com/adobe-fonts/source-code-pro.git /usr/share/fonts/opentype/scp
sudo fc-cache -f -v

##install yaourt by source
#git clone https://aur.archlinux.org/package-query.git
#cd package-query
#makepkg -si --noconfirm
#cd ..
#rm -fr package-query
#git clone https://aur.archlinux.org/yaourt.git
#cd yaourt
#makepkg -si --noconfirm
#cd ..
#rm -fr yaourt
##tmp dir for yaourt, /tmp may be too small
#mkdir $HOME/tmpyaourt
##went with ttf-nerd-fonts, other is outta date
#yaourt -S polybar-git ttf-nerd-fonts-symbols --noconfirm --tmp $HOME/tmpyaourt
#rmdir $HOME/tmpyaourt

#wget http://archive.getdeb.net/ubuntu/pool/apps/p/polybar/polybar_3.0.5-1\~getdeb1_amd64.deb
#sudo apt install -f ./polybar_3.0.5-1~getdeb1_amd64.deb
#rm -f polybar_3.0.5-1~getdeb1_amd64.deb

#git clone --branch 3.1.0 --recursive https://github.com/jaagr/polybar
#mkdir polybar/build
#cd polybar/build
#cmake ..
#sudo make install

#file didn't exist for me, so test and touch
if [ -e $HOME/.Xresources ]
then
	echo "... .Xresources found."
else
	touch $HOME/.Xresources
fi

#rework of user in config.yaml
cd src
rm -f config.yaml
cp defaults/config.yaml .
sed -i -e "s/USER/$USER/g" config.yaml

#file didn't excist for me, so test and touch
if [ -e $HOME/.config/polybar/config ]
then
        echo "... polybar/config found."
else
	mkdir $HOME/.config/polybar
        touch $HOME/.config/polybar/config
fi

#backup, configure and set theme to 000
cp -r ../scripts/* /home/$USER/.config/polybar/
mkdir $HOME/Backup
python i3wm-themer.py --config config.yaml --backup $HOME/Backup
python i3wm-themer.py --config config.yaml --install defaults/

echo ""
echo "Read the README.md"

