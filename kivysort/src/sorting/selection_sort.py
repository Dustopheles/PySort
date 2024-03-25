"""Selectionsort module."""

# pylint: disable=all
from src.sorting.sort import Sort


class Selectionsort(Sort):
    """Selectionsort class."""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.sort_name = 'Selectionsort'

    def sort(self, numbers: list) -> list:
        """Selectionsort algorithm."""
        length = len(numbers)
        for s in range(length):
            min_idenx = s
            
            for i in range(s + 1, length):
                self.schedule_event("compare", i, min_idenx)
                if numbers[i] < numbers[min_idenx]:
                    min_idenx = i
            numbers[s], numbers[min_idenx] = numbers[min_idenx], numbers[s]
            self.schedule_event("switch", s, min_idenx)
        return numbers
