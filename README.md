<link rel="stylesheet" href="https://github.com/unix121/Themes/blob/master/style.css">
  <h1>i3wm-themes</h1>
  <ul>
   My collection of themes for i3wm.
 
  ![screenshot](https://github.com/unix121/i3wm-themes/tree/master/workflow/workflow.gif) 
  </ul>
  
  <h1>What you might need</h1>
  <ul>
    <li> i3-wm in any Linux distro you prefer</li>
    <li> <a href="https://github.com/jaagr/polybar">Polybar</a> (for most of the themes)</li>
    <li> <a href="https://davedavenport.github.io/rofi/">Rofi</a> (for most of the themes)</li>
    <li> Firefox Themes can be installed using the "Stylish" extension</li>
  </ul>
  
<h1>Installation</h1> 
<ul>
<h3>Automated way</h3>
  <ul>
  <li> git clone https://github.com/unix121/i3wm-themes</li>
  <li> cd i3wm-themes/scripts/</li>
  <li> ./apply_theme.sh {THEME} ({THEME} should be the name of the theme you want to apply)

    (example on how to apply the "Minimal" theme)

    ./apply_theme.sh Minimal
 </li>
 <li> After you run the script you have to manually set the wallpaper
which is located in the {THEME} directory and also use your 
appearance manager to apply the Icons and the GTK Themes.</li>
  <li> NOTE: If you notice any bugs on the script feel free to contact me and I will address them</li>
  </ul>
 <h3>Manual Way</h3> To copy the basic configuration of a theme follow those steps:
  <ul>
  <li> git clone https://github.com/unix121/i3wm-themes </li>
  <li> cd i3wm-themes/{THEME_YOU_WANT_TO_APPLY}/</li>
  <li> cp .i3/config ~/.i3/config (or ~/.config/i3/config depending on your configuration file location)</li>
  <li> cp .config/compton.conf ~/.config/compton.conf</li>
  <li> cp .config/polybar/config ~/.config/polybar/config</li>
  <li> cp ../scripts/polybar/launch.sh ~/.config/polybar/launch.sh</li>
  <li> cp ../scripts/polybar/music.sh ~/.config/polybar/music.sh</li>
  <li> cp .resources/.Xresources ~/.Xresources</li>
  <li> cp .resources/.extend.Xresources ~/.extend.Xresources</li>
  <li> cp -R ../.fonts/. ~/.fonts/</li>
  <li> xrdb ~/.Xresources</li>
  <li> i3-msg restart</li>
  </ul>
  

</ul>
  
<h1>Themes</h1>

<ul>
  <li><h2>Space</h2>
  <img src="https://i.imgur.com/eLkyvc0.png">
  <a href="http://imgur.com/a/0hmbl">(More can be found here)</a></li>
  <li><h2>Nature</h2>
  <img src="http://i.imgur.com/1B7IA96.png">
  <a href="http://imgur.com/a/PuXie">(More can be found here)</a></li>
  <li><h2>Subway</h2>
    <img src="http://i.imgur.com/M5ZH9Dh.png">
    <a href="http://imgur.com/a/1aO8E">(More can be found here)</a></li>
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
  </ul>
