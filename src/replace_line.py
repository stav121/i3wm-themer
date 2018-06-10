from tempfile import mkstemp
from shutil import move
from os import fdopen, remove

import msgfunc as prnt

def replace_line(file, pattern, new_line):
    fh, abs_path = mkstemp()
    with fdopen(fh, 'w') as new_file:
        with open( file ) as old_file:
            for line in old_file:
                if line.startswith( pattern ):
                    pl1 = line
                    pl1 = pl1.rstrip()
                    pl2 = new_line
                    pl2 = pl2.rstrip()
                    prnt.prnt( '-n', 'Replacing line: \''+pl1+'\' with \''+pl2+'\'')
                    #print (new_file.write( new_line+'\n' )=="None")
                    try:
                        new_file.write( new_line+'\n' )
                        prnt.prnt( '-s', 'Success!')
                    except:
                        prnt.prnt( '-f', 'Failed!')
                else:
                    try:
                        new_file.write( line )
                        #prnt.prnt( '-s', 'Success!')
                    except:
                        prnt.prnt( '-f', 'Failed!')
                #new_file.write( new_line if pattern in line else line)
    remove(file)
    move(abs_path, file)
