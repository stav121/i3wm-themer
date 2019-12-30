import logging
from subprocess import call

import yaml

from i3wmthemer.utils.fileutils import FileUtils

logger = logging.getLogger(__name__)


class Configuration:
    """
    Basic configuration model.
    Attributes stored:
    * i3 Configuration filepath
    * Polybar configuration filepath
    * xResources configuration filepath
    * Nitrogen configuration filepath
    * Wallpaper path
    """

    def __init__(self, i3_config, polybar_config, xresources, nitrogen_config, wp_path):
        """
        Initializer method.

        :param i3_config: i3 configuration filepath.
        :param polybar_config: polybar configuration filepath.
        :param xresources: xResources filepath.
        :param nitrogen_config: nitrogen configuration filepath.
        :param wp_path: wallpaper filepath.
        """
        # i3 config
        self.i3_config = i3_config
        # Polybar config
        self.polybar_config = polybar_config
        # xResources
        self.xresources = xresources
        # Nitrogen
        self.nitrogen_config = nitrogen_config
        # Wallpaper
        self.wp_path = wp_path

    def refresh_all(self, wallpaper):
        """
        Function that refreshes the configuration.

        :param self: current instance.
        :param wallpaper: the wallpaper file.
        """

        try:
            logger.warning('Refreshing i3 and xrdb and setting wallpaper')
            if self.wp_path is not None:
                call(['nitrogen', '--set-zoom-fill', 'wallpapers/' + wallpaper])
            call(['xrdb', self.xresources])
            call(['i3-msg', 'restart'])
            logger.warning('Done!')
        except FileNotFoundError:
            logger.error('Failed to reload the configuration!')


class ConfigurationLoader:
    """
    Configuration loader helper class.
    """

    def __init__(self, filepath):
        """
        Initializer.

        :param filepath: configuration file path.
        """
        self.filepath = filepath

    def load(self):
        """
        Function used to load the path of each configuration file into the model.

        :return: configuration model.
        """
        configuration = {}

        if FileUtils.locate_file(self.filepath):
            logger.warning('Located the config file')
            config_path = open(self.filepath, 'r')
            config = yaml.load_all(config_path)

            for conf in config:
                for n, v in conf.items():
                    configuration[n] = v

        else:
            logger.error('Failed to locate the config file')
            exit(9)

        # Set each property.
        return Configuration(configuration['i3-config'], configuration['polybar-config'], configuration['xresources'],
                             configuration['nitrogen-config'], configuration['wallpaper-path'])
