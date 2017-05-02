<h1>i3wm-themer</h1>
<ul>
  My collection of themes for i3wm.

  ![](https://github.com/unix121/i3wm-themer/blob/master/workflow/workflow1.gif?raw=true)
</ul>

<h1>What you might need</h1>
<ul>
  <li> i3-wm (maybe i3-gaps in some sections) in any Linux distro you prefer</li>
  <li> <a href="https://github.com/jaagr/polybar">Polybar</a> (for most of the themes)</li>
  <li> <a href="https://davedavenport.github.io/rofi/">Rofi</a> (for most of the themes)</li>
  <li> <a href="https://wiki.archlinux.org/index.php/nitrogen">Nitrogen</a> (To set the wallpapers, can also be done manually)</li>
  <li> Firefox Themes can be installed using the "Stylish" extension</li>
  <li> Most of the GTK Themes and Icons were created using <a href="https://github.com/actionless/oomox">oomox</a></li>
</ul>

<ul>
  All the necessary changes to your configuration files can be found under /templated_themes/{THEME}/ directory.
  Copy what you like from every configuration.
  Under /themes/{THEME}/ directory you can find my exact configuration files, but I do not recommend to copy them
  directly once they contain my own keybindings and generally settings that might not be suitable for you,
  but instead you can use the script below to apply the necessary parts from my configuration files
  to your configuration files.
</ul>

<h3>Basic requirements (for the script)</h3>
<ul>
This script is still hardcoded so you have to check where your configuration
files are before you use it.
<li> i3 configuration file must be placed either under

      ~/.i3/config or ~/.config/i3/config  

</li><li>Polybar configuration file must be under

      ~/.config/polybar/config

</li><li>Compton configuration file must be under

      ~/.config/compton.conf

</li><li>.Xresources should be under

      ~/.Xresources or ~/.extend.Xresources

</li><li>dmenu configuration file should be under

      ~/.dmenurc
</li>
<li>You will still have to make some changes "by hand" even after using the script
once it's still under development and doesn't change everything on it's own.
</li>
<li>For common issues check the issues section in the repository</li>
</ul>

<h1>How to use the scripts</h1>
<ul>
This script will overwrite only the needed parts from your configuration files
in order to apply the basic visuals of any of the themes listed below.
</ul>
<ul>

  <li> git clone https://github.com/unix121/i3wm-themer</li>
  <li> cd i3wm-themer/scripts/</li>
  <li> First backup your current configuration in case you want to come back:

      ./i3wmthemer -b {BACKUP_NAME}

Backups are saved under i3wmthemer/backups/ directory.
The backup directory will contain your configuration files mentioned in [Basic requirements] section.
If anything goes wrong you can still just copy-paste them back to their original place to get back to your current configuration manually.
  </li>

  <li> Now run the script in configuration mode to apply some of the basic changes for the theme:

      ./i3wmthemer -c

  This will add the lines that are in /templates/ directory to your i3 and polybar configuration files.

  DO NOT GO FURTHER IF THOSE CHANGES ARE NOT APPLIED CORRECTLY

  After that step you should have something like <a href="https://github.com/unix121/i3wm-themer/blob/master/templates/.i3/config">
  this</a> added to your i3 configuration file and something like <a href="https://github.com/unix121/i3wm-themer/blob/master/templates/.config/polybar/config">this</a> added under [colors] tag in
  your polybar configuration file.

  If those changes are not applied then you might have to copy them manually.

  Run this script only the first time you use this script just to setup your files.
  You don't need to run it every time you want to apply a theme, only the first time.
  </li>
  <li> Now apply the theme you want:

    ./i3wmthemer -t {THEME}

{THEME} should be the name of the theme you want to apply.

Example on how to apply the "Forest" theme:

    ./i3wmthemer -t Forest
 </li>
 <li> If you want to go back to a backup you can run the script like that:

    ./i3wmthemer -t ../backups/{BACKUP_NAME}

{BACKUP_NAME} should be the same as the one given in the backup step above.
  </li>
 <li> After you run the script you might have to manually set the wallpaper
which is located in the {THEME} directory and also use your
appearance manager to apply the Icons and the GTK Themes.</li>
  <li> NOTE: If you notice any bugs on the script feel free to contact me and I will address them</li>
</ul>

<ul>
<h3>Disclaimer</h3>
The ways mentioned above overwrite some parts of your files, use them with caution. I am not responsible if anything happens to your computer. Normally if you follow the instructions step by step everything should be just fine, but unexpected things sometimes happen. The author is not responsible for any damage done.
Also the script is still under development so any feedback/help would be much appreciated.
</ul>

</ul>

<h1>Themes</h1>

<ul>
  <li><h2>Sky</h2>
    <img src="http://i.imgur.com/mFbVgTf.png">
    <a href="http://imgur.com/a/p2ziB">(More can be found here)</a></li>
  <li><h2>Forest</h2>
    <img src="http://i.imgur.com/1WafFRk.png">
    <a href="http://imgur.com/a/SuKKf">(More can be found here)</a></li>
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
  <li><h2>Sea</h2>(Cannot be set via the script yet)
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
