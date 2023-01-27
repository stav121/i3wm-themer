import logging

from i3wmthemer.models.abstract_theme import AbstractTheme
import shutil
import os
import yaml

logger = logging.getLogger(__name__)


class VimTheme(AbstractTheme):

    def __init__(self, json_file):
        self.vimtheme = json_file['vimrc']
        self.theme_name = json_file['settings']['theme_name']
        if 'plugs' not in self.vimtheme:
            self.vimtheme['plugs'] = []
        with open(json_file['settings']['config'], "r") as f:
            self.config = yaml.safe_load(f)


    def load(self, configuration):
        self.init_plug()
        self.init_colors()
        self.init_extra_lines()

    def init_extra_lines(self):
        with open(self.config['vimrc'], 'a') as f:
            for line in self.vimtheme['extra_lines']:
                f.write("\n" + line)

    def init_colors(self):
        if 'colors' in self.vimtheme:
            colors_file = self.vimtheme['colors']
            colors_path = f"./themes/{self.theme_name}/{colors_file}"
            shutil.copy(src=colors_path, dst=os.path.expanduser("~/.vim/colors/"))
        if 'colorscheme' in self.vimtheme:
            with open(self.config['vimrc'], 'a') as f:
                f.write(f"colorscheme {self.vimtheme['colorscheme']}")

    def init_plug(self):
        def _add_plug_statements(newlines, plugs):
            for plug in plugs:
                newlines.append(plug)
            return newlines


        plugs = self.vimtheme['plugs']
        newlines = []
        with open(self.config['vimrc'], 'r') as f:
            vimfile = f.readlines()

        # loop through original file, find when call plug#begin( gets called
        for line in vimfile:
            newlines.append(line)
            if "call plug#begin(" in line:
                newlines = _add_plug_statements(newlines, plugs)

        with open(self.config['vimrc'], 'w') as f:
            f.writelines(newlines)
