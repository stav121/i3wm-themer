import logging

from i3wmthemer.enumeration.attributes import XresourcesAttr
from i3wmthemer.models.abstract_theme import AbstractTheme
from i3wmthemer.utils.fileutils import FileUtils

logger = logging.getLogger(__name__)


class XresourcesTheme(AbstractTheme):
    """
    .Xresources theme properties store.

    Contains all the data tha should be loaded:
    * Foreground
    * Background
    * 0-15 Colors
    * Rofi
    """

    def __init__(self, json_file):
        """
        Initializer.
        :param json_file: json file to parse.
        """

        # Locate the 'xresources' tag in the json_file
        data = json_file[XresourcesAttr.NAME.value]

        # Background and foreground.
        self.background = data[XresourcesAttr.BACKGROUND.value]
        self.foreground = data[XresourcesAttr.FOREGROUND.value]
        self.cursor_color = data[XresourcesAttr.CURSOR.value]

        # 16 colors.
        self.color0 = data[XresourcesAttr.COLOR0.value]
        self.color1 = data[XresourcesAttr.COLOR1.value]
        self.color2 = data[XresourcesAttr.COLOR2.value]
        self.color3 = data[XresourcesAttr.COLOR3.value]
        self.color4 = data[XresourcesAttr.COLOR4.value]
        self.color5 = data[XresourcesAttr.COLOR5.value]
        self.color6 = data[XresourcesAttr.COLOR6.value]
        self.color7 = data[XresourcesAttr.COLOR7.value]
        self.color8 = data[XresourcesAttr.COLOR8.value]
        self.color9 = data[XresourcesAttr.COLOR9.value]
        self.color10 = data[XresourcesAttr.COLOR10.value]
        self.color11 = data[XresourcesAttr.COLOR11.value]
        self.color12 = data[XresourcesAttr.COLOR12.value]
        self.color13 = data[XresourcesAttr.COLOR13.value]
        self.color14 = data[XresourcesAttr.COLOR14.value]
        self.color15 = data[XresourcesAttr.COLOR15.value]

        # Rofi.
        self.rofi_window = data[XresourcesAttr.ROFI_WIND.value]
        self.rofi_normal = data[XresourcesAttr.ROFI_NORM.value]
        self.rofi_urgent = data[XresourcesAttr.ROFI_URGE.value]
        self.rofi_active = data[XresourcesAttr.ROFI_ACTI.value]

    def load(self, configuration):
        """
        Function that loads the theme by replacing lines in the original file.

        :param configuration: the configuration.
        """
        logger.warning('Applying changes to .Xresources')

        if FileUtils.locate_file(configuration.xresources):
            logger.warning('Located .Xresources file.')

            FileUtils.replace_line(configuration.xresources, '*background:',
                                   '*background: ' + self.background)
            FileUtils.replace_line(configuration.xresources, '*foreground:',
                                   '*foreground: ' + self.foreground)
            FileUtils.replace_line(configuration.xresources, '*cursorColor:',
                                   '*cursorColor: ' + self.cursor_color)
            FileUtils.replace_line(configuration.xresources, '*color0:', '*color0: ' + self.color0)
            FileUtils.replace_line(configuration.xresources, '*color1:', '*color1: ' + self.color1)
            FileUtils.replace_line(configuration.xresources, '*color2:', '*color2: ' + self.color2)
            FileUtils.replace_line(configuration.xresources, '*color3:', '*color3: ' + self.color3)
            FileUtils.replace_line(configuration.xresources, '*color4:', '*color4: ' + self.color4)
            FileUtils.replace_line(configuration.xresources, '*color5:', '*color5: ' + self.color5)
            FileUtils.replace_line(configuration.xresources, '*color6:', '*color6: ' + self.color6)
            FileUtils.replace_line(configuration.xresources, '*color7:', '*color7: ' + self.color7)
            FileUtils.replace_line(configuration.xresources, '*color8:', '*color8: ' + self.color8)
            FileUtils.replace_line(configuration.xresources, '*color9:', '*color9: ' + self.color9)
            FileUtils.replace_line(configuration.xresources, '*color10:', '*color10: ' + self.color10)
            FileUtils.replace_line(configuration.xresources, '*color11:', '*color11: ' + self.color11)
            FileUtils.replace_line(configuration.xresources, '*color12:', '*color12: ' + self.color12)
            FileUtils.replace_line(configuration.xresources, '*color13:', '*color13: ' + self.color13)
            FileUtils.replace_line(configuration.xresources, '*color14:', '*color14: ' + self.color14)
            FileUtils.replace_line(configuration.xresources, '*color15:', '*color15: ' + self.color15)
            FileUtils.replace_line(configuration.xresources, 'rofi.color-window:',
                                   'rofi.color-window: ' + self.rofi_window)
            FileUtils.replace_line(configuration.xresources, 'rofi.color-normal:',
                                   'rofi.color-normal: ' + self.rofi_normal)
            FileUtils.replace_line(configuration.xresources, 'rofi.color-active:',
                                   'rofi.color-active: ' + self.rofi_active)
            FileUtils.replace_line(configuration.xresources, 'rofi.color-urgent:',
                                   'rofi.color-urgent: ' + self.rofi_urgent)
        else:
            logger.error('Failed to locate your .Xresources file')
