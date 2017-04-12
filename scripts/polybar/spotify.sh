#!/bin/bash

exec 2>/dev/null

if [ "$(playerctl status)" = "Playing" ]; then
  title=`exec playerctl metadata xesam:title`
  artist=`exec playerctl metadata xesam:artist`
  echo "[$artist] $title"
else
  echo "No song currently playing"
fi
