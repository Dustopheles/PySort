"""Session context module."""

from kivy.event import EventDispatcher
# pylint: disable=no-name-in-module
from kivy.properties import BooleanProperty

# pylint: disable=import-error
from src.util.decorators import singleton


@singleton
class Context(EventDispatcher):
    """Context class for ViewModels."""
    in_progress = BooleanProperty(False)
