"""Bubblesort module."""

from src.sorting.sort import Sort


class Bubblesort(Sort):
    """Bubblesort class."""
    # pylint: disable=all
    def __init__(self, **kwargs):
        super(Bubblesort, self).__init__(**kwargs)
        self.sort_name = 'Bubblesort'

    def sort(self) -> None:
        """Bubblesort algorithm."""
        i_list = self.numbers
        length = len(i_list)
        for i in range(length-1):
            for j in range(length-1-i):
                self.schedule_event("compare", j, j+1)
                if i_list[j] > i_list[j+1]:
                    tmp = i_list[j]
                    i_list[j] = i_list[j+1]
                    i_list[j+1] = tmp
                    self.schedule_event("switch", j, j+1)
        self.sorted_numbers = i_list
