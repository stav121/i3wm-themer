import logging

from i3wmthemer.enumeration.attributes import I3Attr, XresourcesAttr
from i3wmthemer.models.abstract_theme import AbstractTheme
from i3wmthemer.utils.fileutils import FileUtils

logger = logging.getLogger(__name__)


class I3Theme(AbstractTheme):
    """
    Class that contains the attributes of the i3 theme that should be loaded.
    """
    def __init__(self, json_file):
        """
        Initializer.

        :param json_file: JSON file that contains the theme data.
        """
        self.i3theme = json_file[I3Attr.NAME.value]

        self.x_resources = json_file[XresourcesAttr.NAME.value]
        self.init_colors()

        ### default terminal
        if 'terminal' not in self.i3theme:
            self.i3theme['terminal'] = 'gnome-terminal'


    def init_colors(self):
        """Copy the color entries from the xresources part of the config to the colors for i3"""

        focused_list = ['foreground', 'background', 'foreground', 'color12', 'color12']
        unfocused_list = ['foreground', 'background', 'foreground', 'color4', 'color4']
        focused_inactive_list = ['foreground', 'background', 'foreground', 'color4', 'color4']
        urgent_list =  ['foreground', 'background', 'foreground', 'color4', 'color4']
        placeholder_list =  ['foreground', 'background', 'foreground', 'color4', 'color4']

        if "colors" not in self.i3theme:
            self.background = self.x_resources[XresourcesAttr.BACKGROUND.value]
            self.focused = " ".join([self.x_resources[i] for i in focused_list])
            self.unfocused = " ".join([self.x_resources[i] for i in unfocused_list])
            self.inactive = " ".join([self.x_resources[i] for i in focused_inactive_list])
            self.urgent = " ".join([self.x_resources[i] for i in urgent_list])
            self.placeholder = " ".join([self.x_resources[i] for i in placeholder_list])
        else:
            if 'background' in self.i3theme['colors']:
                self.background = self.parse_color_line(self.i3theme['colors']['background'], self.x_resources)
            else:
                self.background = self.x_resources[XresourcesAttr.BACKGROUND.value]

            if 'focused' in self.i3theme['colors']:
                self.focused = self.parse_color_line(self.i3theme['colors']['focused'], self.x_resources)
            else:
                self.focused = " ".join([self.x_resources[i] for i in focused_list])

            if 'unfocused' in self.i3theme['colors']:
                self.unfocused = self.parse_color_line(
                                    self.i3theme['colors']['unfocused'],
                                    self.x_resources)
            else:
                self.unfocused = " ".join([self.x_resources[i] for i in unfocused_list])

            if 'focused_inactive' in self.i3theme['colors']:
                self.inactive = self.parse_color_line(
                                    self.i3theme['colors']['focused_inactive'],
                                    self.x_resources)
            else:
                self.inactive = " ".join([self.x_resources[i] for i in focused_inactive_list])

            if 'urgent' in self.i3theme['colors']:
                self.urgent = self.parse_color_line(self.i3theme['colors']['urgent'], self.x_resources)
            else:
                self.urgent = " ".join([self.x_resources[i] for i in urgent_list])

            if 'placeholder' in self.i3theme['colors']:
                self.placeholder = self.parse_color_line(self.i3theme['colors']['placeholder'], self.x_resources)
            else:
                self.placeholder = " ".join([self.x_resources[i] for i in placeholder_list])

    def load(self, configuration):
        """Load settings into i3 config file.

        :param configuration:
        """
        # load colors
        self.load_hex(configuration)

        if "font" in self.i3theme:
            self.init_font(configuration)
        self.set_terminal(configuration)
        self.init_bindsyms(configuration)


    def init_bindsyms(self, configuration):
        """Add theme-specific bindsyms to i3 config.

        :param configuration:
        """

        if 'bindsyms' not in self.i3theme:
            return

        for command in self.i3theme['bindsyms']:
            match_found = FileUtils.replace_line(configuration.i3_config,
                                         f"bindsym {command}",
                                         f"bindsym {command} {self.i3theme['bindsyms'][command]}")
            if not match_found:
                cmd = f"bindsym {command} {self.i3theme['bindsyms'][command]}"
                with open(configuration.i3_config, "a") as f:
                    f.write(cmd)

    def init_font(self, configuration):
        """Add font info to i3 config.

        :param configuration:
        """
        with open(configuration.i3_config, "a") as f:
            f.write(f"font {self.i3theme['font']}\n")

    def set_terminal(self, configuration):
        """Set the terminal to run with $mod+Return.

        :param configuration:
        """

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

