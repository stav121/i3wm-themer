#!/bin/env sh
cd src
python i3wm-themer.py --config config.yaml --load themes/$1.json
