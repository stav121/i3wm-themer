import logging
from shutil import copyfile

from i3wmthemer.utils.fileutils import FileUtils

logger = logging.getLogger(__name__)


class InstallationUtils:
    """
    Installation utility class.
    """

    @staticmethod
    def install_file(file, new_file):
        """
        Function that overrides the given file with the appropriate one
        from the configuration.
        :param file: destination.
        :param new_file: file to copy.
        :return: True if success.
        """
        if FileUtils.locate_file(file):
            logger.warning('Located %s file!', file)
            try:
                copyfile(new_file, file)
                logger.warning('Installed the new file successfully!')
                return True
            except IOError:
                logger.error('Failed to install the new file!')
                return False
        else:
            logger.error('Could not locate %s file!', file)
            return False

    @staticmethod
    def install_defaults(temp_folder, configuration):
        """
        Function that installs each configuration template file to the proper
        location in the system.

        :param temp_folder: folder that contains the templates.
        :param configuration: configuration.
        """
        logger.info('Installing the files from %s file', temp_folder)

        if FileUtils.locate_folder(temp_folder):
            logger.info('Located the folder')

            # Install default i3 file
            if configuration.i3_config is not None:
                if not InstallationUtils.install_file(configuration.i3_config, temp_folder + 'i3.template'):
                    logger.error('Failed!')

            # Install default polybar file
            if configuration.polybar_config is not None:
                if not InstallationUtils.install_file(configuration.polybar_config, temp_folder + 'polybar.template'):
                    logger.error('Failed!')

            # Install default Xresources file
            if configuration.xresources is not None:
                if not InstallationUtils.install_file(configuration.xresources, temp_folder + 'xresources.template'):
                    logger.error('Failed!')

            # Install default nitrogen file
            if configuration.nitrogen_config is not None:
                if not InstallationUtils.install_file(configuration.nitrogen_config, temp_folder + 'bg-saved.template'):
                    logger.error('Failed!')
        else:
            logger.error('Failed to locate the folder.')
            exit(9)
