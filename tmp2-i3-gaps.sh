#!/bin/bash
# created for installing i3-gaps over Linux Mint 18.1

# run with sudo

#-------------------------------------------------------------------------------

export DEBIAN_FRONTEND=noninteractive
apt-get update -q
apt-get upgrade -q -y

# depencies of i3-gaps
add-apt-repository ppa:aguignard/ppa -y
apt-get update -q
apt-get install -q -y   -o Dpkg::Options::="--force-confdef" \
                        -o Dpkg::Options::="--force-confold" \
git automake libtool libxcb-xrm0 libxcb-xrm-dev

apt-get install -q -y   -o Dpkg::Options::="--force-confdef" \
                        -o Dpkg::Options::="--force-confold" \
libxcb1-dev libxcb-keysyms1-dev libpango1.0-dev libxcb-util0-dev \
libxcb-icccm4-dev libyajl-dev libstartup-notification0-dev libxcb-randr0-dev \
libev-dev libxcb-cursor-dev libxcb-xinerama0-dev libxcb-xkb-dev \
libxkbcommon-dev libxkbcommon-x11-dev autoconf


# install i3-gaps from source

# clone the repository
git clone https://www.github.com/Airblader/i3 i3-gaps
cd i3-gaps
# compile & install
autoreconf --force --install
rm -rf build/
mkdir -p build && cd build/
# Disabling sanitizers is important for release versions!
# The prefix and sysconfdir are, obviously, dependent on the distribution.
../configure --prefix=/usr --sysconfdir=/etc --disable-sanitizers
make
make install

# install misc. i3 packages
apt-get install -q -y   -o Dpkg::Options::="--force-confdef" \
                        -o Dpkg::Options::="--force-confold" \
i3lock i3status dmenu dunst

# basic apps
add-apt-repository ppa:dawidd0811/neofetch -y
apt-get update -q
apt-get install -q -y   -o Dpkg::Options::="--force-confdef" \
                        -o Dpkg::Options::="--force-confold" \
neofetch xsettingsd feh htop mlocate rxvt-unicode ranger w3m-img mpd ncmpcpp

