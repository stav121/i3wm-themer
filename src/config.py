import yaml

import fileutils as fileu
import msgfunc as prnt

def read_config( path ):
    configuration = {}

    if( fileu.locate_file( path ) ):
        prnt.prnt( '-n', 'Located the config file')
        config_path = open( path, 'r')
        config = yaml.load_all(config_path)

        for conf in config:
            for n, v in conf.items( ):
                configuration[n] = v

    else:
        prnt.prnt( '-f', 'Failed to locate the config file')
        exit(9)

    return configuration
