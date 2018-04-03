import os.path

def locate_folder( path ):
    return os.path.isdir( path )

def locate_file( path ):
    return os.path.isfile( path )
