import logging
from shutil import copyfile

from i3wmthemer.utils.fileutils import FileUtils

logger = logging.getLogger(__name__)


class BackupUtils:
    """
    Basic file copy function.
    """

    @staticmethod
    def backup_file(back_file, destination):
        """
        File backup function. Copies the given file to the given destination.

        :param back_file: file to copy.
        :param destination: destination.
        :return: True if the operation is success.
        """
        if FileUtils.locate_file(back_file):
            logger.warning('Located %s file!', back_file)
            try:
                copyfile(back_file, destination)
                return True
            except IOError:
                logger.error('Failed to back it up!')
                return False
        else:
            logger.error('Could not locate %s file!', back_file)
            return False

    @staticmethod
    def backup_config(backup_folder, configuration):
        """
        Backup method. Backups up the given files:
        * i3 configuration
        * polybar configuration
        * xResources

        :param backup_folder: destination.
        :param configuration: configuration.
        """
        logger.warning('Backing up your files.')

        if FileUtils.locate_folder(backup_folder):
            logger.warning('Located the backup folder.')

            # Backup i3 file
            if configuration.i3_config is not None:
                if not BackupUtils.backup_file(configuration.i3_config, backup_folder + '/i3.config'):
                    logger.error('Failed!')

            # Backup Polybar config
            if configuration.polybar_config is not None:
                if not BackupUtils.backup_file(configuration.polybar_config, backup_folder + '/polybar.config'):
                    logger.error('Failed!')

            # Backup xresources
            if configuration.xresources is not None:
                if not BackupUtils.backup_file(configuration.xresources, backup_folder + '/xresources'):
                    logger.error('Failed!')

        else:
            logger.error('Failed to locate the backup folder.')
            exit(9)
