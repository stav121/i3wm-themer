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

    def __init__(self, json_file):
        """
        Initializer.

        :param json_file: JSON file that contains the theme data
        """

        self.bash_theme = json_file['bashrc']
        print(self.bash_theme)
        if 'extra_lines' not in self.bash_theme:
            self.bash_theme['extra_lines'] = []

        if 'pywal_colors' in self.bash_theme and self.bash_theme['pywal_colors']:
            wp_name = json_file['wallpaper']['name']
            wallpaper_path = os.path.expanduser(f"~/Pictures/wallpapers/{wp_name}")
            self.bash_theme['extra_lines'].append(f"""
            wal -n -e -i {wallpaper_path}
            """)

        if 'git_onefetch' in self.bash_theme and self.bash_theme['git_onefetch']:
            self.bash_theme['extra_lines'].append(textwrap.dedent("""
                function show_onefetch() {
                    if [ -d .git ]; then
                        onefetch
                    fi
                }
                function cd() { builtin cd "$@" && show_onefetch; }

            """))

    def load(self, configuration):

        with open(os.path.expanduser("~/.bashrc"), "a") as f:
            for line in self.bash_theme['extra_lines']:
                #print(line)
                f.write(line)
