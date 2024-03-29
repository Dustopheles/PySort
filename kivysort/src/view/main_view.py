"""View module for MVVM pattern as root widget for main view."""

from kivy.uix.tabbedpanel import TabbedPanel

# pylint: disable=no-name-in-module
# pylint: disable=import-error
from src.viewmodel.main_view_model import MainViewModel


class MainView(TabbedPanel):
    """Root widget class for main view."""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.view_model: MainViewModel

    def on_kv_post(self, base_widget):
        """Assign ViewModel after kv lang rules are applied."""
        # Pass ids of root to ViewModel for widget manipulation and bindings
        self.view_model = MainViewModel(self.ids)
        return super().on_kv_post(base_widget)
