"""Shellsort module."""

from src.sorting.sort import Sort


class Shellsort(Sort):
    """Shellsort class."""
    # pylint: disable=all
    def __init__(self, **kwargs):
        super(Shellsort, self).__init__(**kwargs)
        self.sort_name = 'Shellsort'

    def sort(self) -> None:
        """Shellsort algorithm."""
        i_list = self.numbers
        length = len(i_list)
        timing = 0
        gap = int(length/2)
        while gap > 0:
            for i in range(gap,length):
                temp = i_list[i]
                j = i
                timing = self.schedule_compare(timing, j, j-gap)
                while j >= gap and i_list[j-gap] > temp:
                    i_list[j] = i_list[j-gap]
                    timing = self.schedule_switch(timing, j, j-gap)
                    j -= gap
                i_list[j] = temp
            gap = int(gap/2)
        self.sorted_numbers = i_list
