"""Settings tab module."""

from kivy.uix.tabbedpanel import TabbedPanelHeader
from kivy.uix.togglebutton import ToggleButton

try:
    from src.configs.generator_config import GeneratorConfig as Generator
    from src.configs.animation_config import AnimationConfig as Durations
    from src.sorting.sort_handler import SortHandler
except ImportError as e:
    print(e)


class SettingsTab(TabbedPanelHeader):
    """Settings tab class."""
    def __init__(self, **kwargs):
        super(SettingsTab, self).__init__(**kwargs)
        print(self.ids)
        #self.on_load()

    def on_load(self) -> None:
        """Call on wiget load."""
        self.update_entries()
        self.fill_grid()

    def fill_grid(self) -> None:
        """Fill choice grid with choices."""
        choices = SortHandler.available_sorts()
        for choice in choices:
            bttn = ToggleButton(text=choice, size_hint=(None, None),
                                height=50, width=200, group='sort')
            # pylint: disable=no-member
            bttn.bind(on_press=self.change_sort)
            self.ids['choice_grid'].add_widget(bttn)

    def update_entries(self) -> None:
        """Update settings TextInputs."""
        self.ids['members'].text = str(Generator.members)
        self.ids['lower_limit'].text = str(Generator.lower_limit)
        self.ids['upper_limit'].text = str(Generator.upper_limit)

        self.ids['switch_duration'].text = str(Durations.switch)
        self.ids['pause_duration'].text = str(Durations.pause)
        self.ids['compare_duration'].text = str(Durations.compare)

    def update_settings(self) -> None:
        """Update setting input fields."""
        self.ids['members'].text = str(Generator.members)
        self.ids['lower_limit'].text = str(Generator.lower_limit)
        self.ids['upper_limit'].text = str(Generator.upper_limit)

    def save_settings(self) -> None:
        """Save settings to dicts."""
        members = int(self.ids['members'].text)
        lower_limit = int(self.ids['lower_limit'].text)
        upper_limit = int(self.ids['upper_limit'].text)
        Generator.save_values(members=members,
                              lower_limit=lower_limit,
                              upper_limit=upper_limit)
        self.update_settings()
