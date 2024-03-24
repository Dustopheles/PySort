"""Animation config module."""

try:
    from src.util.decorators import singleton
except ImportError as i_err:
    print(i_err)


@singleton
class AnimationConfig():
    """Animation config class."""
    def __init__(self) -> None:
        self.duration_compare: float = 0.5
        self.duration_switch: float = 0.8
        self.duration_pause: float = 0.1

    def set_values(self, **kwargs) -> None:
        """Save values to class."""
        if not kwargs:
            return
        if kwargs.keys() != vars(self).keys():
            return
        for value in kwargs.values():
            if not isinstance(value, float):
                return

        for key, value in kwargs.items():
            setattr(self, key, value)

    def get_values(self) -> dict:
        """Return object attributes as dictionary."""
        obj_dict = vars(self)
        return obj_dict

    def reset(self) -> None:
        """Reset values to fallback"""
        self.duration_compare: float = 0.5
        self.duration_switch: float = 0.8
        self.duration_pause: float = 0.1
