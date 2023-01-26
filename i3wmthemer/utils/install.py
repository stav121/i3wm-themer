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
            #try:
            print("new_file = ", new_file)
            print("file = ", file)
            shutil.copy2(new_file, file)
            logger.warning('Installed the new file successfully!')
            return True
            #except IOError:
            #    logger.error('Failed to install the new file!')
            #    return False
        else:
            logger.error('Could not locate %s file!', file)
            return False

    @staticmethod
    def install_defaults(file: dict):

        # pull config path from theme file
        if 'settings' in file and 'config' in file['settings']:
            config_path = file['settings']['config']
        else:
            config_path = "config.yaml"

        with open(config_path, "r") as f:
            config = yaml.safe_load(f)

        # pull install path from file
        if 'settings' in file and "install" in file['settings']:
            install_dir = file['settings']['install']
        else:
            install_dir = "./defaults/"

        # loop through the files in the install path
        for template in os.listdir(install_dir):
            print('='*80)
            key = template.split('.')[0]
            print("key = ", key)
            # skip if there are no entries in the config for this file
            if key not in config:
                continue

            # make a new directory and touch the file if it doesn't already exist
            if not os.path.exists(config[key]):
                dir_to_make = "/" + os.path.join(*config[key].split('/')[:-1])
                logger.warning(f"making directory {dir_to_make}")
                os.mkdir(dir_to_make)

            logger.warning(f"touching {config[key]}")
            with open(config[key], "w") as f:
                pass

            install_file = f"{key}.template"
            install_path = os.path.join(install_dir, install_file)

            # update the template to install if it's passed in the config
            if key in file and 'template' in file[key]:
                if '/' in file[key]['template']:
                    install_path = file[key]['template']
                else:
                    install_file = file[key]['template']
                    install_path = os.path.join(install_dir, install_file)

            # copy the default file
            if not InstallationUtils.install_file(config[key], install_path):
                logger.error("Failed!")

