from i3wmthemer.models.abstract_theme import AbstractTheme
from i3wmthemer.models.i3 import I3Theme
from i3wmthemer.models.nitrogen import NitrogenTheme
#from i3wmthemer.models.polybar import PolybarTheme
from i3wmthemer.models.status import StatusbarTheme
from i3wmthemer.models.xresources import XresourcesTheme
import pywal


class Theme(AbstractTheme):
    """
    Class that contains the loaded theme.
    """
    x_resources, i3_theme, polybar_theme, nitrogen_theme = None, None, None, None
    def __init__(self, file):
        """
        Initializer.

        :param file: the JSON file to load from.
        """
        if 'settings': in file:
            file = self.parse_settings(file)
        if 'xresources' in file:
            self.x_resources = XresourcesTheme(file)
        self.i3_theme = I3Theme(file)
        self.statusbar_theme = StatusbarTheme(file)
        self.polybar_theme = PolybarTheme(file)
        self.nitrogen_theme = NitrogenTheme(file)

    def load(self, configuration):
        """
        Batch apply all the themes.

        :param configuration: the configuration.
        """
        self.x_resources.load(configuration)
        self.i3_theme.load(configuration)
        self.polybar_theme.load(configuration)
        self.nitrogen_theme.load(configuration)
        configuration.refresh_all(self.nitrogen_theme.wallpaper)

    def parse_settings(self, file):
        if 'use_pywal' in file['settings'] and file['use_pywal']:
            file = self.populate_file_from_pywal(file)


    def populate_file_from_pywal(self, file):
        wallpaper = file['wallpaper']
        colors = pywal.colors.get(wallpaper)

        ### xresources
        for key in colors['colors']:
            file['xresources'][key] = colors['colors'][key]
        file['xresources']['background'] = colors['special']['background']
        file['xresources']['foreground'] = colors['special']['foreground']
        file['xresources']['cursorcolor'] = colors['special']['cursor']


