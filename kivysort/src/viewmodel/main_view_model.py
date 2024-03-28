"""Visualizer logic module."""

# pylint: disable=no-name-in-module
# pylint: disable=import-error
from src.util.decorators import singleton


@singleton
class MainViewModel():
    """Visualizer class."""
    def __init__(self, ids) -> None:
        self.ids = ids
