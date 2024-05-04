"""Quicksort module."""

try:
    from src.sorting.sort import Sort
except ImportError as e:
    raise e


class Quicksort(Sort):
    """Quicksort class."""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = 'Quicksort'
        self.array = []

    def sort(self, numbers: list) -> list:
        """Quicksort algorithm."""
        self.array = numbers
        length = len(self.array)
        self.quicksort(0, length - 1)
        return self.array

    def partition(self, low, high):
        """List partition"""
        pivot = self.array[high]
        i = low - 1
        for j in range(low, high):
            self.schedule_event("compare", j, high)
            if self.array[j] <= pivot:
                i = i + 1
                (self.array[i], self.array[j]) = (self.array[j], self.array[i])
                self.schedule_event("switch", i, j)
        (self.array[i + 1], self.array[high]) = (self.array[high], self.array[i + 1])
        self.schedule_event("switch", i+1, high)
        return i + 1

    def quicksort(self, low, high):
        """Quicksort."""
        if low < high:
            pi = self.partition(low, high)
            self.quicksort(low, pi - 1)
            self.quicksort(pi + 1, high)
