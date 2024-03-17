"""Operation module."""

from dataclasses import dataclass


@dataclass
class Operation():
    """Operation data class."""
    ident: int
    operation: str
    counter: int
    timeout: float
    widgets: tuple
    numbers: tuple
    event: object
