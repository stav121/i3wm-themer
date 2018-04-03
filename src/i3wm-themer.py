#!/bin/env python

#   Author  :   Stavros Grigoriou

import os
import argparse
import dis
import yaml
import os.path
from pprint import pprint

import msgfunc as prnt
import fileutils as fileu
import config as conf
import backup
import install
import load_json as lj
import replace_xresources as rx
import replace_i3 as ri
import replace_polybar as rp
import command as com

if __name__=="__main__":

    parser = argparse.ArgumentParser(description='i3wm-themer by Stavros Grigoriou')
    parser.add_argument('-c','--config', type=str, required=True, help='Load config file')
    parser.add_argument('-b','--backup', type=str, help='Backup files')
    parser.add_argument('-i','--install', type=str, help='Install i3wmthemer\'s default configuration files')
    parser.add_argument('-l','--load', type=str, help='Load theme from JSON file')
    args = parser.parse_args()

    configuration = {}

    if args.config != None :
        configuration = conf.read_config( args.config)
    else:
        exit(0)

    if args.backup != None :
        backup.backup_config( args.backup, configuration)
        exit(0)

    if args.install != None :
        install.install_defaults( args.install, configuration)
        com.refresh_all( configuration['xresources'], '')
        exit(0)

    if args.load != None:
        jfile = lj.load_json( args.load)
        rx.replace_xresources( configuration, jfile)
        ri.replace_i3( configuration, jfile)
        rp.replace_polybar( configuration, jfile)
        com.refresh_all( configuration['xresources'], jfile['wallpaper'])
        exit(0)
