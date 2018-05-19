
sudo apt-get install libxcb1-dev libxcb-keysyms1-dev libpango1.0-dev libxcb-util0-dev libxcb-icccm4-dev libyajl-dev libstartup-notification0-dev libxcb-randr0-dev libev-dev libxcb-cursor-dev libxcb-xinerama0-dev libxcb-xkb-dev libxkbcommon-dev libxkbcommon-x11-dev autoconf xutils-dev dh-autoreconf

git clone --recursive https://github.com/Airblader/xcb-util-xrm.git
cd xcb-util-xrm/
./autogen.sh
make
sudo make install

cat > /etc/ld.so.conf.d/i3.conf 
/usr/local/lib/

sudo ldconfig
sudo ldconfig -p

git clone https://www.github.com/Airblader/i3 i3-gaps
cd i3-gaps
autoreconf --force --install
rm -Rf build/
mkdir build
cd build/
 ../configure --prefix=/usr --sysconfdir=/etc
 make
 sudo make install
 which i3
 ls -l /usr/bin/i3

