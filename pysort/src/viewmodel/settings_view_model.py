"""ViewModel module for MVVM pattern for settings view model."""

from kivy.uix.popup import Popup
from kivy.uix.colorpicker import ColorPicker

try:
    from src.configs.generator_config import GeneratorConfig
    from src.configs.animation_config import AnimationConfig
    from src.configs.color_config import ColorConfig
    from src.util.decorators import singleton
    from src.util.context import Context
except ImportError as e:
    raise e


@singleton
class SettingsViewModel():
    """ViewModel class for settings."""
    numbers = GeneratorConfig()
    colors = ColorConfig()
    durations = AnimationConfig()
    context = Context()

    def __init__(self, ids) -> None:
        self.ids = ids
        self.color_widget = None
        self.on_init()

    def on_init(self) -> None:
        """Bind properties."""
        self.ids["save_bttn"].bind(on_release=self.save_settings)
        self.ids["save_n_load_bttn"].bind(on_release=self.save_n_load_settings)
        self.ids["reset_bttn"].bind(on_release=self.reset_settings)
        self.ids["generator_bttn"].bind(on_release=self.switch_tab)
        self.ids["animation_bttn"].bind(on_release=self.switch_tab)
        self.ids["colors_bttn"].bind(on_release=self.switch_tab)

        self.context.bind(in_progress=self.on_sort_state_changed)
        self.bind_colors()
        self.update_settings_inputs()

    def switch_tab(self, widget, *_args) -> None:
        """Switch tab to selected."""
        self.ids['settings_panel'].switch_to(self.ids[widget.tab])

    def on_sort_state_changed(self, _widget, value) -> None:
        """Handle button states."""
        self.set_disabled(value, "save_bttn", "reset_bttn")

    def bind_colors(self) -> None:
        """Bind color buttons."""
        for key, value in self.ids.items():
            if "color_" in key:
                value.bind(on_release=self.create_popup)

    def update_settings_inputs(self) -> None:
        """Update settings TextInputs."""
        self.update_generator()
        self.update_durations()
        self.update_colors()

    def update_generator(self) -> None:
        """Update number generator input fields."""
        numbers = vars(self.numbers)
        for key, value in self.ids.items():
            if "numbers_" in key:
                value.text = str(numbers[key])

    def update_durations(self) -> None:
        """Update animation duration input fields."""
        durations = vars(self.durations)
        for key, value in self.ids.items():
            if "duration_" in key:
                value.text = str(durations[key])

    def update_colors(self) -> None:
        """Update animation duration input fields."""
        colors = vars(self.colors)
        for key, value in self.ids.items():
            if "color_" in key:
                value.background_color = colors[key]
        self.update_widget_colors()

    def update_widget_colors(self) -> None:
        """Update colors of widgets where no binding is available."""
        #self.ids["bars"].redraw_rectangle()

    def save_settings(self, *_args) -> None:
        """Save settings to dicts."""
        self.save_generator()
        self.save_durations()
        self.save_colors()
        self.update_settings_inputs()

    def save_n_load_settings(self, *_args) -> None:
        """Save settings and reload."""
        self.save_settings(*_args)
        self.set_disabled(False, 'save_bttn', 'reset_bttn')
        self.context.load = True

    def save_generator(self) -> None:
        """Save number generator settings to class."""
        numbers_kwargs = {}
        for key, value in self.ids.items():
            if "numbers_" in key:
                numbers_kwargs[key] = int(value.text)
        self.numbers.set_values(**numbers_kwargs)

    def save_durations(self) -> None:
        """Save animation duration settings to class."""
        duration_kwargs = {}
        for key, value in self.ids.items():
            if "duration_" in key:
                duration_kwargs[key] = float(value.text)

        self.durations.set_values(**duration_kwargs)

    def save_colors(self) -> None:
        """Save widget color settings to class."""
        color_kwargs = {}
        for key, value in self.ids.items():
            if "color_" in key:
                color_kwargs[key] = value.background_color

        self.colors.set_values(**color_kwargs)

    def reset_settings(self, *_args) -> None:
        """Reset settings to fallback values."""
        self.numbers.reset()
        self.durations.reset()
        self.colors.reset()
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
                      size_hint=(None, None),
                      size=(450, 450))
        popup.open()

    def change_color(self, _widget, color) -> None:
        """Change color indicator."""
        self.color_widget.background_color = color

    def set_disabled(self, state: bool, *args) -> None:
        """Switch disabled state of widgets."""
        for ident in args:
            self.ids[ident].disabled = state

    def popup_on_release(self, *_args) -> None:
        """Popup on button release event."""
        self.create_popup(*_args)
