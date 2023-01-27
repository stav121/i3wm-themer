from abc import ABC, abstractmethod
from typing import Union, List, Dict

class AbstractTheme(ABC):
    """
        Abstract Theme.
    """

    @abstractmethod
    def load(self, configuration):
        """
        Method that must be implemented.
        Should load the theme in the proper file in the configuration.

        :param configuration: the configuration.
        """
        raise NotImplementedError

    @staticmethod
    def parse_color_line(line: Union[str, List], x_resources: dict) -> str:
        """Parse a color entry from a config. If it starts wtih #, do nothing, if it's a string, replace with the corresponding hex key in xresources.

        :param line: a string or list of strings representing colors or xresources key
        :type line: Union[str, List]
        :param x_resources: dictionary with xresources colors
        :type x_resources: dict
        :rtype: str
        """
        if isinstance(line, str):
            if line[0] == "#":
                return line
            else:
                return x_resources[line]

        elif isinstance(line, list):
            ret = ""
            for elem in line:
                if elem[0] == '#':
                    ret += f"{elem} "
                else:
                    ret += f"{x_resources[elem]} "
            return ret
