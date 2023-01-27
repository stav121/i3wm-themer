import logging
import os
import shutil
from i3wmthemer.models.abstract_theme import AbstractTheme
from i3wmthemer.utils.fileutils import FileUtils
import textwrap


logger = logging.getLogger(__name__)

class BashTheme(AbstractTheme):
    """
    Class that extends bashrc for the given theme
    """

    def __init__(self, json_file: dict):
        """
        Initializer.

        :param json_file: JSON file that contains the theme data
        """

        self.bash_theme = json_file['bash']

        ### defaults
        # add call to wal if we want to get terminal colors from pywal
        if 'pywal_colors' in self.bash_theme and self.bash_theme['pywal_colors']:
            wp_name = json_file['wallpaper']['name']
            wallpaper_path = os.path.expanduser(f"~/Pictures/wallpapers/{wp_name}")
            self.bash_theme['extra_lines'].append(f"""
            wal -n -e -i {wallpaper_path} > /dev/null
            """)

        # function that calls onefetch if you cd into the top of a git repo
        if 'git_onefetch' in self.bash_theme and self.bash_theme['git_onefetch']:
            self.bash_theme['extra_lines'].append(textwrap.dedent("""
                function show_onefetch() {
                    if [ -d .git ]; then
                        onefetch
                    fi
                }
                function cd() { builtin cd "$@" && show_onefetch; }
                \n
            """))

        # add onefetch
        if 'neofetch' in self.bash_theme and self.bash_theme['neofetch']:
            self.bash_theme['extra_lines'].append("neofetch\n")

    def load(self, configuration):
        """add lines to bashrc.

        :param configuration:
        """
        logger.warning("adding lines to bashrc")
        bashrc_path = os.path.expanduser("~/.bashrc")
        with open(bashrc_path, "a") as f:
            for line in self.bash_theme['extra_lines']:
                logger.warning(f"appending {line} to {bashrc_path}")
                f.write(line)
