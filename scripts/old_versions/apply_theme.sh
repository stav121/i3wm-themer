#!/usr/bin/env bash

#
# Last update: 27 April 2017
#
# This script is no longer under development. Soon to be replaces with a
# better version that overwrites only what is needed in every configuration
# file.

# Written by : Stavros Grigoriou (unix121)
# GitHub : https://github.com/unix121
# E-mail : unix121@protonmail.com
# Simple script to apply a theme from the collection.

# Also contributing: rynnon
# GitHub: https://github.com/rynnon

# Simple function to display messages in a certain way
msg(){
  NORMAL="\e[1;0m"
  BOLD="\e[1;1m"
  COLORED="${BOLD}\e[1;32m"
  local option=$1
  local message=$2; shift

  if [ "$option" == "-n" ]
  then
    #Normal information display messages
    printf "\n${COLORED}${BOLD}[*]${NORMAL} ${message}"
  elif [ "$option" ==  "-e" ]
  then
    # Error messages
    printf "\n${COLORED}${BOLD}${message}"
  elif [  "$option" == "-i" ]
  then
    # Subprocess error messages
    printf "\n\t${COLORED}${BOLD}[*]${NORMAL} ${message}"
  elif [ "$option" == "-s" ]
  then
    # Subprocess success messages
    printf "\n\t${COLORED}${BOLD}[+]${NORMAL} ${message}"
  elif [ "$option" == "-f" ]
  then
    # Subprocess failure messages
    printf "\n\t${COLORED}${BOLD}[-]${NORMAL} ${message}"
  elif [ "$option" == "-p" ]
  then
    # Subprocess information message
    printf "\n\t${COLORED}${BOLD}[!]${NORMAL}${message}"
  elif [ "$option" == "-h" ]
  then
    # Help infomrmation messages
    printf "\n${NORMAL}${message}"
  elif [ "$option" == "-c" ]
  then
    # Caution message
    printf "\n${COLORED}${BOLD}[!]${NORMAL} ${message}"
  else
    # Wrong argument given error
    printf "\n${COLORED}${BOLD}Printing error...!{$NORMAL}"
  fi
}

# Exit function
ext(){
  echo
  msg -n "i3wmthemer finished\n\n"
  exit 0
}

# Simple initiation message
echo
msg -n "i3wmthemer script started"
echo

