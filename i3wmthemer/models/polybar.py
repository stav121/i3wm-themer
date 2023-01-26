import logging

from i3wmthemer.enumeration.attributes import PolybarAttr, XresourcesAttr
from i3wmthemer.models.abstract_theme import AbstractTheme
from i3wmthemer.utils.fileutils import FileUtils
import shutil
import os

logger = logging.getLogger(__name__)


class PolybarTheme(AbstractTheme):
    """
    Class that contains the Polybar theme attributes.
    """

    def __init__(self, json_file):
        """
        Initializer.
        :param json_file: file that contains the polybar theme.
        """
        polybar_theme = json_file[PolybarAttr.NAME.value]

        if 'use_xresources' in polybar_theme and polybar_theme['use_xresources']:
            self.x_resources = json_file[XresourcesAttr.NAME.value]
            self.modules_l = polybar_theme[PolybarAttr.MOD_L.value]
            self.modules_c = polybar_theme[PolybarAttr.MOD_C.value]
            self.modules_r = polybar_theme[PolybarAttr.MOD_R.value]
            self.init_from_xresources()

        else:
            self.colors = polybar_theme['colors']
            self.modules_l = polybar_theme[PolybarAttr.MOD_L.value]
            self.modules_c = polybar_theme[PolybarAttr.MOD_C.value]
            self.modules_r = polybar_theme[PolybarAttr.MOD_R.value]

    def init_from_xresources(self):
        self.colors = dict(
            background              = self.x_resources['background'],
            foreground              = self.x_resources['foreground'],
            label_un_back           = self.x_resources['color12'],
            label_un_fore           = self.x_resources['background'],
            label_mod_back          = self.x_resources['background'],
            label_mod_fore          = self.x_resources['color0'],
            label_foc_back          = self.x_resources['color4'],
            label_foc_fore          = self.x_resources['background'],
            label_vis_back          = self.x_resources['color12'],
            label_vis_fore          = self.x_resources['background'],
            format_back             = self.x_resources['color12'],
            format_fore             = self.x_resources['background'],
            label_open_fore         = self.x_resources['color12'],
            label_close_fore        = self.x_resources['color12'],
            label_sep_fore          = self.x_resources['color12'],
            format_con_back         = self.x_resources['color12'],
            format_con_fore         = self.x_resources['background'],
            format_con_pre_fore     = self.x_resources['background'],
            ramp_sign_fore          = self.x_resources['background'],
            label_active_background = self.x_resources['color0'],
            label_active_underline  = self.x_resources['color1'],
        )
    def load(self, configuration):
        """
        Function that loads the Polybar theme.

        :param configuration: the configuration.
        """
        logger.warning('Applying changes to Polybar configuration file')
        # copy launch script
        src_script = "./scripts/i3wmthemer_bar_launch.sh"
        dest = "/" + os.path.join(*configuration.polybar_config.split('/')[:-1])
        dest_script = os.path.join(dest, "i3wmthemer_bar_launch.sh")
        if not os.path.exists(dest):
            os.makedirs(dest)
        with open(dest_script, "w") as f:
            pass
        shutil.copy2(src_script, dest)

        if FileUtils.locate_file(configuration.polybar_config):
            logger.warning('Located the Polybar configuration file')

            logger.warning('Found the Polybar info in the JSON file')

            FileUtils.replace_line(configuration.polybar_config, 'modules-left', 'modules-left = ' + self.modules_l)
            FileUtils.replace_line(configuration.polybar_config, 'modules-center', 'modules-center = ' + self.modules_c)
            for color in self.colors:
                FileUtils.replace_line(configuration.polybar_config, color, color + " = " +  self.colors[color])
            FileUtils.replace_line(configuration.polybar_config, 'modules-right', 'modules-right = ' + self.modules_r)
        else:
            logger.error('Failed to locate the Polybar configuration file')

