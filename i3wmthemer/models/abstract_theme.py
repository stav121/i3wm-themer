from abc import ABC, abstractmethod


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
    def parse_color_line(line, x_resources):
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
