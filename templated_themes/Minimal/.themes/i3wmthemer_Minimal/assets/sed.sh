#!/bin/sh
sed -i \
         -e 's/#1c1c22/rgb(0%,0%,0%)/g' \
         -e 's/#b0aba8/rgb(100%,100%,100%)/g' \
    -e 's/#1c1c22/rgb(50%,0%,0%)/g' \
     -e 's/#3e646f/rgb(0%,50%,0%)/g' \
     -e 's/#1c1c22/rgb(50%,0%,50%)/g' \
     -e 's/#b0aba8/rgb(0%,0%,50%)/g' \
	*.svg
