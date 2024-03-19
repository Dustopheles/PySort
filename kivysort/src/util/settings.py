"""Settings logic module."""

from kivy.uix.popup import Popup
from kivy.uix.colorpicker import ColorPicker

try:
    from src.configs.generator_config import GeneratorConfig as Generator
    from src.configs.animation_config import AnimationConfig as Durations
    from src.configs.color_config import ColorConfig as Colors
except ImportError as i_err:
    print(i_err)

class Settings():
    """Settings class."""
    def __init__(self, ids) -> None:
        self.ids = ids
        self.color_widget = None
        self.bind_colors()

    def bind_colors(self) -> None:
        """Bind color buttons."""
        self.ids["background_color"].bind(on_press=self.create_popup)
        self.ids["passive_color"].bind(on_press=self.create_popup)
        self.ids["active_color"].bind(on_press=self.create_popup)
        self.ids["switch_color"].bind(on_press=self.create_popup)
        self.ids["sorted_color"].bind(on_press=self.create_popup)
        self.ids["text_color"].bind(on_press=self.create_popup)

    def update_settings_inputs(self) -> None:
        """Update settings TextInputs."""
        self.update_generator()
        self.update_durations()
        self.update_colors()

    def update_generator(self) -> None:
        """Update number generator input fields."""
        self.ids['members'].text = str(Generator.members)
        self.ids['lower_limit'].text = str(Generator.lower_limit)
        self.ids['upper_limit'].text = str(Generator.upper_limit)

    def update_durations(self) -> None:
        """Update animation duration input fields."""
        self.ids['switch_duration'].text = str(Durations.switch)
        self.ids['pause_duration'].text = str(Durations.pause)
        self.ids['compare_duration'].text = str(Durations.compare)

    def update_colors(self) -> None:
        """Update animation duration input fields."""
        self.ids['background_color'].background_color = Colors.background
        self.ids['passive_color'].background_color = Colors.passive
        self.ids['active_color'].background_color = Colors.active
        self.ids['switch_color'].background_color = Colors.switch
        self.ids['sorted_color'].background_color = Colors.sorted
        self.ids['text_color'].background_color = Colors.text

        self.update_widget_colors()

    def update_widget_colors(self) -> None:
        """Update colors of widgets where no binding is available."""
        self.ids["bars"].redraw_rectangle()

    def save_settings(self) -> None:
        """Save settings to dicts."""
        self.save_generator()
        self.save_durations()
        self.save_colors()
        self.update_settings_inputs()

    def save_generator(self) -> None:
        """Save number generator settings to class."""
        members = int(self.ids['members'].text)
        lower_limit = int(self.ids['lower_limit'].text)
        upper_limit = int(self.ids['upper_limit'].text)

        Generator.save_values(members=members,
                              lower_limit=lower_limit,
                              upper_limit=upper_limit)

    def save_durations(self) -> None:
        """Save animation duration settings to class."""
        compare = float(self.ids['compare_duration'].text)
        switch = float(self.ids['switch_duration'].text)
        pause = float(self.ids['pause_duration'].text)

        Durations.save_values(compare_duration=compare,
                              switch_duration=switch,
                              pause_duration=pause)

    def save_colors(self) -> None:
        """Save widget color settings to class."""
        c_background = self.ids['background_color'].background_color
        c_passive = self.ids['passive_color'].background_color
        c_active = self.ids['active_color'].background_color
        c_switch = self.ids['switch_color'].background_color
        c_sorted = self.ids['sorted_color'].background_color
        c_text = self.ids['text_color'].background_color

        Colors.save_values(color_background=c_background,
                           color_passive=c_passive,
                           color_active=c_active,
                           color_switch=c_switch,
                           color_sorted=c_sorted,
                           color_text=c_text)

    def reset_settings(self) -> None:
        """Reset settings to fallback values."""
        Generator.reset()
        Durations.reset()
        Colors.reset()
        self.update_settings_inputs()

    def create_popup(self, widget) -> None:
        """Create popup window"""
        self.color_widget = widget
        clr_picker = ColorPicker()
        clr_picker.color = widget.background_color
        # pylint: disable=no-member
        clr_picker.bind(color=self.change_color)
        popup = Popup(title='Farbauswahl',
            content=clr_picker,
            size_hint=(None, None), size=(450, 450))
        popup.open()

    def change_color(self, _widget, color) -> None:
        """Change color indicator."""
        self.color_widget.background_color = color
