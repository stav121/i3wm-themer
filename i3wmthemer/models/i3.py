import logging

from i3wmthemer.enumeration.attributes import I3Attr
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
        i3theme = json_file[I3Attr.NAME.value]

        self.background = i3theme[I3Attr.BACKGROUND.value]
        self.focused = i3theme[I3Attr.FOCUSED.value]
        self.unfocused = i3theme[I3Attr.UNFOCUSED.value]
        self.inactive = i3theme[I3Attr.INACTIVE.value]
        self.urgent = i3theme[I3Attr.URGENT.value]
        self.placeholder = i3theme[I3Attr.PLACEHOLDER.value]

    def load(self, configuration):
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
