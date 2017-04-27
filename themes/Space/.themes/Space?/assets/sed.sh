#!/bin/sh
sed -i \
         -e 's/#1f1f1f/rgb(0%,0%,0%)/g' \
         -e 's/#c6c6c6/rgb(100%,100%,100%)/g' \
    -e 's/#1f1f1f/rgb(50%,0%,0%)/g' \
     -e 's/#81a2be/rgb(0%,50%,0%)/g' \
     -e 's/#1f1f1f/rgb(50%,0%,50%)/g' \
     -e 's/#c6c6c6/rgb(0%,0%,50%)/g' \
	*.svg
