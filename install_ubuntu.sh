#!/bin/bash

### 20180515 Script written and fully commented by James Shane ( github.com/jamesshane )
### 20200408 Script refactored by Johannes Pertl ( github.com/JohannesPertl )


function preparation() {
  # Look for env command and link if not found to help make scripts uniform
  if [ -e /bin/env ]; then
    echo "... /bin/env found."
  else
    sudo ln -s /usr/bin/env /bin/env
  fi
}

function install_required_packages() {
    # Refresh apt
    sudo apt update
    sudo apt install libcanberra-gtk-module \
      libcanberra-gtk3-module \
      libjsoncpp-dev build-essential \
      libxcb-composite0-dev \
      libxcb1-dev \
      libxcb-keysyms1-dev \
      libpango1.0-dev \
      libxcb-util0-dev \
      libxcb-icccm4-dev \
      libyajl-dev \
      libstartup-notification0-dev \
      libxcb-randr0-dev \
      libev-dev \
      libxcb-cursor-dev \
      libxcb-xinerama0-dev \
      libxcb-xkb-dev \
      libxkbcommon-dev \
      libxkbcommon-x11-dev \
      autoconf \
      xutils-dev \
      dh-autoreconf \
      unzip \
      git \
      x11-xserver-utils \
      compton \
      nitrogen \
      rofi \
      binutils \
      gcc \
      build-essential \
      cmake \
      pkg-config \
      fakeroot \
      python3 \
      python3-xcbgen \
      xcb-proto \
      libxcb-ewmh-dev \
      wireless-tools \
      libiw-dev \
      libasound2-dev \
      libpulse-dev \
      libcurl4-openssl-dev \
      libmpdclient-dev \
      pavucontrol \
      python3-pip \
      rxvt-unicode \
      compton \
      ninja-build \
      meson \
      python3-sphinx \
      libxcb-xrm-dev \
      libuv1-dev \
      -y

}

function install_xcb() {
  git clone --recursive https://github.com/Airblader/xcb-util-xrm.git
  # shellcheck disable=SC2164
  cd xcb-util-xrm/
  ./autogen.sh
  make
  sudo make install
  # shellcheck disable=SC2103
  cd ..
  rm -fr xcb-util-xrm
}


function refresh_shared_libraries() {
    #cat > /etc/ld.so.conf.d/i3.conf
    #/usr/local/lib/

    sudo ldconfig
    sudo ldconfig -p
}

function install_i3_gaps() {

    git clone https://www.github.com/Airblader/i3.git i3-gaps
    # shellcheck disable=SC2164
    cd i3-gaps
    rm -Rf build/
    mkdir build
    # shellcheck disable=SC2164
    cd build/
    meson ..
    sudo ninja install
    # which i3
    # ls -l /usr/bin/i3
    cd ../..
    rm -fr i3-gaps

}

function install_fonts_awesome() {
    # Added PYTHONDONTWRITEBYTECODE to prevent __pycache__
    export PYTHONDONTWRITEBYTECODE=1
    sudo -H pip3 install -r requirements.txt

    [ -d /usr/share/fonts/opentype ] || sudo mkdir /usr/share/fonts/opentype
    sudo git clone https://github.com/adobe-fonts/source-code-pro.git /usr/share/fonts/opentype/scp
    mkdir fonts
    # shellcheck disable=SC2164
    cd fonts
    wget https://use.fontawesome.com/releases/v5.0.13/fontawesome-free-5.0.13.zip
    unzip fontawesome-free-5.0.13.zip
    # shellcheck disable=SC2164
    cd fontawesome-free-5.0.13
    sudo cp use-on-desktop/* /usr/share/fonts
    sudo fc-cache -f -v
    cd ../..
    rm -fr fonts
}

function install_polybar() {
    git clone https://github.com/jaagr/polybar.git
    # shellcheck disable=SC2164
    cd polybar
    # shellcheck disable=SC2164
    env USE_GCC=ON ENABLE_I3=ON ENABLE_ALSA=ON ENABLE_PULSEAUDIO=ON ENABLE_NETWORK=ON ENABLE_MPD=ON ENABLE_CURL=ON ENABLE_IPC_MSG=ON INSTALL=OFF INSTALL_CONF=OFF ./build.sh -f
    # shellcheck disable=SC2164
    cd build
    sudo make install
    make userconfig
    cd ../..
    rm -fr polybar
}

function create_config_files() {
    # File didn't exist for me, so test and touch
    if [ -e "$HOME"/.Xresources ]; then
      echo "... .Xresources found."
    else
      touch "$HOME"/.Xresources
    fi

    # File didn't exist for me, so test and touch
    if [ -e "$HOME"/.config/nitrogen/bg-saved.cfg ]; then
      echo "... .bg-saved.cfg found."
    else
      mkdir "$HOME"/.config/nitrogen
      touch "$HOME"/.config/nitrogen/bg-saved.cfg
    fi

    # File didn't excist for me, so test and touch
    if [ -e "$HOME"/.config/polybar/config ]; then
      echo "... polybar/config found."
    else
      mkdir "$HOME"/.config/polybar
      touch "$HOME"/.config/polybar/config
    fi

    # File didn't excist for me, so test and touch
    if [ -e "$HOME"/.config/i3/config ]; then
      echo "... i3/config found."
    else
      mkdir "$HOME"/.config/i3
      touch "$HOME"/.config/i3/config
    fi

    # Compton config file doesn't come by default
    if [ -e "$HOME"/.config/compton.conf ]; then
        echo "... compton.conf found"
    else
        cp "/usr/share/doc/compton/examples/compton.sample.conf" "$HOME/.config/compton.conf"
    fi

}

function apply_default_theme() {
  # Rework of user in config.yaml
  rm -f config.yaml
  cp defaults/config.yaml .
  sed -i -e "s/USER/$USER/g" config.yaml

  # Backup
  mkdir "$HOME"/Backup
  python3 i3wm-themer.py --config config.yaml --backup "$HOME"/Backup

  # Configure and set theme to default
  cp -r scripts/* /home/"$USER"/.config/polybar/
  python3 i3wm-themer.py --config config.yaml --install defaults/

  echo ""
  echo "Read the README.md"
}

preparation
install_required_packages
install_xcb
refresh_shared_libraries
install_i3_gaps
install_fonts_awesome
install_polybar
create_config_files
apply_default_theme
