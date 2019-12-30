import json
import logging
import unittest
from unittest.mock import patch

from i3wmthemer.models.configuration import Configuration
from i3wmthemer.models.polybar import PolybarTheme
from i3wmthemer.utils.fileutils import FileUtils

logging.disable(logging.ERROR)


class TestPolybar(unittest.TestCase):
    """
    Test polybar model.
    """

    theme_str = u' \
        { \
            "polybar": { \
                "background": "#1d1f21", \
                "foreground": "#c5c8c6", \
                "modules-left": "wlan eth", \
                "modules-center": "i3", \
                "modules-right": "date powermenu", \
                "label-unfocused-background": "#81a2be", \
                "label-unfocused-foreground": "#1d1f21", \
                "label-mode-background": "#1d1f21", \
                "label-mode-foreground": "#282a2e", \
                "label-focused-foreground": "#1d1f21", \
                "label-focused-background": "#5f819d", \
                "label-visible-background": "#81a2be", \
                "label-visible-foreground": "#1d1f21", \
                "format-foreground": "#1d1f21", \
                "format-background": "#81a2be", \
                "label-open-foreground": "#81a2be", \
                "label-close-foreground": "#81a2be", \
                "label-separator-foreground": "#81a2be", \
                "format-connected-foreground": "#1d1f21", \
                "format-connected-background": "#81a2be", \
                "format-connected-prefix-foreground": "#1d1f21", \
                "ramp-signal-foreground": "#1d1f21" \
              } \
        }'

    def test_something(self):
        """
        Test data loading from JSON.
        """

        data = json.loads(self.theme_str)

        polybar = PolybarTheme(data)

        self.assertIsNotNone(polybar.background)
        self.assertIsNotNone(polybar.modules_r)
        self.assertIsNotNone(polybar.modules_c)
        self.assertIsNotNone(polybar.modules_l)
        self.assertIsNotNone(polybar.label_un_fore)
        self.assertIsNotNone(polybar.label_un_back)
        self.assertIsNotNone(polybar.label_mod_back)
        self.assertIsNotNone(polybar.label_mod_fore)
        self.assertIsNotNone(polybar.label_foc_fore)
        self.assertIsNotNone(polybar.label_foc_back)
        self.assertIsNotNone(polybar.label_vis_back)
        self.assertIsNotNone(polybar.label_vis_fore)
        self.assertIsNotNone(polybar.format_fore)
        self.assertIsNotNone(polybar.format_back)
        self.assertIsNotNone(polybar.label_open_fore)
        self.assertIsNotNone(polybar.label_close_fore)
        self.assertIsNotNone(polybar.label_sep_fore)
        self.assertIsNotNone(polybar.format_con_back)
        self.assertIsNotNone(polybar.format_con_fore)
        self.assertIsNotNone(polybar.format_con_pre_fore)
        self.assertIsNotNone(polybar.ramp_sign_fore)

    @patch.object(FileUtils, 'locate_file')
    @patch.object(FileUtils, 'replace_line')
    def test_load(self, replace_line, locate_file):
        """
        Test load method.
        """

        configuration = Configuration('x', '', '', '', '')
        data = json.loads(self.theme_str)

        polybar = PolybarTheme(data)
        polybar.load(configuration)

        self.assertTrue(locate_file.called)
        self.assertEqual(locate_file.call_count, 1)

        self.assertTrue(replace_line.called)
        self.assertEqual(replace_line.call_count, 22)


if __name__ == '__main__':
    unittest.main()
