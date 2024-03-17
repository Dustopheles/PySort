"""Minsort module."""

from src.sorting.sort import Sort


class Minsort(Sort):
    """Minsort class."""
    # pylint: disable=all
    def __init__(self, **kwargs):
        super(Minsort, self).__init__(**kwargs)
        self.sort_name = 'Minsort'    

    def sort(self) -> None:
        """Minsort algorithm."""
        i_list = self.numbers
        length = len(i_list)
        for k in range(1, length):
            MinPos = k-1
            for i in range(k, length):
                self.schedule_event("compare", i, MinPos)
                if i_list[i] < i_list[MinPos]:
                    MinPos = i
            i_list[k-1], i_list[MinPos] = i_list[MinPos], i_list[k-1]
            self.schedule_event("switch", k-1, MinPos)
        self.sorted_numbers = i_list
