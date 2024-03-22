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
        for value in kwargs.values():
            if not isinstance(value, float):
                return

        self.duration_compare = kwargs['duration_compare']
        self.duration_switch = kwargs['duration_switch']
        self.duration_pause = kwargs['duration_pause']

    def get_values(self) -> dict:
        """Return object attributes as dictionary."""
        ret_dict = vars(self)
        return ret_dict

    def reset(self) -> None:
        """Reset values to fallback"""
        self.duration_compare: float = 0.5
        self.duration_switch: float = 0.8
        self.duration_pause: float = 0.1
