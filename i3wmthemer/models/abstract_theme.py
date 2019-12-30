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
