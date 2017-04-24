#!/bin/sh
sed -i \
         -e 's/#2f2f38/rgb(0%,0%,0%)/g' \
         -e 's/#cfd2cf/rgb(100%,100%,100%)/g' \
    -e 's/#2f2f38/rgb(50%,0%,0%)/g' \
     -e 's/#688486/rgb(0%,50%,0%)/g' \
     -e 's/#2f2f38/rgb(50%,0%,50%)/g' \
     -e 's/#cfd2cf/rgb(0%,0%,50%)/g' \
	*.svg
