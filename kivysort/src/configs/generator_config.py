"""Number generator config module."""

try:
    from src.util.decorators import singleton
except ImportError as i_err:
    print(i_err)


@singleton
class GeneratorConfig():
    """Number generator config class."""
    def __init__(self) -> None:
        self.numbers_length: int = 10
        self.numbers_lower_limit: int = 1
        self.numbers_upper_limit: int = 30


    def _allowed_input(self, kwargs: dict) -> dict:
        """Return corrected problematic input values."""
        if kwargs['numbers_lower_limit'] > kwargs['numbers_upper_limit']:
            kwargs['numbers_lower_limit'] = kwargs['numbers_upper_limit']

        if kwargs['numbers_length'] < 2:
            kwargs['numbers_length'] = 2

        if kwargs['numbers_length'] > 100:
            kwargs['numbers_length'] = 100

        return kwargs

    def set_values(self, **kwargs) -> None:
        """Save values to class."""
        if not kwargs:
            return
        if kwargs.keys() != vars(self).keys():
            return
        for value in kwargs.values():
            if not isinstance(value, int):
                return

        kwargs = self._allowed_input(kwargs)

        for key, value in kwargs.items():
            setattr(self, key, value)

    def get_values(self) -> dict:
        """Return object attributes as dictionary."""
        obj_dict = vars(self)
        return obj_dict

    def reset(self) -> None:
        """Reset values to fallback"""
        self.numbers_length = 10
        self.numbers_lower_limit = 1
        self.numbers_upper_limit = 30
