import logging

from i3wmthemer.enumeration.attributes import I3Attr, XresourcesAttr
from i3wmthemer.models.abstract_theme import AbstractTheme
from i3wmthemer.utils.fileutils import FileUtils

logger = logging.getLogger(__name__)


class I3Theme(AbstractTheme):
    """
    Class that contains the attributes of the i3 theme that should be loaded.
    """
    x_resources = None
    def __init__(self, json_file):
        """
        Initializer.

        :param json_file: JSON file that contains the theme data.
        """
        self.i3theme = json_file[I3Attr.NAME.value]

        ### use the xresources entry to get the colors
        if 'use_xresources' in self.i3theme and self.i3theme['use_xresources']:
            self.x_resources = json_file[XresourcesAttr.NAME.value]
            self.init_from_xresources()

        ### or get the colors written manually
        else:
            self.background = self.i3theme[I3Attr.BACKGROUND.value]
            self.focused = self.i3theme[I3Attr.FOCUSED.value]
            self.unfocused = self.i3theme[I3Attr.UNFOCUSED.value]
            self.inactive = self.i3theme[I3Attr.INACTIVE.value]
            self.urgent = self.i3theme[I3Attr.URGENT.value]
            self.placeholder = self.i3theme[I3Attr.PLACEHOLDER.value]

        if 'terminal' not in self.i3theme:
            self.i3theme['terminal'] = 'i3-sensible-terminal'

    def init_from_xresources(self):
        """Copy the color entries from the xresources part of the config to the colors for i3"""
        self.background = self.x_resources[XresourcesAttr.BACKGROUND.value]

        focused_list = ['foreground', 'background', 'foreground', 'color12', 'color12']
        unfocused_list = ['foreground', 'background', 'foreground', 'color4', 'color4']
        focused_inactive_list = ['foreground', 'background', 'foreground', 'color4', 'color4']
        urgent_list =  ['foreground', 'background', 'foreground', 'color4', 'color4']
        placeholder_list =  ['foreground', 'background', 'foreground', 'color4', 'color4']

        self.focused = " ".join([self.x_resources[i] for i in focused_list])
        self.unfocused = " ".join([self.x_resources[i] for i in unfocused_list])
        self.inactive = " ".join([self.x_resources[i] for i in focused_inactive_list])
        self.urgent = " ".join([self.x_resources[i] for i in urgent_list])
        self.placeholder = " ".join([self.x_resources[i] for i in placeholder_list])

    def load(self, configuration):
        # load colors
        self.load_hex(configuration)

        if "font" in self.i3theme:
            self.init_font(configuration)
        self.set_terminal(configuration)

    def init_font(self, configuration):
        with open(configuration.i3_config, "a") as f:
            f.write(f"font {self.i3theme['font']}\n")

    def set_terminal(self, configuration):
        with open(configuration.i3_config, "a") as f:
            f.write(f"bindsym $mod+Return exec {self.i3theme['terminal']}\n")

    def load_hex(self, configuration):
        """
        Function that loads the i3 theme.

        :param configuration: the configuration.
        """
        logger.warning('Applying changes to i3 configuration')

        if FileUtils.locate_file(configuration.i3_config):
            logger.warning('Located the i3 configuration file')

            logger.warning('Found the i3wm info in the JSON file')
            FileUtils.replace_line(configuration.i3_config, 'client.background', 'client.background ' + self.background)
            FileUtils.replace_line(configuration.i3_config, 'client.focused ', 'client.focused ' + self.focused)
            FileUtils.replace_line(configuration.i3_config, 'client.unfocused', 'client.unfocused ' + self.unfocused)
            FileUtils.replace_line(configuration.i3_config, 'client.focused_inactive',
                                   'client.focused_inactive ' + self.inactive)
            FileUtils.replace_line(configuration.i3_config, 'client.urgent',
                                   'client.urgent ' + self.urgent)
            FileUtils.replace_line(configuration.i3_config, 'client.placeholder',
                                   'client.placeholder ' + self.placeholder)
        else:
            logger.warning('Failed to locate your i3 configuration file')

