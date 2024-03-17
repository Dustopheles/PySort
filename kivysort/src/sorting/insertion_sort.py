"""Insertionsort module."""

from src.sorting.sort import Sort


class Insertionsort(Sort):
    """Insertionsort class."""
    # pylint: disable=all
    def __init__(self, **kwargs):
        super(Insertionsort, self).__init__(**kwargs)
        self.sort_name = 'Insertionsort'

    def sort(self) -> None:
        """Insertionsort algorithm."""
        i_list = self.numbers
        length = len(i_list)
        for k in range(1, length):
            i = k
            self.schedule_event("compare", i-1, i)
            while (i_list[i] < i_list[i-1]) and (i > 0):
                i_list[i-1], i_list[i] = i_list[i], i_list[i-1]
                self.schedule_event("switch", i-1, i)
                i = i - 1
        self.sorted_numbers = i_list
