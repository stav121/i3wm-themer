import json
import logging
import unittest
from unittest.mock import patch

from i3wmthemer.models.configuration import Configuration
from i3wmthemer.models.nitrogen import NitrogenTheme
from i3wmthemer.utils.fileutils import FileUtils

logging.disable(logging.ERROR)


class TestNitrogen(unittest.TestCase):
    """
    Test nitrogen model.
    """

    theme_str = u'{"wallpaper": "000.png"}'

    def test_something(self):
        """
        Test nitrogen model.
        """
        data = json.loads(self.theme_str)

        nitro = NitrogenTheme(data)

        self.assertIsNotNone(nitro.wallpaper)

    @patch.object(FileUtils, 'locate_file')
    @patch.object(FileUtils, 'replace_line')
    def test_load(self, replace_line, locate_file):
        """
        Test load method.
        """

        configuration = Configuration('x', '', '', '', '')
        data = json.loads(self.theme_str)

        nitro = NitrogenTheme(data)
        nitro.load(configuration)

        self.assertTrue(locate_file.called)
        self.assertEqual(locate_file.call_count, 1)

        self.assertTrue(replace_line.called)
        self.assertEqual(replace_line.call_count, 1)


if __name__ == '__main__':
    unittest.main()
