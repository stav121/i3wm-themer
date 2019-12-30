import json
import logging
import unittest
from unittest.mock import patch

from i3wmthemer.models.configuration import Configuration
from i3wmthemer.models.i3 import I3Theme
from i3wmthemer.utils.fileutils import FileUtils

logging.disable(logging.ERROR)


class TestI3(unittest.TestCase):
    """
    Tests for i3 model.
    """

    theme_str = u' \
        { \
            "i3wm": { \
                "client.background": "#1d1f21", \
                "client.focused": "#c5c8c6 #1d1f21 #c5c8c6 #81a2be #81a2be", \
                "client.unfocused": "#c5c8c6 #1d1f21 #c5c8c6 #5f819d #5f819d", \
                "client.focused_inactive": "#c5c8c6 #1d1f21 #c5c8c6 #5f819d #5f819d", \
                "client.urgent": "#c5c8c6 #1d1f21 #c5c8c6 #5f819d #5f819d", \
                "client.placeholder": "#c5c8c6 #1d1f21 #c5c8c6 #5f819d #5f819d" \
            } \
        }'

    def test_i3(self):
        """
        Test loading from JSON.
        """
        data = json.loads(self.theme_str)

        i3 = I3Theme(data)

        self.assertIsNotNone(i3.background)
        self.assertIsNotNone(i3.focused)
        self.assertIsNotNone(i3.unfocused)
        self.assertIsNotNone(i3.inactive)
        self.assertIsNotNone(i3.urgent)
        self.assertIsNotNone(i3.placeholder)

    @patch.object(FileUtils, 'locate_file')
    @patch.object(FileUtils, 'replace_line')
    def test_load(self, replace_line, locate_file):
        """
        Test load method.
        """

        configuration = Configuration('x', '', '', '', '')
        data = json.loads(self.theme_str)

        i3 = I3Theme(data)
        i3.load(configuration)

        self.assertTrue(locate_file.called)
        self.assertEqual(locate_file.call_count, 1)

        self.assertTrue(replace_line.called)
        self.assertEqual(replace_line.call_count, 6)


if __name__ == '__main__':
    unittest.main()
