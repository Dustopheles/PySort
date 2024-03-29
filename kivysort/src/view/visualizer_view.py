"""View module for MVVM pattern as root widget for visualizer view."""

from kivy.uix.tabbedpanel import GridLayout

# pylint: disable=no-name-in-module
# pylint: disable=import-error
from src.viewmodel.visualizer_view_model import VisualizerViewModel


class VisualizerView(GridLayout):
    """Root widget class for visualizer view."""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.view_model: VisualizerViewModel

    def on_kv_post(self, base_widget):
        """Assign ViewModel after kv lang rules are applied."""
        # Pass ids of root to ViewModel for widget manipulation and bindings
        self.view_model = VisualizerViewModel(self.ids)
        return super().on_kv_post(base_widget)
