import logging
from shutil import copyfile

from i3wmthemer.enumeration.attributes import NitrogenAttr
from i3wmthemer.models.abstract_theme import AbstractTheme
from i3wmthemer.utils.fileutils import FileUtils

logger = logging.getLogger(__name__)


class NitrogenTheme(AbstractTheme):
    """
    Class that contains the attributes needed for Nitrogen.
    """

    def __init__(self, json_file):
        """
        Initialized.
        :param json_file: JSON file that contains the Nitrogen theme.
        """

        self.wallpaper = json_file[NitrogenAttr.NAME.value]

    def load(self, configuration):

        """
        Function that loads the wallpaper using Nitrogen.

        :param configuration: the configuration.
        """
        logger.warning('Loading wallpaper')

        if FileUtils.locate_file(configuration.nitrogen_config):
            logger.warning('Applying changes to Nitrogen configuration file')
            FileUtils.replace_line(configuration.nitrogen_config, 'file',
                                   'file= ' + configuration.wp_path + self.wallpaper)
            new_file = 'wallpapers/' + self.wallpaper
            try:
                copyfile(new_file, configuration.wp_path + self.wallpaper)
                logger.warning('Loaded the wallpaper successfully!!')
                return True
            except IOError:
                logger.error('Failed to install the new wallpaper!')
                return False
        else:
            logger.error('Failed to locate nitrogen configuration file')
