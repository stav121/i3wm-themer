#!/bin/sh
sed -i \
         -e 's/#1e272b/rgb(0%,0%,0%)/g' \
         -e 's/#ead49b/rgb(100%,100%,100%)/g' \
    -e 's/#1e272b/rgb(50%,0%,0%)/g' \
     -e 's/#1e272b/rgb(0%,50%,0%)/g' \
     -e 's/#1e272b/rgb(50%,0%,50%)/g' \
     -e 's/#ead49b/rgb(0%,0%,50%)/g' \
	*.svg
