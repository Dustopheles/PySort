"""Animation config module."""

try:
    from src.configs.config import Config
except ImportError as i_err:
    print(i_err)

class AnimationConfig():
    """Animation config class."""
    section = "animation"
    compare: float = 0.5
    switch: float = 0.8
    pause: float = 0.1

    @staticmethod
    def load_values() -> None:
        """Load config values from config parser."""
        Config.read_config()
        if not Config.config.items():
            return

        try:
            compare = Config.config.getfloat(AnimationConfig.section, 'compare_duration')
            switch = Config.config.getfloat(AnimationConfig.section, 'switch_duration')
            pause = Config.config.getfloat(AnimationConfig.section, 'pause_duration')

            AnimationConfig.compare = compare
            AnimationConfig.switch = switch
            AnimationConfig.pause = pause

        except Exception as p_err:
            print(p_err)
            AnimationConfig.reset()

    @staticmethod
    def save_value(key: str, value: float) -> None:
        """Save value to config."""
        if not isinstance(value, float):
            return
        Config.config.set(AnimationConfig.section, key, value)

    @staticmethod
    def save_values(**kwargs) -> None:
        """Save values to class."""
        for value in kwargs.values():
            if not isinstance(value, float):
                return

        AnimationConfig.compare = kwargs['compare_duration']
        AnimationConfig.switch = kwargs['switch_duration']
        AnimationConfig.pause = kwargs['pause_duration']

    @staticmethod
    def save_values_to_file(**kwargs):
        """Save values to config file."""
        for key, value in kwargs.items():
            if not isinstance(value, int):
                continue
            Config.config.set(AnimationConfig.section, key, value)
        Config.write_config()

    @staticmethod
    def reset() -> None:
        """Reset values to fallback"""
        AnimationConfig.compare = 0.5
        AnimationConfig.switch = 0.8
        AnimationConfig.pause = 0.1
