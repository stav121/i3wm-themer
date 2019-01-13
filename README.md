<h1>i3wm-themer</h1>
<ul>
Personal collection of themes and scripts for <a href="https://www.i3wm.org">i3wm</a>.

![](workflow/workflow.gif?raw=true)
</ul>

<h3>Update [April 4, 2018]</h3>
<ul>
Due to the high amount of requests to update this repository, I took the time to *completely* rework
it from the ground up. The old script is gone, the old configs are long gone. There is a <a
href="src/i3wm-themer.py">new script</a> used to apply/modify the themes for i3wm, polybar and .Xresources, all the old themes have been
reworked and a few new added. The script now uses a <a href="src/config.yaml">configuration file</a> used to locate your configs
more accurately and the themes are now presented in a <a href="src/themes">JSON</a> format to make them easier to read/modify/add your own.
This time I decided to add a few <a href="src/defaults">default configuration files</a> for you to use, to avoid the "oh my dots are now 
messed up" complains. With all that said, I hope you enjoy the fully reworked repo, I put a lot of
effort to make it meet everyone's needs/likings.
</ul>

<h1>Why?</h1>
<ul>
<li>You like CLI tools too much</li>
<li>You like simple and minimalistic desktop themes</li>
<li>You always wanted to use i3wm but can't figure it out on your own</li>
<li>You want to change themes on the go</li>
<li><a href="https://www.i3wm.org">i3wm</a> is awesome</li>
<li>Satan > Jesus</li>
</ul>

<h1>What you will need</h1>
<ul>
<li>Python 3</li>
<li><a href="https://github.com/Airblader/i3">i3-gaps</a></li>
<li><a href="https://github.com/jaagr/polybar">Polybar</a></li>
<li><a href="https://github.com/DaveDavenport/rofi">Rofi</a></li>
<li><a href="https://fontawesome.com">Font-Awesome-5</a></li>
<li><a href="https://aur.archlinux.org/packages/nitrogen-git/">Nitrogen</a></li>
<li><a href="https://aur.archlinux.org/packages/nerd-fonts-complete/">nerd-fonts-complete</a></li>
<li><a href="https://github.com/adobe-fonts/source-code-pro">Adobe Source Code Pro font</a></li>
<li><a href="https://wiki.archlinux.org/index.php/Rxvt-unicode">rxvt-unicode</a></li>
</ul>

<h2>Using the script</h2>
<ul>
Clone this repository and install the requirements for the script.

    git clone https://github.com/unix121/i3wm-themer
    cd i3wm-themer/
    sudo pip install -r requirements.txt

Install all the requirements from the 'What you will need' section.
Either manually or use one of the scripts created for some distros:

    # For Arch, ArchLabs or Manjaro Linux
    ./install_arch.sh

    # For Debian
    ./install_debian.sh

    # For Ubuntu
    ./install_ubuntu.sh

If you are not on one of the above, install them using your Package manager.

Make sure you have the requirements mentioned earlier installed.
Edit the <a href="src/config.yaml">config.yaml</a> file and add your full path of i3wm config, polybar config and .Xresources
files. In the end it should look something like this:

    i3-config: /home/[USER]/.i3/config
    polybar-config: /home/[USER]/.config/polybar/config
    xresources: /home/[USER]/.Xresources

Where `[USER]` is your `$USER`.

All further commands are to be executed from the /src directory.

Copy the script in the <a href="scripts/">scripts</a> folder to your polybar directory:

    cp -r ../scripts/* /home/$USER/.config/polybar/

Backup your files:

    mkdir ~/Backups
    python i3wm-themer.py --config config.yaml --backup /home/[USER]/Backups

This step will copy the files that you set in the `config.yaml` for safekeeping in case things go
wrong.

Install the `config files` located in the <a href="src/defaults">src/defaults/</a> directory (not 100% required but
I suggest you do so just to be sure).

    python i3wm-themer.py --config config.yaml --install defaults/

In case you get lost `$mod+Return` will open a new terminal, `$mode+d` will launch Rofi. (For the
rest of the shortcuts just take a look on the config file for i3, and change them to your needs.)

Now you are basically ready to go. Pick a theme you like from the collection and load it:

    python i3wm-themer.py --config config.yaml --load themes/[theme_id].json

(Where [theme_id] is the name of the theme you want to try!)

TADA!!!

Now every time you want to change a theme you can just run the command above with the theme you like
and apply it instantly.

You can always use the `--help` on the script to check the given options.
</ul>

<h2>Disclaimer</h2>
<ul>
I am not responsible for any harm done to your PC by anything in the repository. Use everything with
caution!
</ul>

<h2>Available Themes</h2>
<ul>
Just take a look at the <a href="src/themes/">Theme collection</a> and pick the ones you like.

![](workflow/themepreview.png?raw=true)

</ul>

<h2>Contribute to the project</h2>
<ul>
If you want to contribute to the project you can do it in two ways:
<ul>
<li>Add new themes by following this <a href="templates/README.md">guide</a></li>
<li>Help with the script by helping cross out more things from the <a href="src/README.md">TODO</a> list</li>
</ul>
</ul>

<h2>Author</h2>
<ul>
<a href="https://github.com/unix121">Stavros Grigoriou (unix121)</a>
</ul>

<h2>Support this project</h2>
<ul>
<a href="https://patreon.com/unix121">Patreon</a>
</ul>

<h2>Credits</h2>
<ul>
This whole project wouldn't be possible without the creators of all those awesome tools:
i3wm, i3-gaps, polybar and everyone who worked on those projects.
</ul>
