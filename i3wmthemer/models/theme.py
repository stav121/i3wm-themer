from i3wmthemer.models.abstract_theme import AbstractTheme
from i3wmthemer.models.i3 import I3Theme
from i3wmthemer.models.nitrogen import NitrogenTheme
from i3wmthemer.models.polybar import PolybarTheme
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
        file = self.parse_settings(file)
        self.x_resources = XresourcesTheme(file)
        self.i3_theme = I3Theme(file)
        #self.statusbar_theme = StatusbarTheme(file)
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
        if 'use_pywal' in file['settings'] and file['settings']['use_pywal']:
            file = self.populate_file_from_pywal(file)
        return file

    def populate_file_from_pywal(self, file: dict) -> dict:

        wallpaper = file['wallpaper']
        colors = pywal.colors.get("./wallpapers/" + wallpaper)

        ### xresources
        for key in colors['colors']:
            file['xresources'][key] = colors['colors'][key]
        file['xresources']['background'] = colors['special']['background']
        file['xresources']['foreground'] = colors['special']['foreground']
        file['xresources']['cursorcolor'] = colors['special']['cursor']

        color0 = colors['colors']['color0']
        color10 = colors['colors']['color10']
        foreground = colors['special']['foreground']
        color2 = colors['colors']['color2']

        color3 = colors['colors']['color3'] # note - in original themes this color did not show up anywhere else in xresources (e.g. 78824b in 002.json)
        file['xresources']['rofi.color-window'] = f"{color0}, {color10}, {color10}"
        file['xresources']['rofi.color-normal'] = f"{color0}, {foreground}, {color2}, {foreground}, {color3}"
        file['xresources']['rofi.color-active'] = f"{color0}, {foreground}, {color2}, {foreground}, {color3}"
        file['xresources']['rofi.color-urgent'] = f"{color0}, {foreground}, {color2}, {foreground}, {color3}"
        return file
