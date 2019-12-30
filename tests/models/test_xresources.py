import json
import logging
import unittest
from unittest.mock import patch

from i3wmthemer.models.configuration import Configuration
from i3wmthemer.models.xresources import XresourcesTheme
from i3wmthemer.utils.fileutils import FileUtils

logging.disable(logging.ERROR)


class TestXresources(unittest.TestCase):
    """
    Test case for Xresources model.
    """

    theme_str = u' \
    { \
        "xresources": { \
            "background": "#1d1f21", \
            "foreground": "#c5c8c6", \
            "cursorcolor": "#c5c8c6", \
            "color0": "#282a2e", \
            "color1": "#a54242", \
            "color2": "#8c9440", \
            "color3": "#de935f", \
            "color4": "#5f819d", \
            "color5": "#85678f", \
            "color6": "#5e8d87", \
            "color7": "#707880", \
            "color8": "#373b41", \
            "color9": "#cc6666", \
            "color10": "#b5bd68", \
            "color11": "#f0c674", \
            "color12": "#81a2be", \
            "color13": "#b294bb", \
            "color14": "#8abeb7", \
            "color15": "#c5c8c6", \
            "rofi.color-window": "#282a2e, #b5bd68, #b5bd68", \
            "rofi.color-normal": "#282a2e, #c5c8c6, #8c9440, #c5c8c6, #78824B", \
            "rofi.color-active": "#282a2e, #c5c8c6, #8c9440, #c5c8c6, #78824B", \
            "rofi.color-urgent": "#282a2e, #c5c8c6, #8c9440, #c5c8c6, #78824B" \
        } \
    }'

    def test_xresources(self):
        """
        Test loading from JSON file.
        """
        data = json.loads(self.theme_str)

        xresources = XresourcesTheme(data)
        self.assertIsNotNone(xresources.background)
        self.assertIsNotNone(xresources.foreground)
        self.assertIsNotNone(xresources.cursor_color)
        self.assertIsNotNone(xresources.color0)
        self.assertIsNotNone(xresources.color1)
        self.assertIsNotNone(xresources.color2)
        self.assertIsNotNone(xresources.color3)
        self.assertIsNotNone(xresources.color4)
        self.assertIsNotNone(xresources.color5)
        self.assertIsNotNone(xresources.color6)
        self.assertIsNotNone(xresources.color7)
        self.assertIsNotNone(xresources.color8)
        self.assertIsNotNone(xresources.color9)
        self.assertIsNotNone(xresources.color10)
        self.assertIsNotNone(xresources.color11)
        self.assertIsNotNone(xresources.color12)
        self.assertIsNotNone(xresources.color13)
        self.assertIsNotNone(xresources.color14)
        self.assertIsNotNone(xresources.color15)
        self.assertIsNotNone(xresources.rofi_window)
        self.assertIsNotNone(xresources.rofi_normal)
        self.assertIsNotNone(xresources.rofi_active)
        self.assertIsNotNone(xresources.rofi_urgent)

    @patch.object(FileUtils, 'locate_file')
    @patch.object(FileUtils, 'replace_line')
    def test_xresources_load(self, replace_line, locate_file):
        """
        Test the load method of Xresources.
        """

        configuration = Configuration('x', '', '', '', '')
        data = json.loads(self.theme_str)

        xresources = XresourcesTheme(data)
        xresources.load(configuration)

        self.assertTrue(locate_file.called)
        self.assertEqual(locate_file.call_count, 1)

        self.assertTrue(replace_line.called)
        self.assertEqual(replace_line.call_count, 23)


if __name__ == '__main__':
    unittest.main()
