"""Number generator config module."""

try:
    from src.configs.config import Config
except ImportError as i_err:
    print(i_err)

class GeneratorConfig():
    """Number generator config class."""
    section = "settings"
    members: int = 10
    lower_limit: int = 1
    upper_limit: int = 30

    @staticmethod
    def load_values() -> None:
        """Load config values from config parser."""
        Config.read_config()
        if not Config.config.items():
            return

        try:
            members = Config.config.getint(GeneratorConfig.section, 'members')
            lower = Config.config.getint(GeneratorConfig.section, 'lower_limit')
            upper = Config.config.getint(GeneratorConfig.section, 'upper_limit')

            GeneratorConfig.members = members
            GeneratorConfig.lower_limit = lower
            GeneratorConfig.upper_limit = upper

        except Exception as p_err:
            print(p_err)
            GeneratorConfig.reset()

    @staticmethod
    def save_value(key: str, value: int) -> None:
        """Save value to config."""
        if not isinstance(value, int):
            return
        Config.config.set(GeneratorConfig.section, key, value)

    @staticmethod
    def save_values(**kwargs) -> None:
        """Save values to class."""
        for value in kwargs.values():
            if not isinstance(value, int):
                return
        if kwargs['lower_limit'] > kwargs['upper_limit']:
            kwargs['lower_limit'] = kwargs['upper_limit']

        if kwargs['members'] < 2:
            kwargs['members'] = 2

        GeneratorConfig.members = kwargs['members']
        GeneratorConfig.lower_limit = kwargs['lower_limit']
        GeneratorConfig.upper_limit = kwargs['upper_limit']

    @staticmethod
    def save_values_to_file(**kwargs):
        """Save values to config file."""
        for key, value in kwargs.items():
            if not isinstance(value, int):
                continue
            Config.config.set(GeneratorConfig.section, key, value)
        Config.write_config()

    @staticmethod
    def reset() -> None:
        """Reset values to fallback"""
        GeneratorConfig.members = 10
        GeneratorConfig.lower_limit = 1
        GeneratorConfig.upper_limit = 30
