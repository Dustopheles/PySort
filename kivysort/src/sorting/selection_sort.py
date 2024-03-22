"""Selectionsort module."""

from src.sorting.sort import Sort


class Selectionsort(Sort):
    """Selectionsort class."""
    # pylint: disable=all
    def __init__(self, **kwargs):
        super(Selectionsort, self).__init__(**kwargs)
        self.sort_name = 'Selectionsort'

    def sort(self) -> None:
        """Selectionsort algorithm."""
        i_list = self.numbers
        length = len(i_list)
        size = length
        for s in range(size):
            min_idx = s
            
            for i in range(s + 1, size):
                self.schedule_event("compare", i, min_idx)
                if i_list[i] < i_list[min_idx]:
                    min_idx = i
            (i_list[s], i_list[min_idx]) = (i_list[min_idx], i_list[s])
            self.schedule_event("switch", s, min_idx)
        self.sorted_numbers = i_list
