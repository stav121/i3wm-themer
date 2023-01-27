#!/bin/env python3

"""
i3-wm theme changing utility.

Author  :   Stavros Grigoriou (@unix121), modified by Alex Palermo (@apalermo01)
"""

import argparse

from i3wmthemer.models.configuration import ConfigurationLoader
from i3wmthemer.models.theme import Theme
from i3wmthemer.utils.backup import BackupUtils
from i3wmthemer.utils.fileutils import FileUtils
from i3wmthemer.utils.install import InstallationUtils

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='i3wm-themer by Stavros Grigoriou (@unix121)')
    parser.add_argument('-b', '--backup', type=str, help='Backup files')
    parser.add_argument('-l', '--load', type=str, help='Load theme from JSON or YAML file')
    args = parser.parse_args()

    # TODO :: Default
    # if args.config is None:
    #     exit(0)


    #if args.backup is not None:
    #    BackupUtils.backup_config(args.backup, configuration)
    #    exit(0)


    if args.load is not None:
        theme_name = args.load
        file = FileUtils.load_theme_from_file(theme_name)
        if 'settings' not in file:
            file['settings'] = {
                    'config': "config.yaml",
                    "install": "./defaults",}
        file['settings']['theme_name'] =theme_name
        InstallationUtils.install_defaults(file)
        InstallationUtils.copy_files(theme_name, file['settings']['config'])
        theme = Theme(file)
        configLoader = ConfigurationLoader(file['settings']['config'])
        configuration = configLoader.load()
        theme.load(configuration, theme_name)
        exit(0)
