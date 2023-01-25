import logging
from shutil import copyfile
import shutil
from i3wmthemer.enumeration.attributes import NitrogenAttr
from i3wmthemer.models.abstract_theme import AbstractTheme
from i3wmthemer.utils.fileutils import FileUtils
import os


logger = logging.getLogger(__name__)

class WallpaperTheme(AbstractTheme):

    def __init__(self, json_file):
         wallpaper_settings = json_file['wallpaper']
         method = wallpaper_settings['method']
         if method == 'feh':
            self.loader= FehTheme(json_file)
         else:
            self.loader = NitrogenTheme(json_file)
         self.wallpaper = self.loader.wallpaper

    def load(self, configuration):
        return self.loader.load(configuration)

class FehTheme(AbstractTheme):

    def __init__(self, json_file):
        self.wallpaper = json_file['wallpaper']['name']

    def load(self, configuration):
        if not os.path.exists(os.path.expanduser("~/Pictures/wallpapers/")):
            os.makedirs(os.path.expanduser("~/Picutres/wallpapers/"))
        logger.warning("Loading wallpaper")
        with open(configuration.i3_config, "a") as f:
            f.write(f"exec_always feh --bg-fill $HOME/Pictures/wallpapers/{self.wallpaper}")

        shutil.copy2(src=f"wallpapers/{self.wallpaper}",
                     dst=os.path.expanduser(f"~/Pictures/wallpapers/{self.wallpaper}"))
        return True


class NitrogenTheme(AbstractTheme):
    """
    Class that contains the attributes needed for Nitrogen.
    """

    def __init__(self, json_file):
        """
        Initialized.
        :param json_file: JSON file that contains the Nitrogen theme.
        """

        self.wallpaper = json_file['wallpaper']['name']

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
