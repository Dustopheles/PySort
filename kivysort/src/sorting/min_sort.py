"""Minsort module."""

from src.sorting.sort import Sort


class Minsort(Sort):
    """Minsort class."""
    # pylint: disable=all
    def __init__(self, **kwargs):
        super(Minsort, self).__init__(**kwargs)
        self.sort_name = 'Minsort'    

    def sort(self) -> None:
        """Min sort algorithm."""
        i_list = self.numbers
        timing = 0
        for k in range(1, len(i_list)):
            MinPos = k-1
            for i in range(k, len(i_list)):
                timing = self.schedule_compare(timing, i, MinPos)
                if i_list[i] < i_list[MinPos]:
                    MinPos = i
            i_list[k-1], i_list[MinPos] = i_list[MinPos], i_list[k-1]
            timing = self.schedule_switch(timing, k-1, MinPos)
        self.sorted_numbers = i_list
