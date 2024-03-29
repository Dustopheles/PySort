"""View module for MVVM pattern as root widget for settings view."""

from kivy.uix.tabbedpanel import GridLayout

# pylint: disable=no-name-in-module
# pylint: disable=import-error
from src.viewmodel.settings_view_model import SettingsViewModel


class SettingsView(GridLayout):
    """Root widget class for settings view."""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.view_model: SettingsViewModel

    def on_kv_post(self, base_widget):
        """Assign ViewModel after kv lang rules are applied."""
        # Pass ids of root to ViewModel for widget manipulation and bindings
        self.view_model = SettingsViewModel(self.ids)
        return super().on_kv_post(base_widget)
