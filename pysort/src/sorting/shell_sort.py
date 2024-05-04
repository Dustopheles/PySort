"""Shellsort module."""

try:
    from src.sorting.sort import Sort
except ImportError as e:
    raise e


class Shellsort(Sort):
    """Shellsort class."""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.sort_name = 'Shellsort'

    def sort(self, numbers: list) -> list:
        """Shellsort algorithm."""
        length = len(numbers)
        gap = int(length/2)
        while gap > 0:
            for i in range(gap,length):
                temp = numbers[i]
                j = i
                self.schedule_event("compare", j, j-gap)
                while j >= gap and numbers[j-gap] > temp:
                    numbers[j] = numbers[j-gap]
                    self.schedule_event("switch", j, j-gap)
                    j -= gap
                numbers[j] = temp
            gap = int(gap/2)
        return numbers
