#!/bin/env sh
### Script written by James Shane ( github.com/jamesshane )

#python3 i3wm-themer.py --config config.yaml -i ./defaults/ --load themes/"$1".json
python3 i3wm-themer.py --load $1
