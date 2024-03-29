"""Session context module."""

# PyLint modifications
# pylint: disable=no-name-in-module
# pylint: disable=import-error

from kivy.event import EventDispatcher
from kivy.properties import BooleanProperty

from src.util.decorators import singleton


@singleton
class Context(EventDispatcher):
    """Context class for ViewModels."""
    in_progress = BooleanProperty(False)
