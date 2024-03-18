"""Main UI module for Kivy."""

import os
import sys

from kivy.app import App
from kivy.config import Config
from kivy.lang import Builder
from kivy.resources import resource_add_path

from src.widgets.main_widget import MainWidget


class SortApp(App):
    """Kivy app builder class."""
    def build(self):
        self.title = 'PySort - Visualisierer für Sortierverfahren'
        self.configurate()
        Builder.load_file('src/kv/main.kv')
        return MainWidget()

    def configurate(self):
        """Set up kivy config."""
        Config.set('graphics', 'minimum_width', '610')
        Config.set('graphics', 'minimum_height', '450')
        Config.set('graphics', 'width', '900')
        Config.set('graphics', 'height', '600')
        Config.set('kivy', 'kivy_clock', 'interrupt')


if __name__ == '__main__':
    if hasattr(sys, '_MEIPASS'):
        # pylint: disable=protected-access
        resource_add_path(os.path.join(sys._MEIPASS))
    SortApp().run()
