"""ViewModel module for MVVM pattern for main view model."""

# pylint: disable=no-name-in-module
# pylint: disable=import-error
from src.util.decorators import singleton


@singleton
class MainViewModel():
    """ViewModel class for main."""
    def __init__(self, ids) -> None:
        self.ids = ids

    def set_disabled(self, state: bool, *args) -> None:
        """Switch disabled state of widgets."""
        for ident in args:
            self.ids[ident].disabled = state
