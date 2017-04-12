<h1>Themes</h1>

My collection of themes for i3. 

<h1>What you might need</h1>

- i3-wm in any Linux distro you prefer
- Polybar (for most of the themes)
- You might need to copy the files located in "scripts" folder into "~/.config/polybar/"
  to make the Polybar configuration work properly on most themes.
- To recreate some of the GTK themes (for now) you can download <a href="https://github.com/actionless/oomox">oomox</a> and use the 
  colors located in "/{Theme_name}/.resources/.extend.Xresources" and recreate them.
- A couple of fonts might be required. <a href="https://github.com/chrissimpkins/Hack">Hack Font</a> and <a href="http://fontawesome.io/">Font Awesome</a>.
- Firefox Themes can be installed using the "Stylish" extension

<h1>Installation</h1> 

- <h3>Manual Way</h3> To copy the basic configuration of a theme follow those steps:

  - git clone https://github.com/unix121/Themes
  - cd {THEME_YOU_WANT_TO_APPLY}
  - cp .i3/config ~/.i3/config (or ~/.config/i3/config depending on your configuration file location)
  - cp .config/compton.conf ~/.config/compton.conf
  - cp .config/polybar/confing ~/.config/polybar/config
  - cp ../scripts/polybar/launch.sh ~/.config/polybar/launch.sh
  - cp ../scripts/polybar/music.sh ~/.config/polybar/music.sh
- <h3>Automated way</h3> (In testing please use with caution)
  
  - git clone https://github.com/unix121/Themes
  - cd scripts/
  - sudo ./apply_theme.sh {THEME} ({THEME} should be the name of the theme you want to apply)
  
    (example on how to apply the "Minimal" theme)
    
    sudo ./apply_theme.sh Minimal
  - NOTE: This script might not be working perfectly (yet), I will fix it when I have the time to do so.

<h1>Themes<h1>
<li><h2>Colors</h2>
<img src="http://i.imgur.com/ZUEzkiT.png">
<a href="http://imgur.com/a/ub0Jl">(More can be found here)</a></li>
<li><h2>Minimal</h2>
<img src="http://i.imgur.com/aaosiZ2.png">
<a href="http://imgur.com/gallery/bZHDF">(More can be found here)</a></li>
<li><h2>Grayscale</h2>
<img src="http://i.imgur.com/K0uT5ua.png">
<a href="http://imgur.com/gallery/1TYFd">(More can be found here)</a></li>
<li><h2>Sea</h2>
<img src="http://i.imgur.com/yapFCCe.png">
<a href="http://imgur.com/a/3BsTW">(More can be found here)</a></li>

