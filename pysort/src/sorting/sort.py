"""Sort base module."""

try:
    from src.scheduler.event_scheduler import EventScheduler
except ImportError as e:
    raise e


class Sort():
    """Sort base parent class."""
    scheduler = EventScheduler()

    def __init__(self, **kwargs):
        self.numbers = kwargs['numbers']
        self.sorted_numbers = []
        self.name = ""

    def start_sort(self) -> None:
        """Wrapper for sort method to return sorted numbers."""
        self.sorted_numbers = self.sort(self.numbers)

    def sort(self, numbers: list[int]) -> list[int]:
        """Abstract sorting method.

        Args:
            numbers (list[int]): Integer list

        Returns:
            list[int]: Sorted integer list
        """
        return numbers

    def schedule_event(self, operation: str, index_a: int, index_b: int) -> None:
        """Schedule event of type x on event scheduler.
        - compare - Compare two values
        - switch - Switch two values

        Args:
            operation (str): compare or switch
            index_a (int): list index a
            index_b (int): list index b
        """
        self.scheduler.schedule_event(operation, index_a, index_b)
