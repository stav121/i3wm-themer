import os.path
from shutil import copyfile

import fileutils as fileu
import msgfunc as prnt

def backup_file( config, back_file, destination):
    if(fileu.locate_file(config[back_file])):
        prnt.prnt( '-s', 'Located your '+config[back_file]+' file!')
        if( copyfile( config[back_file], destination)):
            prnt.prnt( '-s', 'Backed it up successfully!')
            return True
        else:
            prnt.prnt( '-f', 'Failed to back it up!')
            return False
    else:
        prnt.prnt( '-f', 'Could not locate '+config[back_file]+' file!')
        return False

def backup_config( backup_folder, configuration):
    prnt.prnt( '-n', 'Backing up your files.')

    if( fileu.locate_folder(backup_folder) ):
        prnt.prnt( '-s', 'Located the backup folder.')

        # Backup i3 file
        if 'i3-config' in configuration:
            if( backup_file( configuration, 'i3-config', backup_folder+'/i3.config')):
                prnt.prnt( '-s', 'Success!')
            else:
                prnt.prnt( '-f', 'Failed!')

        # Backup Polybr config
        if 'polybar-config' in configuration:
            if( backup_file( configuration, 'polybar-config', backup_folder+'/polybar.config')):
                prnt.prnt( '-s', 'Success!')
            else:
                prnt.prnt( '-f', 'Failed!')

        # Backup xresources
        if 'xresources' in configuration:
            if( backup_file( configuration, 'xresources', backup_folder+'/xresources')):
                prnt.prnt( '-s', 'Success!')
            else:
                prnt.prnt( '-f', 'Failed!')

    else:
       prnt.prnt( '-f', 'Failed to locate the backup folder.')
       exit(9)

