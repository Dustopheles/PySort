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
        if "better" in module_name:
            module_name = module_name.replace("better ", "")
            module_name += "_better"
            sort = sort.replace(" ", "")
        module = importlib.import_module(module_name)
        if not hasattr(module, sort):
            return None
        try:
            class_name = getattr(module, sort)
            sort_object = class_name(**kwargs)
        except Exception:
            return None
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
            if "_sort" in module:
                name = module.split('_')[0].capitalize() + 'sort'
                if "better" in module:
                    name = f"Better {name}"
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
