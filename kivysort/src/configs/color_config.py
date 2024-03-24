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
        if kwargs.keys() != vars(self).keys():
            return
        for value in kwargs.values():
            type_bool = isinstance(value, (list, tuple))
            if not type_bool:
                return

        for key, value in kwargs.items():
            setattr(self, key, value)

    def get_values(self) -> dict:
        """Return object attributes as dictionary."""
        obj_dict = vars(self)
        return obj_dict

    def reset(self) -> None:
        """Reset values to fallback"""
        self.color_background = (36/255, 40/255, 47/255, 1)
        self.color_passive = (70/255, 77/255, 88/255, 1)
        self.color_active = (180/255, 180/255, 180/255, 0.9)
        self.color_switch = (1.0, 165/255, 0.0, 0.9)
        self.color_sorted = (60/255, 179/255, 113/255, 0.9)
        self.color_text = (1, 1, 1, 1)
       