# Check if no arguments were given
if [ $# -eq 0 ]
then
  msg -e "Error: No arguments given"
  msg -e "try: ./apply_theme.sh -h for help"
  echo
  ext
fi

# Parse the command line arguments
OPTION=$1
THEME=$2

# Hide the system messages
exec 2> /dev/null

# Check the options given
if [ "$OPTION" == "-t" ]
then

  if [ -z "$THEME" ]
  then
    msg -e 'Error: No theme given'
    msg -e 'try: ./apply_theme.sh -h for help'
    ext
  fi

  msg -i 'Applying the theme..'

  # First we try to locate the theme
  if [ -d "../themes/$THEME" ]
  then
    msg -s 'Located the theme directory...'

    # First copy all the fonts into the right directory
    if [ -d "../.fonts" ]
    then
      if [ -d "/$HOME/.fonts/" ]
       then
        if cp -R ../.fonts/. ~/.fonts/
        then
          msg -s 'Fonts are set up successfully'
        else
          msg -f 'Failed to copy Fonts into ~/.fonts/ directory'
        fi
      else
        echo '  [*] Could not locate ~/.fonts/ directory, attempting to create it...'
        if mkdir ~/.fonts/
        then
          msg -s '~/.fonts/ directory created successfully'
          if cp -R ../.fonts/. ~/.fonts/
          then
            msg -s 'Fonts migration completed successfully'
          else
            msg -f 'Failed to create ~/.fonts/ directory'
          fi
        fi
      fi
    else
      msg -f '../.fonts/ directory not found'
   fi

    # Now that the file is located we copy everything into the right place

    # First we locate the i3wm configuration file in both the theme and
    # the user's configuration. There are 2 possible places for it to be
    # either "~/.i3/config" or ~/.config/i3/config
    if [ -e ~/.i3/config ]
    then
      if cp ../themes/$THEME/.i3/config ~/.i3/config
      then
        msg -s '.i3/config configuration file set up successfully'
      else
        msg -f 'Failed to apply changes to ~/.i3/config configuration file'
      fi
    elif [ -e ~/.config/i3/config ]
    then
      if cp ../themes/$THEME/.i3/config ~/.config/i3/config
      then
        msg -s '.config/i3/config configuration file set up successfully'
      else
        msg -f 'Failed to apply changes to ~/.config/i3/config configuration file'
      fi
    else
      # If we are here that means that the i3wm configuration file is not
      # located in either ~/.i3/config or ~/.config/i3/config
      msg -f 'Failed to locate i3wm configuraion file in your /home/ directory'
    fi

    if cp ../themes/$THEME/.config/compton.conf ~/.config/compton.conf
    then
      msg -s '.config/compton.conf configuration file set up successfully'
    else
      msg -f 'Failed to apply .config/compton.conf configuration file'
    fi

    if cp ../themes/$THEME/.resources/.Xresources ~/.Xresources
    then
      msg -s '.Xresources file set up successfully'
    else
      msg -f 'Failed to apply .Xresources configuration file'
    fi

    if cp ../themes/$THEME/.resources/.extend.Xresources ~/.extend.Xresources
    then
      msg -s '.extend.Xresources file set up successfully'
    else
      msg -f 'Failed to apply .extend.Xresources configuration file'
    fi

    if cp ../themes/$THEME/Other/.vimrc ~/.vimrc
    then
      msg -s '.vimrc configuration file set up successfully'
    else
      msg -f 'Failed to apply .vimrc configuraion file'
    fi

    if cp ../themes/$THEME/Other/.dmenurc ~/.dmenurc
    then
      msg -s '.dmenurc configuration file set up successfully'
    else
      msg -f 'Failed to apply .dmenurc configuration file'
    fi

    if xrdb ~/.Xresources
    then
      msg -s 'Terminal Theme applied successfully'
    else
      msg -f 'Failed to apply terminal theme'
    fi

    if cp ../themes/$THEME/.config/polybar/config ~/.config/polybar/config
    then
      msg -s '.config/polybar/config configuration file set up successfully'
    else
      msg -f 'Failed to apply ./config/polybar/config configuration file'
    fi


    if cp ../scripts/polybar/launch.sh ~/.config/polybar/launch.sh
    then
      chmod u+x ~/.config/polybar/launch.sh
      msg -s '.config/polybar/launch.sh script set up successfully'
    else
      msg -f 'Failed to apply .config/polybar/launch.sh script'
    fi

    if [ -x "~/.config/polybar/music.sh" ]
    then
      msg -p 'music.sh is already in the right folder'
    else
      if cp ../scripts/polybar/music.sh ~/.config/polybar/music.sh
      then
         chmod u+x ~/.config/polybar/music.sh
         msg -s '.config/polybar/music.sh script set up successfully'
      else
         msg -f 'Failed to apply .config/polybar/music.sh script'
      fi
    fi

    # Copying the GTK Theme into the right folder

    if [ -d "../themes/$THEME/.themes" ]
    then
      if [ -d "/$HOME/.themes/" ]
      then
        if cp -R  ../themes/$THEME/.themes/. ~/.themes/
        then
          msg -s  'GTK Theme migration completed successfully'
        else
          msg -f 'Failed to copy GTK Theme into ~/.themes/'
        fi
      else
        msg -p 'Could not locate ~/.themes/ directory, attempting to create it...'
         if mkdir ~/.themes/
         then
           msg -s '~/.themes/ directory created successfully'
           if cp -R ../themes/$THEME/.themes/. ~/.themes/
           then
             msg -s 'GTK Theme migration completed successfully'
           else
             msg -f 'Failed to copy GTK Theme into ~/.themes/ directory'
           fi
         else
           msg -f 'Failed to create ~/.themes/ directory'
         fi
      fi
    else
      msg -f 'This theme does not have a GTK Theme included'
    fi

    # Copying the Icons into the right folder
    if [ -d "../themes/$THEME/.icons" ]
    then
      if [ -d "/$HOME/.icons/" ]
      then
        if cp -R ../themes/$THEME/.icons/. ~/.icons/
        then
          msg -s 'Icon migration completed successfully'
        else
          msg -f 'Failed to copy Icons into ~/.icons/ directory'
        fi
      else
        msg -p 'Could not locate ~/.icons/ directory, attempting to create it...'
        if mkdir ~/.icons/
        then
          msg -s '~/.icons/ directory created successfully'
          if cp -R  ../themes/$THEME/.icons/. ~/.icons/
          then
            msg -s 'Icon migration completed successfully'
          else
            msg -f 'Failed to create ~/.icons/ directory'
          fi
        fi
      fi
    else
      msg -f 'This theme does not have Icon pack included'
    fi

#<---------------- Implementation by : Rynnon -------------------->

    if cp ../themes/$THEME/.xsettingsd ~/.xsettingsd
    then
      msg -s 'xsettingsd file set up successfully'
    else
      msg -f 'Failed to apply xsettingsd file'
    fi

    if xsettingsd &
    then
      msg -s 'Icons and GTK Themes applied successfully'
    else
      msg -f 'Failed to apply GTK theme and Icons'
    fi

##<---------------- End of implementation -------------------->

    if  nitrogen --set-scaled ../themes/$THEME/$THEME.png
    then
      msg -s 'Wallpaper set successfully'
    else
      msg -f 'Could not set wallpaper (Nitrogen missing?)'
    fi

    # Finally we restart i3wm
    i3-msg restart

    msg -c 'Use your Appearance Manager to set the Icons and GTK+ Themes'

  else

    msg -e 'ERROR: Could not locate the theme directory...'
  fi

elif [ "$OPTION" == "-b" ]
then
  # Backup mode. We locate the ../Backups/ directory
  # If it exists then we write into it, otherwise
  # we create it.
  msg -n "Backing up your files"

  if [ -d "../backups" ]
  then
    msg -s "Located backup directory"
  else
    mkdir ../backups
    msg -s  "Created backup directory"
  fi

#<------------------------- BACKUP ------------------------->

  if [ -z "$THEME" ]
  then
    msg -e 'Error: No backup name given'
    msg -e 'try: ./apply_theme.sh -h for help'
    ext
  fi

  if mkdir ../backups/$THEME
    then
    msg -s 'Folder created successfully'
  else
    msg -f 'Error, folder might already exist'
    ext
  fi

  mkdir ../backups/$THEME/.resources/

  if cp ~/.Xresources ../backups/$THEME/.resources/.Xresources
    then
    msg -s 'Saved ~/.Xresources successfully'
  else
    msg -f 'Failed to save ~/.Xresources'
  fi

  if cp ~/.extend.Xresources ../backups/$THEME/.resources/.extend.Xresources
    then
    msg -s 'Saved ~/.extend.Xresources successfully'
  else
    msg -f 'Failed to save ~/.extend.Xresources'
  fi

  mkdir ../backups/$THEME/.config/
  mkdir ../backups/$THEME/.config/polybar/

  if cp ~/.config/polybar/config ../backups/$THEME/.config/polybar/config
  then
    msg -s 'Saved ~/.config/polybar/config successfully'
  else
    msg -f 'Failed to save ~/.config/polybar/config'
  fi

  if cp ~/.config/polybar/launch.sh ../backups/$THEME/.config/polybar/launch.sh
  then
    msg -s 'Saved ~/.config/polybar/launch.sh successfully'
  else
    msg -f 'Failed to save ~/.config/polybar/config'
  fi

  if cp ~/.config/compton.conf ../backups/$THEME/.config/compton.conf
    then
    msg -s 'Saved ~/.config/compton.conf successfully'
  else
    msg -f 'msg -fFailed to save ~/.config/compton.conf'
  fi

  mkdir ../backups/$THEME/.i3/

  if cp ~/.i3/config ../backups/$THEME/.i3/config
    then
    msg -s 'Saved ~/.i3/config successfully'
  else
    msg -f 'Failed to save ~/.i3/config'
  fi

  mkdir ../backups/$THEME/Other/

  if cp ~/.dmenurc ../backups/$THEME/Other/.dmenurc
    then
    msg -s 'Saved ~/.dmenurc successfully'
  else
    msg -f 'Failed to save ~/.dmenurc'
  fi

  if cp ~/.vimrc ../backups/$THEME/Other/.vimrc
    then
    msg -s 'Saved ~/.vimrc successfully'
  else
    msg -f 'Failed to save ~/.vimrc'
  fi

  mkdir ../backups/$THEME/.config/dunst/

  if cp ~/.config/dunst/dunstrc ../backups/$THEME/.config/dunst/dunstrc
  then
    msg -s 'Saved ~/.config/dunst/dunstrc successfully'
  else
    msg -f 'Failed to save ~/.config/dunst/dunstrc'
  fi

  if cp ~/.xsettingsd ../backups/$THEME/.xsettingsd
  then
    msg -s 'Saved ~/.xsettingsd successfully'
  else
    msg -f 'Faled to save ~/.xsettingsd'
  fi

  msg -c "Your backup theme is now saved under ../backups/ directory\n"

  ext
#<------------------------END OF BACKUP -------------------->
elif [ "$OPTION" == "-h" ]
then
  # Simple help display
  msg -h "-t {THEME}                   ->  Set a theme (if it exists)."
  msg -h "        Example use: ./apply_theme.sh -t ThemeX"
  msg -h "-b {BACKUP_NAME}             ->  Create a backup of your files under"
  msg -h "                                  ../Backups/ directory"
  msg -h "        Example use: ./apply_theme.sh -b Backup123"
  msg -h "-t ../backups/{BACKUP_NAME}    -> Restore a backup (if it exists)"
  msg -h "        Example use: ./apply_theme.sh -t ../backups/Backup123\n"

else
  # If we are here that means that no right command argument was given.
  msg -e "Error: No arguments given"
  msg -e "try: ./apply_theme.sh -h for help"
  echo
  ext
fi

# Script ended, time to exit
ext
