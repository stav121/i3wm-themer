import logging
import unittest
from unittest.mock import patch

from i3wmthemer.models.configuration import Configuration
from i3wmthemer.utils.fileutils import FileUtils
from i3wmthemer.utils.install import InstallationUtils

logging.disable(logging.ERROR)


class TestInstall(unittest.TestCase):
    """
    Test case for Install class.
    """

    @patch.object(FileUtils, 'locate_file', return_value=True)
    @patch.object(FileUtils, 'locate_folder', return_value=True)
    def test_install_defaults(self, locate_folder, copyfile_mock):
        """
        Test the backup_config function.
        """
        configuration = Configuration('', '', '', '', '')
        InstallationUtils.install_defaults('', configuration)

        self.assertTrue(copyfile_mock.called)
        self.assertEqual(copyfile_mock.call_count, 4)

        self.assertTrue(locate_folder.called)
        self.assertEqual(locate_folder.call_count, 1)


if __name__ == '__main__':
    unittest.main()
