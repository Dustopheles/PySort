"""Color config module."""

try:
    from src.configs.config import Config
except ImportError as i_err:
    print(i_err)

class ColorConfig():
    """Color config class."""
    section = "Color"
    passive = (90/255, 90/255, 90/255, 0.9)
    active = (180/255, 180/255, 180/255, 0.9)
    switch = (1.0, 165/255, 0.0, 0.9)
    sorted = (60/255, 179/255, 113/255, 0.9)

    @staticmethod
    def fixed(list_str: str) -> list:
        """Fixes stringyfication of list and returns as list."""
        list_str = list_str.strip('()[]')
        list_str = list_str.replace(' ', '')
        fixed_list = list_str.split(',')
        fixed_list = [float(x) if x.count('.') == 1 else int(x) for x in fixed_list]
        return fixed_list

    @staticmethod
    def load_values() -> None:
        """Load config values from config parser."""
        Config.read_config()
        if not Config.config.items():
            return

        try:
            rgba_passive = Config.config.get(ColorConfig.section, 'color_passive')
            rgba_active = Config.config.get(ColorConfig.section, 'color_active')
            rgba_switch = Config.config.get(ColorConfig.section, 'color_switch')
            rgba_sorted = Config.config.get(ColorConfig.section, 'color_sorted')

            ColorConfig.passive = ColorConfig.fixed(rgba_passive)
            ColorConfig.active = ColorConfig.fixed(rgba_active)
            ColorConfig.switch = ColorConfig.fixed(rgba_switch)
            ColorConfig.sorted = ColorConfig.fixed(rgba_sorted)

        except Exception as p_err:
            print(p_err)
            ColorConfig.reset()

    @staticmethod
    def save_value(key: str, value: list) -> None:
        """Save value to config."""
        if not isinstance(value, list):
            return
        value = f"[{', '.join(list)}]"
        Config.config.set(ColorConfig.section, key, value)

    @staticmethod
    def save_values(**kwargs) -> None:
        """Save values to class."""
        for value in kwargs.values():
            if not isinstance(value, list):
                return

        ColorConfig.passive = kwargs['color_passive']
        ColorConfig.active = kwargs['color_active']
        ColorConfig.switch = kwargs['color_switch']
        ColorConfig.sorted = kwargs['color_sorted']

    @staticmethod
    def save_values_to_file(**kwargs):
        """Save values to config file."""
        for key, value in kwargs.items():
            if not isinstance(value, list):
                continue
            value = f"[{', '.join(list)}]"
            Config.config.set(ColorConfig.section, key, value)
        Config.write_config()

    @staticmethod
    def reset() -> None:
        """Reset values to fallback"""
        ColorConfig.passive = (90/255, 90/255, 90/255, 0.9)
        ColorConfig.active = (180/255, 180/255, 180/255, 0.9)
        ColorConfig.switch = (1.0, 165/255, 0.0, 0.9)
        ColorConfig.sorted = (60/255, 179/255, 113/255, 0.9)
