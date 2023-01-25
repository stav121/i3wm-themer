import logging
#from shutil import copyfile
import shutil
import os
from i3wmthemer.utils.fileutils import FileUtils
import yaml
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
                print("src: ", new_file)
                print("destination: ", file)
                shutil.copy2(new_file, file)
                logger.warning('Installed the new file successfully!')
                return True
            except IOError:
                logger.error('Failed to install the new file!')
                return False
        else:
            logger.error('Could not locate %s file!', file)
            return False

    @staticmethod
    def install_defaults(file: dict):
        if 'config' in file['settings']:
            config_path = file['settings']['config']
        else:
            config_path = "config.yaml"

        if "install" in file['settings']:
            install_path = file['settings']['install']
        else:
            install_path = "./defaults/"

        with open(config_path, "r") as f:
            config = yaml.safe_load(f)

        for template in os.listdir(install_path):
            key = template.split('.')[0]
            if key not in config:
                continue
            print(f"template={template}, target={config[key]}")
            if not os.path.exists(config[key]):
                print('generating path', config[key])
                dir_to_make = "/" + os.path.join(*config[key].split('/')[:-1])
                print("dir to make = ", dir_to_make)
                os.mkdir(dir_to_make)
                with open(config[key], "w") as f:
                    pass
            if not InstallationUtils.install_file(config[key], os.path.join(install_path, f"{key}.template")):
                logger.error("Failed!")

    def install_defaults_old(temp_folder, configuration):
        """
        DOCSTRING DEPRECIATED
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
                if not InstallationUtils.install_file(configuration.i3_config, temp_folder + '/i3.template'):
                    logger.error('Failed!')

            # Install default polybar file
            if configuration.polybar_config is not None:
                if not InstallationUtils.install_file(configuration.polybar_config, temp_folder + '/polybar.template'):
                    logger.error('Failed!')

            # Install default Xresources file
            if configuration.xresources is not None:
                if not InstallationUtils.install_file(configuration.xresources, temp_folder + '/xresources.template'):
                    logger.error('Failed!')

            # Install default nitrogen file
            if configuration.nitrogen_config is not None:
                if not InstallationUtils.install_file(configuration.nitrogen_config, temp_folder + '/bg-saved.template'):
                    logger.error('Failed!')
        else:
            logger.error('Failed to locate the folder.')
            exit(9)
