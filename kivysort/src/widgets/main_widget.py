"""Main UI Widget for kivy app."""

from kivy.uix.tabbedpanel import TabbedPanel

try:
    from src.util.settings import Settings
    from src.util.visualizer import Visualizer
except ImportError as e:
    print(e)


class MainWidget(TabbedPanel):
    """Main widget for window."""
    def __init__(self, **kwargs):
        super(MainWidget, self).__init__(**kwargs)
        self.settings = Settings(self.ids)
        self.visualizer = Visualizer(self.ids)
        self.on_load()

    def on_load(self):
        """Executed on widget creation.."""
        self.settings.update_settings_inputs()
        self.visualizer.fill_grid()

    def load_on_press(self):
        """Load button event."""
        self.visualizer.load()

    def start_on_press(self):
        """Start button event."""
        self.visualizer.start()

    def stop_on_press(self):
        """Stop button event."""
        self.visualizer.stop()

    def previous_on_press(self):
        """Previous button event."""
        self.visualizer.previous()

    def next_on_press(self):
        """Next button event."""
        self.visualizer.next()

    def save_settings_on_press(self) -> None:
        """Save button event."""
        self.settings.save_settings()

    def save_and_load_settings_on_press(self) -> None:
        """Save and load button event."""
        self.save_settings_on_press()
        self.load_on_press()

    def reset_settings_on_press(self) -> None:
        """Reset button event."""
        self.settings.reset_settings()
