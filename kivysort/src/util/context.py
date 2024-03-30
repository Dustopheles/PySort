"""Session context module."""

# pylint: disable=no-name-in-module
# pylint: disable=import-error
from kivy.event import EventDispatcher
from kivy.properties import BooleanProperty

from src.util.decorators import singleton


@singleton
class Context(EventDispatcher):
    """Context class for ViewModels."""
    in_progress = BooleanProperty(False)
    load = BooleanProperty(False)

    def __init__(self) -> None:
        self.bind(load=self.reset)

    def reset(self, *_args):
        """Reset self."""
        if self.load:
            self.load = False
