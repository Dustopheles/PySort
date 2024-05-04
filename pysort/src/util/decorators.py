"""Decorator collection module."""

def singleton(cls):
    """Singleton pattern decorator method."""
    instances = {}
    def getinstance(*arg, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*arg, **kwargs)
        return instances[cls]
    return getinstance
