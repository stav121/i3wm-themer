import json

import replace_line as rl
import msgfunc as prnt
import fileutils as fileu

def replace_i3( configuration, json_file):
    prnt.prnt( '-n', 'Replacing the colors in your i3 configuration file')

    if( fileu.locate_file(configuration['i3-config'])):
        prnt.prnt( '-s', 'Located your i3 configuration file')
        if 'i3wm' in json_file:
            i3wm = json_file['i3wm']
            prnt.prnt( '-s', 'Found the i3wm info in the JSON file')
            rl.replace_line( configuration['i3-config'], 'client.background', 'client.background '+i3wm['client.background'])
            rl.replace_line( configuration['i3-config'], 'client.focused ', 'client.focused '+i3wm['client.focused'])
            rl.replace_line( configuration['i3-config'], 'client.unfocused', 'client.unfocused '+i3wm['client.unfocused'])
            rl.replace_line( configuration['i3-config'], 'client.focused_inactive', 'client.focused_inactive '+i3wm['client.focused_inactive'])
            rl.replace_line( configuration['i3-config'], 'client.urgent', 'client.urgent '+i3wm['client.urgent'])
            rl.replace_line( configuration['i3-config'], 'client.placeholder', 'client.placeholder '+i3wm['client.placeholder'])
    else:
        prnt.prnt( '-f', 'Failed to locate your i3 configuration file')
