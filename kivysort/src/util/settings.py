"""Settings logic module."""

try:
    from src.configs.generator_config import GeneratorConfig as Generator
    from src.configs.animation_config import AnimationConfig as Durations
    #from src.configs.color_config import ColorConfig as Colors
except ImportError as e:
    print(e)

class Settings():
    """Settings class."""
    def __init__(self, ids) -> None:
        self.ids = ids

    def update_settings_inputs(self) -> None:
        """Update settings TextInputs."""
        self.update_generator()
        self.update_durations()

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

    def save_settings(self) -> None:
        """Save settings to dicts."""
        self.save_generator()
        self.save_durations()
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

    def reset_settings(self) -> None:
        """Reset settings to fallback values."""
        Generator.reset()
        Durations.reset()
        self.update_settings_inputs()
