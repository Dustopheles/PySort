"""Bubblesort module."""

from src.sorting.sort import Sort


class Bubblesort(Sort):
    """Bubblesort class."""
    # pylint: disable=all
    def __init__(self, **kwargs):
        super(Bubblesort, self).__init__(**kwargs)
        self.sort_name = 'Bubblesort'

    def sort(self) -> None:
        """Bubble sort algorithm."""
        i_list = self.numbers
        timing = 0
        for i in range(len(i_list)-1):
            for j in range(len(i_list)-1-i):
                timing = self.schedule_compare(timing, j, j+1)
                if i_list[j] > i_list[j+1]:
                    tmp = i_list[j]
                    i_list[j] = i_list[j+1]
                    i_list[j+1] = tmp
                    timing = self.schedule_switch(timing, j, j+1)
        self.sorted_numbers = i_list
