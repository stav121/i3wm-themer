def prnt( arg, msg ):
    prefix_blue = '\x1b[0;34;40m [>] '
    prefix_success = '\x1b[0;32;40m [>] \x1b[0m'
    prefix_fail = '\x1b[0;31;40m [x] \x1b[0m'
    prefix_fatal = '\x1b[0;31;40m [!] '
    prefix_normal = '\x1b[0m'

    class bcolors:
        HEADER = '\033[95m'
        OKBLUE = '\033[94m'
        OKGREEN = '\033[92m'
        WARNING = '\033[93m'
        FAIL = '\033[91m'
        ENDC = '\033[0m'
        BOLD = '\033[1m'
        UNDERLINE = '\033[4m'

    #print ("arg=",arg," msg=",msg)
    if arg == '-s':
        print (bcolors.OKGREEN + "[>] " + bcolors.ENDC + msg)
        #print( prefix_success, msg)
    elif arg == '-f':
        print (bcolors.FAIL + "[x] " + bcolors.ENDC + msg)
        #print( prefix_fail, msg)
    elif arg == '-n':
        print (bcolors.OKBLUE + "[>] " + bcolors.ENDC + msg)
        #print( prefix_blue, msg, prefix_normal)
    else:
        print (bcolors.WARNING + "[!] " + bcolors.ENDC + msg)
        #print( prefix_fatal, 'Wrong argument given in prnt() function!', prefix_normal)
        exit(9)
