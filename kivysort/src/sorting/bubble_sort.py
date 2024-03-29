"""Bubblesort module."""

# pylint: disable=all
from src.sorting.sort import Sort


class Bubblesort(Sort):
    """Bubblesort class."""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = 'Bubblesort'

    def sort(self, numbers: list) -> list:
        """Bubblesort algorithm."""
        length = len(numbers)
        for i in range(length-1):
            for j in range(length-1-i):
                self.schedule_event("compare", j, j+1)
                if numbers[j] > numbers[j+1]:
                    numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
                    self.schedule_event("switch", j, j+1)
        return numbers
