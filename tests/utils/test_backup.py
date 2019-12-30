import logging
import unittest
from unittest.mock import patch

from i3wmthemer.models.configuration import Configuration
from i3wmthemer.utils.backup import BackupUtils
from i3wmthemer.utils.fileutils import FileUtils

logging.disable(logging.ERROR)


class TestBackup(unittest.TestCase):
    """
    Test case for Backup class.
    """

    @patch.object(FileUtils, 'locate_file', return_value=True)
    def test_backup_file(self, copyfile_mock):
        """
        Test the backup_file function.
        """
        BackupUtils.backup_file('', '')

        self.assertTrue(copyfile_mock.called)
        self.assertEqual(copyfile_mock.call_count, 1)

    @patch.object(FileUtils, 'locate_file', return_value=True)
    @patch.object(FileUtils, 'locate_folder', return_value=True)
    def test_backup_config(self, locate_folder, copyfile_mock):
        """
        Test the backup_config function.
        """
        configuration = Configuration('', '', '', '', '')
        BackupUtils.backup_config('', configuration)

        self.assertTrue(copyfile_mock.called)
        self.assertEqual(copyfile_mock.call_count, 3)

        self.assertTrue(locate_folder.called)
        self.assertEqual(locate_folder.call_count, 1)


if __name__ == '__main__':
    unittest.main()
