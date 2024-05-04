"""Sorthandler module."""

import importlib
import os


class SortHandler():
    """Sort handler class."""
    @staticmethod
    def get_sort(sort: str, **kwargs) -> object:
        """Return chosen sort class as object.

        Args:
            sort (str): Name of sort
            kwargs: Class parameter

        Returns:
            object: Sort object
        """
        module_name = "src.sorting." + sort.lower().replace('sort', '_sort')
        module = importlib.import_module(module_name)
        class_name = getattr(module, sort)
        sort_object = class_name(**kwargs)
        return sort_object

    @staticmethod
    def available_sorts() -> list[str]:
        """Return list of available sorts.

        Returns:
            list[str]: Names of all available sorts in folder sorting 
        """
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
        """Return right relative os path.

        Returns:
            str: Path to relative directory
        """
        path = os.path.join(os.getcwd(), 'pysort', 'src', 'sorting')
        if not os.path.exists(path):
            path = os.path.join(os.getcwd(), 'src', 'sorting')
        if not os.path.exists(path):
            path = os.path.join(os.getcwd(), '_internal', 'src', 'sorting')
        return path
