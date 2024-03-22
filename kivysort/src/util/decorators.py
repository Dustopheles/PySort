"""Decorator collection module."""

def singleton(cls):
    """Singleton pattern decorator method."""
    instances = {}
    def getinstance():
        if cls not in instances:
            instances[cls] = cls()
        return instances[cls]
    return getinstance
