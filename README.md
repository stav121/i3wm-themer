<link rel="stylesheet" href="https://github.com/unix121/Themes/blob/master/style.css">
  <h1>i3wm-themes</h1>
  <ul>
   My collection of themes for i3wm.

  ![](https://github.com/unix121/i3wm-themes/blob/master/workflow/workflow.gif?raw=true)
  </ul>

  <h1>What you might need</h1>
  <ul>
    <li> i3-wm in any Linux distro you prefer</li>
    <li> <a href="https://github.com/jaagr/polybar">Polybar</a> (for most of the themes)</li>
    <li> <a href="https://davedavenport.github.io/rofi/">Rofi</a> (for most of the themes)</li>
    <li> Firefox Themes can be installed using the "Stylish" extension</li>
    <li> Most of the GTK Themes and Icons were created using <a href="https://github.com/actionless/oomox">oomox</a></li>
  </ul>

<h1>Installation</h1>
<ul>
<ul>

<h3>Automated way</h3>
  <ul>
  <li> git clone https://github.com/unix121/i3wm-themes</li>
  <li> cd i3wm-themes/scripts/</li>
  <li> First backup your current configuration in case you want to come back:

      ./apply_theme -b {BACKUP_NAME}

Backups are saved under ../Backups/ directory.
  </li>
  <li> Now apply the theme you want:

    ./apply_theme.sh -t {THEME}

{THEME} should be the name of the theme you want to apply.

Example on how to apply the "Minimal" theme:

    ./apply_theme.sh -t Minimal
 </li>
 <li> If you want to go back to a backup you can run the script like that:

    ./apply_theme.sh -t ../backups/{BACKUP_NAME}

{BACKUP_NAME} should be the same as the one given in the backup step above.
  </li>
 <li> After you run the script you might have to manually set the wallpaper
which is located in the {THEME} directory and also use your
appearance manager to apply the Icons and the GTK Themes.</li>
  <li> NOTE: If you notice any bugs on the script feel free to contact me and I will address them</li>
  </ul>
 <h3>Manual Way</h3> To copy the basic configuration of a theme follow those steps:
  <ul>
  <li> git clone https://github.com/unix121/i3wm-themes </li>
  <li> Backup all the files listed below before replacing them with the theme version in case you want to go back later</li>
  <li> cd i3wm-themes/themes/{THEME_YOU_WANT_TO_APPLY}/</li>
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

<ul>
<h3>Disclaimer</h3>
The ways mentioned above overwrite many of your files, use them with caution. I am not responsible if anything happens to your computer. Normally if you follow the instructions step by step everything should be just fine, but unexpected things sometimes happen. The author is not responsible for any damage done.
</ul>

</ul>

<h1>Themes</h1>

<ul>
  <li><h2>Water</h2>
    <img src="http://i.imgur.com/z3rliuz.png">
    <a href="http://imgur.com/a/PVCKq">(More can be found here)</a></li>
  <li><h2>Fire</h2>
    <img src="http://i.imgur.com/8U5DmFY.png">
    <a href="http://imgur.com/a/pYqEl">(More can be found here)</a></li>
  <li><h2>Ice</h2>
    <img src="http://i.imgur.com/3a1J77j.png">
    <a href="http://imgur.com/a/0FMYq">(More can be found here)</a></li>
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

<ul>

<h3>Note</h3>

If you are the original artist of any of the photos/pictures
featured in those themes, please feel free to contact me,
so that you can get credited.

e-mail: unix121@protonmail.com
</ul>
