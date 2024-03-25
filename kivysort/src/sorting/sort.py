"""Sort base module."""

try:
    from src.util.event_scheduler import EventScheduler
except ImportError as i_err:
    print(i_err)


class Sort():
    """Sort base class."""
    scheduler = EventScheduler()
    def __init__(self, **kwargs):
        self.numbers = kwargs['numbers']
        self.sorted_numbers = []
        self.name = ""

    def start_sort(self):
        """Wrapper for sort method."""
        self.sorted_numbers = self.sort(self.numbers)

    def sort(self, numbers: list) -> list:
        """Abstract sorting method."""
        return numbers

    def schedule_event(self, operation: str, index_a: int, index_b: int) -> None:
        """Schedule event of type x on event scheduler.
        - compare - Compare two values
        - switch - Switch two values"""
        self.scheduler.schedule_event(operation, index_a, index_b)
