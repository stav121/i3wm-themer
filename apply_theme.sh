# April 05, 2017
# Written by Stavros Grigoriou
# Simple script to apply a theme from my collection

THEME=$1

echo '[*] Applying the theme..'

if [ -d "../$THEME" ]
then
  echo '  [+] Located the theme directory...'

  if cp ../$THEME/.i3/config ~/.i3/config
  then
    echo '  [+] .i3/config configuration file set up successfully'
  else
    echo '  [-] Failed to apply .i3/config configuration file'
  fi

  if cp ../$THEME/.config/compton.conf ~/.config/compton.conf
  then
    echo '  [+] .config/compton.conf configuration file set up successfully'
  else
    echo '  [-] Failed to apply .config/compton.conf configuration file'
  fi

  if cp ../$THEME/.resources/.Xresources ~/.Xresources
  then
    echo '  [+] .Xresources file set up successfully'
  else
    echo '  [-] Failed to apply .Xresources configuration file'
  fi

  if cp ../$THEME/.resources/.extend.Xresources ~/.extend.Xresources
  then
    echo '  [+] .extend.Xresources file set up successfully'
  else
    echo '  [-] Failed to apply .extend.Xresources configuration file'
  fi

  if cp ../$THEME/Other/.vimrc ~/.vimrc
  then
    echo '  [+] .vimrc configuration file set up successfully'
  else
    echo '  [-] Failed to apply .vimrc configuraion file'
  fi

  if cp ../$THEME/Other/.dmenurc ~/.dmenurc
  then
    echo '  [+] .dmenurc configuration file set up successfully'
  else
    echo '  [-] Failed to apply .dmenurc configuration file'
  fi

  if xrdb ~/.Xresources
  then
    echo '  [+] Terminal Theme applied successfully'
  else
    echo '  [-] Failed to apply terminal theme'
  fi

  if cp ../$THEME/.config/polybar/config ~/.config/polybar/config
  then 
    echo ' [+] .config/polybar/config configuration file set up successfully'
  else
    echo ' [-] Failed to apply ./config/polybar/config configuration file'
  fi

  if cp ../scripts/launch.sh ~/.config/polybar/launch.sh
  then
    chmod u+x ~/.config/polybar/launch.sh
    echo '  [+] .config/polybar/launch.sh script set up successfully'
  else
    echo '  [-] Failed to apply .config/polybar/launch.sh script'
  fi

  if cp ../scripts/music.sh ~/.config/polybar/music.sh
  then
    chmod u+x ~/.config/polybar/music.sh
    echo '  [+] .config/polybar/music.sh script set up successfully'
  else
    echo '  [-] Failed to apply .config/polybar/music.sh script'
  fi

else
  echo '[-] ERROR: Could not locate the theme directory...'
fi

echo '[*] Script exiting...'
exit
