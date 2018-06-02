import json

import os.path
from shutil import copyfile

import replace_line as rl
import msgfunc as prnt
import fileutils as fileu

def replace_wallpaper( configuration, json_file):
    prnt.prnt( '-n', 'Replacing wallpaper')

    if( fileu.locate_file(configuration['nitrogen-config'])):
        prnt.prnt( '-s', 'Located your nitrogen configuration file')
        if 'wallpaper' in json_file:
            wallpaper = json_file['wallpaper']
            prnt.prnt( '-s', 'Found the wallpaper info in the JSON file')

            rl.replace_line( configuration['nitrogen-config'], 'file', 'file= '+configuration['wallpaper-path']+wallpaper)
            new_file='wallpapers/'+wallpaper
            if(copyfile(new_file, configuration['wallpaper-path']+wallpaper)):
                prnt.prnt( '-s', 'Installed the new file successfully!')
                return True
            else:
                prnt.prnt( '-f', 'Failed to install the new file!')
                return False
    else:
        prnt.prnt( '-f', 'Failed to locate your nitrogen configuration file')
