#!/bin/env sh
# Terminate already running bar instances
# If all your bars have ipc enabled, you can use 
polybar-msg cmd quit

# https://github.com/polybar/polybar/issues/763#issuecomment-331604987
# if type "xrandr"; then
#   for m in $(xrandr --query | grep "connected" | cut -d" " -f1); do
#       MONITOR=$m polybar --reload main --config=~/.config/polybar/config.ini &
#   done
# else
#   polybar --reload main --config=~/.config/polybar/config.ini &
# fi
if [ -z "$(pgrep -x polybar)" ]; then
    BAR="main"
    for m in $(polybar --list-monitors | cut -d":" -f1); do
        MONITOR=$m polybar --reload $BAR --config=~/.config/polybar/config.ini &
        sleep 1
    done
else
    polybar-msg cmd restart
fi
# Launch bar1 and bar2
#polybar main --config=~/.config/polybar/config.ini

echo "Bars launched..."

#pkill polybar

#sleep 1;

#polybar i3wmthemer_bar &
