"""Sort base module."""

try:
    from src.util.event_scheduler import EventScheduler
except ImportError as i_err:
    print(i_err)


class Sort():
    """Sort base class."""
    def __init__(self, **kwargs):
        self.numbers = kwargs['numbers']
        self.scheduler = EventScheduler()

    def sort(self):
        """Abstract sorting method."""

    def schedule_event(self, operation: str, index_a: int, index_b: int) -> None:
        """Schedule event of type x on event scheduler.
        - compare - Compare two values
        - switch - Switch two values"""
        self.scheduler.schedule_event(operation, index_a, index_b)
