"""Sorthandler module."""

import importlib
import os


def get_sort(sort: str, **kwargs) -> object:
    """Return chosen sort class as object"""
    module_name = "src.sorting." + sort.lower().replace('sort', '_sort')
    module = importlib.import_module(module_name)
    class_name = getattr(module, sort)
    sort_object = class_name(**kwargs)
    return sort_object


def available_sorts() -> list:
    """Return list of available sorts."""
    modules = os.listdir(f'{os.getcwd()}/kivysort/src/sorting/')
    sorts = []
    for module in modules:
        if "_sort.py" in module:
            name = module.split('_')[0].capitalize() + 'Sort'
            sorts.append(name)

    return sorts
