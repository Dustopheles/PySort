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

    def set_values(self, **kwargs) -> None:
        """Save values to class."""
        if not kwargs:
            return
        for value in kwargs.values():
            if not isinstance(value, int):
                return
        if kwargs['numbers_lower_limit'] > kwargs['numbers_upper_limit']:
            kwargs['numbers_lower_limit'] = kwargs['numbers_upper_limit']

        if kwargs['numbers_length'] < 2:
            kwargs['numbers_length'] = 2

        self.numbers_length = kwargs['numbers_length']
        self.numbers_lower_limit = kwargs['numbers_lower_limit']
        self.numbers_upper_limit = kwargs['numbers_upper_limit']

    def reset(self) -> None:
        """Reset values to fallback"""
        self.numbers_length = 10
        self.numbers_lower_limit = 1
        self.numbers_upper_limit = 30
