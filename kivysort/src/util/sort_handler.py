"""Sorthandler module."""

import importlib
import os

class SortHandler():
    """Sort handler class."""
    @staticmethod
    def get_sort(sort: str, **kwargs) -> object:
        """Return chosen sort class as object"""
        module_name = "src.sorting." + sort.lower().replace('sort', '_sort')
        module = importlib.import_module(module_name)
        class_name = getattr(module, sort)
        sort_object = class_name(**kwargs)
        return sort_object

    @staticmethod
    def available_sorts() -> list:
        """Return list of available sorts."""
        path = SortHandler._relative_path()
        modules = os.listdir(path)
        sorts = []
        for module in modules:
            if "_sort.py" in module.lower():
                name = module.split('_')[0].capitalize() + 'sort'
                sorts.append(name)
        return sorts

    @staticmethod
    def _relative_path() -> str:
        """Return right relative os path."""
        path = os.path.join(os.getcwd(), 'kivysort', 'src', 'sorting')
        if not os.path.exists(path):
            path = os.path.join(os.getcwd(), 'src', 'sorting')
        if not os.path.exists(path):
            path = os.path.join(os.getcwd(), '_internal', 'src', 'sorting')
        return path
