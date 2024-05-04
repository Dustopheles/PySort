"""Main UI module for Kivy."""

import os
import sys

from kivy.app import App
from kivy.config import Config
from kivy.lang import Builder
# pylint: disable=unused-import
# PyInstaller imports for kivy
from kivy.resources import resource_add_path, resource_find

from src.view.main_view import MainView


class SortApp(App):
    """Kivy app builder class."""
    def build(self):
        self.title = 'PySort - Visualisierer für Sortierverfahren'
        self.configurate()
        Builder.load_file('src/view/main_view.kv')
        return MainView()

    def configurate(self):
        """Set kivy config values."""
        Config.set('graphics', 'minimum_width', '900')
        Config.set('graphics', 'minimum_height', '500')
        Config.set('graphics', 'width', '900')
        Config.set('graphics', 'height', '600')
        Config.set('kivy', 'kivy_clock', 'interrupt')


if __name__ == '__main__':
    # PyInstaller dependency block
    if hasattr(sys, '_MEIPASS'):
        # pylint: disable=protected-access
        resource_add_path(os.path.join(sys._MEIPASS))
    SortApp().run()
