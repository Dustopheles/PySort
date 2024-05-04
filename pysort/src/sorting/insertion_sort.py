"""Insertionsort module."""

try:
    from src.sorting.sort import Sort
except ImportError as e:
    raise e


class Insertionsort(Sort):
    """Insertionsort class."""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = 'Insertionsort'

    def sort(self, numbers: list) -> list:
        """Insertionsort algorithm."""
        length = len(numbers)
        for k in range(1, length):
            i = k
            self.schedule_event("compare", i-1, i)
            while (numbers[i] < numbers[i-1]) and (i > 0):
                numbers[i-1], numbers[i] = numbers[i], numbers[i-1]
                self.schedule_event("switch", i-1, i)
                i = i - 1
        return numbers
