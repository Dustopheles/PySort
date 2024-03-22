"""Color config module."""

try:
    from src.util.decorators import singleton
except ImportError as i_err:
    print(i_err)


@singleton
class ColorConfig():
    """Color config class."""
    def __init__(self) -> None:
        self.color_background = (36/255, 40/255, 47/255, 1)
        self.color_passive = (70/255, 77/255, 88/255, 1)
        self.color_active = (180/255, 180/255, 180/255, 0.9)
        self.color_switch = (1.0, 165/255, 0.0, 0.9)
        self.color_sorted = (60/255, 179/255, 113/255, 0.9)
        self.color_text = (1, 1, 1, 1)

    def set_values(self, **kwargs) -> None:
        """Set object attributes."""
        if not kwargs:
            return
        for value in kwargs.values():
            if not isinstance(value, list):
                return

        self.color_background = kwargs['color_background']
        self.color_passive = kwargs['color_passive']
        self.color_active = kwargs['color_active']
        self.color_switch = kwargs['color_switch']
        self.color_sorted = kwargs['color_sorted']
        self.color_text = kwargs['color_text']

    def get_values(self) -> dict:
        """Return object attributes as dictionary."""
        ret_dict = vars(self)
        return ret_dict

    def reset(self) -> None:
        """Reset values to fallback"""
        self.color_background = (36/255, 40/255, 47/255, 1)
        self.color_passive = (70/255, 77/255, 88/255, 1)
        self.color_active = (180/255, 180/255, 180/255, 0.9)
        self.color_switch = (1.0, 165/255, 0.0, 0.9)
        self.color_sorted = (60/255, 179/255, 113/255, 0.9)
        self.color_text = (1, 1, 1, 1)
       