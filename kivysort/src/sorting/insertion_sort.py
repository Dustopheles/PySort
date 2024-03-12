"""Insertionsort module."""

from src.sorting.sort import Sort


class Insertionsort(Sort):
    """Insertionsort class."""
    # pylint: disable=all
    def __init__(self, **kwargs):
        super(Insertionsort, self).__init__(**kwargs)
        self.sort_name = 'Insertionsort'

    def sort(self) -> None:
        """Insertion sort algorithm."""
        i_list = self.numbers
        timing = 0
        for k in range(1, len(i_list)):
            i = k
            timing = self.schedule_compare(timing, i-1, i)
            while (i_list[i] < i_list[i-1]) and (i > 0):
                i_list[i-1], i_list[i] = i_list[i], i_list[i-1]
                timing = self.schedule_switch(timing, i-1, i)
                i = i - 1
        self.sorted_numbers = i_list
