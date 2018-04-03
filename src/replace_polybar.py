import json

import replace_line as rl
import msgfunc as prnt
import fileutils as fileu

def replace_polybar( configuration, json_file):
    prnt.prnt( '-n', 'Replacing your Polybar configuration file')

    if( fileu.locate_file( configuration['polybar-config'])):
        prnt.prnt( '-s', 'Located your polybar configuration file')
        if 'polybar' in json_file:
            polybar = json_file['polybar']
            prnt.prnt( '-s', 'Found you polybar info in the JSON file')

            rl.replace_line( configuration['polybar-config'], 'background =', 'background = '+polybar['background'])
            rl.replace_line( configuration['polybar-config'], 'foreground =', 'foreground = '+polybar['foreground'])
            rl.replace_line( configuration['polybar-config'], 'modules-left', 'modules-left = '+polybar['modules-left'])
            rl.replace_line( configuration['polybar-config'], 'modules-center', 'modules-center = '+polybar['modules-center'])
            rl.replace_line( configuration['polybar-config'], 'modules-right', 'modules-right = '+ polybar['modules-right'])
            rl.replace_line( configuration['polybar-config'], 'label-unfocused-background', 'label-unfocused-background = '+polybar['label-unfocused-background'])
            rl.replace_line( configuration['polybar-config'], 'label-unfocused-foreground', 'label-unfocused-foreground = '+polybar['label-unfocused-foreground'])
            rl.replace_line( configuration['polybar-config'], 'label-focused-background', 'label-focused-background = '+polybar['label-focused-background'])
            rl.replace_line( configuration['polybar-config'], 'label-focused-foreground', 'label-focused-foregroun = '+polybar['label-focused-foreground'])
            rl.replace_line( configuration['polybar-config'], 'label-visible-background', 'label-visible-background = '+polybar['label-visible-background'])
            rl.replace_line( configuration['polybar-config'], 'label-visible-foreground', 'label-visible-foreground = '+polybar['label-visible-foreground'])
            rl.replace_line( configuration['polybar-config'], 'label-mode-background', 'label-mode-background = '+polybar['label-mode-background'])
            rl.replace_line( configuration['polybar-config'], 'label-mode-foreground', 'label-mode-foreground = '+polybar['label-mode-foreground'])
            rl.replace_line( configuration['polybar-config'], 'format-foreground', 'format-foreground = '+polybar['format-foreground'])
            rl.replace_line( configuration['polybar-config'], 'format-background', 'format-background = '+polybar['format-background'])
            rl.replace_line( configuration['polybar-config'], 'label-open-foreground', 'label-open-foreground = '+polybar['label-open-foreground'])
            rl.replace_line( configuration['polybar-config'], 'label-close-foreground', 'label-close-foreground = '+polybar['label-close-foreground'])
            rl.replace_line( configuration['polybar-config'], 'label-separator-foreground', 'label-separator-foreground = '+polybar['label-separator-foreground'])
            rl.replace_line( configuration['polybar-config'], 'format-connected-foreground', 'format-connected-foreground = '+polybar['format-connected-foreground'])
            rl.replace_line( configuration['polybar-config'], 'format-connected-background', 'format-connected-background = '+polybar['format-connected-background'])
            rl.replace_line( configuration['polybar-config'], 'format-connected-prefix-foreground', 'format-connected-prefix-foreground = '+polybar['format-connected-prefix-foreground'])
            rl.replace_line( configuration['polybar-config'], 'ramp-signal-foreground', 'ramp-signal-foreground = '+polybar['ramp-signal-foreground'])
        else:
            prnt.prnt( '-f', 'Failed to locate polybar info in the JSON file')
    else:
        prnt.prnt( '-f', 'Failed to locate your polybar configuration file')
