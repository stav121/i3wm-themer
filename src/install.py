import os.path
from shutil import copyfile

import fileutils as fileu
import msgfunc as prnt

def install_file( config, install_file, new_file):
    if(fileu.locate_file(config[install_file])):
        prnt.prnt( '-s', 'Located '+config[install_file]+' file!')
        try:
            copyfile(new_file, config[install_file])
            prnt.prnt( '-s', 'Installed the new file successfully!')
            return True
        except:
            prnt.prnt( '-f', 'Failed to install the new file!')
            return False
    else:
        prnt.prnt( '-f', 'Could not locate '+config[install_file]+' file!')
        return False

def install_defaults( temp_folder, configuration ):
    prnt.prnt( '-n', 'Intalling the files from '+temp_folder+' file.')

    if(fileu.locate_folder(temp_folder)):
        prnt.prnt( '-n', 'Located the folder.')

        # Install default i3 file
        if 'i3-config' in configuration:
            if( install_file( configuration, 'i3-config', temp_folder+'i3.template')):
               prnt.prnt( '-s', 'Success!')
            else:
                prnt.prnt( '-f', 'Failed!')

        # Install default polybar file
        if 'polybar-config' in configuration:
            if( install_file( configuration, 'polybar-config', temp_folder+'polybar.template')):
               prnt.prnt( '-s', 'Success!')
            else:
                prnt.prnt( '-f', 'Failed!')

        # Install default Xresources file
        if 'xresources' in configuration:
            if( install_file( configuration, 'xresources', temp_folder+'xresources.template')):
                prnt.prnt( '-s', 'Success!')
            else:
                prnt.prnt( '-f', 'Failed!')

        # Install default nitrogen file
        if 'nitrogen-config' in configuration:
            if( install_file( configuration, 'nitrogen-config', temp_folder+'bg-saved.template')):
                prnt.prnt( '-s', 'Success!')
            else:
                prnt.prnt( '-f', 'Failed!')
    else:
        prnt.prnt( '-f', 'Failed to locate the folder.')
        exit(9)
