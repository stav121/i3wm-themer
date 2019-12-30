from i3wmthemer.models.abstract_theme import AbstractTheme
from i3wmthemer.models.i3 import I3Theme
from i3wmthemer.models.nitrogen import NitrogenTheme
from i3wmthemer.models.polybar import PolybarTheme
from i3wmthemer.models.xresources import XresourcesTheme


class Theme(AbstractTheme):
    """
    Class that contains the loaded theme.
    """

    def __init__(self, file):
        """
        Initializer.

        :param file: the JSON file to load from.
        """
        self.x_resources = XresourcesTheme(file)
        self.i3_theme = I3Theme(file)
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
