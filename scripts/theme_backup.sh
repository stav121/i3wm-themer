#!/bin/bash

# Written by Stauros Grigoriou. April 05, 2017.
# A simple backup script to save my current i3 configuration

# First we hide all the error messages
exec 2>/dev/null

# Now we check if the directory that we are going to save the
# File already exists, if it exists we prompt a message and exit

# The name of the folder must be given at the arguments
FILE=$1

echo '[*] i3 backup script will now save your current configuration'

if mkdir $HOME/Documents/Themes/$FILE 
  then
  echo '  [+] Folder created successfully'
else
  echo '  [-] Error, folder might already exist. Exiting...'
  exit
fi

mkdir $HOME/Documents/Themes/$FILE/.resources

if cp ~/.Xresources $HOME/Documents/Themes/$FILE/.resources/.Xresources
  then
  echo '  [+] Saved ~/.Xresources successfully'
else
  echo '  [-] Failed to save ~/.Xresources'
fi

if cp ~/.extend.Xresources $HOME/Documents/Themes/$FILE/.resources/.extend.Xresources
  then
  echo '  [+] Saved ~/.extend.Xresources successfully'
else
  echo '  [-] Failed to save ~/.extend.Xresources'
fi

mkdir $HOME/Documents/Themes/$FILE/.config/
mkdir $HOME/Documents/Themes/$FILE/.config/polybar/

if cp ~/.config/polybar/config $HOME/Documents/Themes/$FILE/.config/polybar/config
  then
  echo '  [+] Saved ~/.config/polybar/config successfully'
else
  echo '  [-] Failed to save ~/.config/polybar/config'
fi

if cp ~/.config/compton.conf $HOME/Documents/Themes/$FILE/.config/compton.conf
  then
  echo '  [+] Saved ~/.config/compton.conf successfully'
else
  echo '  [-] Failed to save ~/.config/compton.conf'
fi

mkdir $HOME/Documents/Themes/$FILE/.i3/

if cp ~/.i3/config $HOME/Documents/Themes/$FILE/.i3/config
  then
  echo '  [+] Saved ~/.i3/config successfully'
else
  echo '  [-] Failed to save ~/.i3/config'
fi

mkdir $HOME/Documents/Themes/$FILE/Other/

if cp ~/.dmenurc $HOME/Documents/Themes/$FILE/Other/.dmenurc
  then
  echo '  [+] Saved ~/.dmenurc successfully'
else
  echo '  [-] Failed to save ~/.dmenurc'
fi

if cp ~/.vimrc $HOME/Documents/Themes/$FILE/Other/.vimrc
  then
  echo '  [+] Saved ~/.vimrc successfully'
else
  echo '  [-] Failed to save ~/.vimrc'
fi

echo '[*] i3 backup script will now exit...'
