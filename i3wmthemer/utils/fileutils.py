import json
import logging
import os.path
from os import fdopen, remove
from shutil import move
from tempfile import mkstemp

logger = logging.getLogger(__name__)


class FileUtils:
    """
    File utilities method.
    """

    @staticmethod
    def locate_folder(path):
        """
        Check if the given path is a directory.

        :param path: path to check.
        :return:  True if the path is an existing directory.
        """
        return os.path.isdir(path)

    @staticmethod
    def locate_file(path):
        """
        Check if the given path is file.

        :param path: path to check.
        :return: true if the path is an existing file.
        """
        return os.path.isfile(path)

    @staticmethod
    def load_theme_from_file(path):
        """
        JSon file loader.

        Loads the theme from the given JSON file and returns it.

        :param path: json filepath.
        :return: the loaded theme.
        """
        file = ''
        if FileUtils.locate_file(path):
            logger.warning('Located the Json file.')
            with open(path) as json_data:
                file = json.load(json_data)
        else:
            logger.error('Failed to locate the Json file.')
            exit(9)

        return file

    @staticmethod
    def replace_line(file, pattern, new_line):
        """
        Function that replaces the given line in the given file.

        :param file: file to modify.
        :param pattern: pattern to filter.
        :param new_line: line to replace with.
        """
        fh, abs_path = mkstemp()
        with fdopen(fh, 'w') as new_file:
            with open(file) as old_file:
                for line in old_file:
                    if line.startswith(pattern):
                        pl1 = line
                        pl1 = pl1.rstrip()
                        pl2 = new_line
                        pl2 = pl2.rstrip()
                        logger.warning('Replacing line: \'%s\' with \'%s\'', pl1, pl2)
                        try:
                            new_file.write(new_line + '\n')
                        except IOError:
                            logger.error('Failed!')
                    else:
                        try:
                            new_file.write(line)
                        except IOError:
                            logger.error('Failed!')
        remove(file)
        move(abs_path, file)
