def prnt( arg, msg ):
    prefix_blue = '\x1b[0;34;40m [>] '
    prefix_success = '\x1b[0;32;40m [>] \x1b[0m'
    prefix_fail = '\x1b[0;31;40m [x] \x1b[0m'
    prefix_fatal = '\x1b[0;31;40m [!] '
    prefix_normal = '\x1b[0m'

    if arg == '-s':
        print( prefix_success, msg)
    elif arg == '-f':
        print( prefix_fail, msg)
    elif arg == '-n':
        print( prefix_blue, msg, prefix_normal)
    else:
        print( prefix_fatal, 'Wrong argument given in prnt() function!', prefix_normal)
        exit(9)
