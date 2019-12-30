#!/bin/env python3

"""
i3-wm theme changing utility.

Author  :   Stavros Grigoriou (@unix121)
"""

import argparse

from i3wmthemer.models.configuration import ConfigurationLoader
from i3wmthemer.models.theme import Theme
from i3wmthemer.utils.backup import BackupUtils
from i3wmthemer.utils.fileutils import FileUtils
from i3wmthemer.utils.install import InstallationUtils

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='i3wm-themer by Stavros Grigoriou (@unix121)')
    parser.add_argument('-c', '--config', type=str, required=True, help='Load config file')
    parser.add_argument('-b', '--backup', type=str, help='Backup files')
    parser.add_argument('-i', '--install', type=str, help='Install i3wm-themer\'s default configuration files')
    parser.add_argument('-l', '--load', type=str, help='Load theme from JSON file')
    args = parser.parse_args()

    # TODO :: Default
    if args.config is None:
        exit(0)

    # Load the configuration
    configLoader = ConfigurationLoader(args.config)
    configuration = configLoader.load()

    if args.backup is not None:
        BackupUtils.backup_config(args.backup, configuration)
        exit(0)

    if args.install is not None:
        InstallationUtils.install_defaults(args.install, configuration)
        configuration.refresh_all('')
        exit(0)

    if args.load is not None:
        file = FileUtils.load_theme_from_file(args.load)
        theme = Theme(file)
        theme.load(configuration)
        exit(0)
