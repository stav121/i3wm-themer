#!/usr/bin/env bash

# Written by : unix121
# GitHub : https://github.com/unix121
# Website : unix121.github.io
# E-mail : unix121@protonmail.com
# Simple script to apply a theme from my collection

# Also contributing: rynnon
# GitHub: https://github.com/rynnon

if [ $# -eq 0 ]
then
  echo "Error: No arguements given"
  exit
fi

OPTION=$1

THEME=$2

exec 2> /dev/null

if [ "$OPTION" == "-t" ]
then

  if [ -z "$THEME" ]
  then
    echo '[-] Error: No theme given'
    exit
  fi

  echo '[*] Applying the theme..'

  # First we try to locate the theme
  if [ -d "../$THEME" ]
  then
    echo '  [+] Located the theme directory...'

    # First copy all the fonts into the right directory
    if [ -d "../.fonts" ]
    then
      if [ -d "/$HOME/.fonts/" ]
       then
        if cp -R ../.fonts/. ~/.fonts/
        then
          echo '  [+] Fonts are set up successfully'
        else
          echo '  [-] Failed to copy Fonts into ~/.fonts/ directory'
        fi
      else
        echo '  [*] Could not locate ~/.fonts/ directory, attemptint to create it...'
        if mkdir ~/.fonts/
        then
          echo ' [+] ~/.fonts/ directory created successfully'
          if cp -R ../.fonts/. ~/.fonts/
          then
            echo '  [+] Fonts migration completed successfully'
          else
            echo '  [-] Failed to create ~/.fonts/ directory'
          fi
        fi
      fi
    else
      echo '  [-] ../.fonts/ directory not found'
   fi

    # Now that the file is located we copy everything into the right place

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
      echo '  [+] .config/polybar/config configuration file set up successfully'
    else
      echo '  [-] Failed to apply ./config/polybar/config configuration file'
    fi


    if cp ../scripts/polybar/launch.sh ~/.config/polybar/launch.sh
    then
      chmod u+x ~/.config/polybar/launch.sh
      echo '  [+] .config/polybar/launch.sh script set up successfully'
    else
      echo '  [-] Failed to apply .config/polybar/launch.sh script'
    fi

    if [ -x "~/.config/polybar/music.sh" ]
    then
      echo '    [*] music.sh is already in the right folder'
    else
      if cp ../scripts/polybar/music.sh ~/.config/polybar/music.sh
      then
         chmod u+x ~/.config/polybar/music.sh
         echo '  [+] .config/polybar/music.sh script set up successfully'
      else
         echo '  [-] Failed to apply .config/polybar/music.sh script'
      fi
    fi

    # Copying the GTK Theme into the right folder

    if [ -d "../$THEME/.themes" ]
    then
      if [ -d "/$HOME/.themes/" ]
      then
        if cp -R  ../$THEME/.themes/. ~/.themes/
        then
          echo  '  [+] GTK Theme migration completed successfully'
        else
          echo '   [-] Failed to copy GTK Theme into ~/.themes/'
        fi
      else
        echo '  [*] Could not locate ~/.themes/ directory, attempting to create it...'
         if mkdir ~/.themes/
         then
           echo '  [+] ~/.themes/ directory created successfully'
           if cp -R ../$THEME/.themes/. ~/.themes/
           then
             echo '  [+] GTK Theme migration completed successfully'
           else
             echo '  [-] Failed to copy GTK Theme into ~/.themes/ directory'
           fi
         else
           echo '  [-] Failed to create ~/.themes/ directory'
         fi
      fi
    else
      echo '  [-] This theme does not have a GTK Theme included'
    fi

    # Copying the Icons into the right folder
    if [ -d "../$THEME/.icons" ]
    then
      if [ -d "/$HOME/.icons/" ]
      then
        if cp -R ../$THEME/.icons/. ~/.icons/
        then
          echo '  [+] Icon migration completed successfully'
        else
          echo '  [-] Failed to copy Icons into ~/.icons/ directory'
        fi
      else
        echo '  [*] Could not locate ~/.icons/ directory, attempting to create it...'
        if mkdir ~/.icons/
        then
          echo '  [+] ~/.icons/ directory created successfully'
          if cp -R  ../$THEME/.icons/. ~/.icons/
          then
            echo '  [+] Icon migration completed successfully'
          else
            echo '  [-] Failed to create ~/.icons/ directory'
          fi
        fi
      fi
    else
      echo '  [-] This theme does not have Icon pack included'
    fi

    # Implementation by : Rynnon

    if cp ../$THEME/.xsettingsd ~/.xsettingsd
    then
      echo '  [+] xsettingsd file set up successfully'
    else
      echo '  [-] Failed to apply xsettingsd file'
    fi

    if xsettingsd &
    then
      echo '  [+] Icons and GTK Themes applied successfully'
    else
      echo '  [-] Failed to apply GTK theme'
    fi

    # End of implementation

    if  nitrogen --set-scaled ../$THEME/$THEME.png
    then
      echo '  [+] Wallpaper set successfully'
    else
      echo '  [-] Could not set wallpaper (Nitrogen missing?)'
    fi

    # Finally we restart i3wm
    i3-msg restart

    echo '[!] Use your Appearance Manager to set the Icons and GTK+ Themes'

  else

    echo '[-] ERROR: Could not locate the theme directory...'
  fi
elif [ "$OPTION" == "-b" ]
then
  echo "[+] Backing up your files"

  if [ -d "../Backups" ]
  then
    echo "  [+] Located backup Directory "
  else
    mkdir ../Backups
    echo  "  [+] Created backup directory"
  fi

  exec ./theme_backup.sh $THEME

fi

echo '[*] Script exiting...'


exit
