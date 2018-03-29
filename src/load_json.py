import json

import fileutils as fileu
import msgfunc as prnt

def load_json( path ):
    file = ''
    if( fileu.locate_file(path) ):
        prnt.prnt( '-s', 'Located the json file')
        with open( path ) as json_data:
            file = json.load(json_data)
    else:
        prnt.prnt( '-f', 'Failed to locate the json file')
        exit( 9 )

    return file
