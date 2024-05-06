"""Minsort module."""

try:
    from src.sorting.sort import Sort
except ImportError as e:
    raise e


class Minsort(Sort):
    """Minsort class."""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = 'Minsort'

    def sort(self, numbers: list) -> list:
        """Minsort algorithm."""
        length = len(numbers)
        for k in range(1, length):
            min_pos = k-1
            for i in range(k, length):
                self.schedule_event("compare", i, min_pos)
                if numbers[i] < numbers[min_pos]:
                    min_pos = i
            numbers[k-1], numbers[min_pos] = numbers[min_pos], numbers[k-1]
            self.schedule_event("switch", k-1, min_pos)
        return numbers
