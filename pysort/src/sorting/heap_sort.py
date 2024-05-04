"""Heapsort module."""

try:
    from src.sorting.sort import Sort
except ImportError as e:
    raise e


class Heapsort(Sort):
    """Heapsort class."""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = 'Heapsort'
        self.array = []

    def sort(self, numbers: list) -> list:
        """Heapsort algorithm."""
        self.array = numbers
        self.heap(self.array)
        return self.array

    def heapify(self, arr, n, i):
        """Sub heap."""
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2

        if l < n and arr[largest] < arr[l]:
            largest = l

        if r < n and arr[largest] < arr[r]:
            largest = r

        self.schedule_event("compare", largest, i)
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            self.schedule_event("switch", i, largest)
            self.heapify(arr, n, largest)

    def heap(self, arr):
        """Heap."""
        n = len(arr)

        for i in range(n//2 - 1, -1, -1):
            self.heapify(arr, n, i)

        for i in range(n-1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]
            self.schedule_event("switch", i, 0)
            self.heapify(arr, i, 0)
