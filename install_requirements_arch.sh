#!/bin/env sh

### Script written by Stavros Grigoriou ( github.com/unix121 )

sudo pacman -S git nitrogen rofi python-pip ttf-font-awesome adobe-source-code-pro-fonts 
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
yaourt -S polybar-git nerd-fonts-complete --noconfirm
