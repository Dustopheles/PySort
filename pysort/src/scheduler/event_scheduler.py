"""Event scheduler module."""

from kivy.animation import Animation
from kivy.clock import Clock

try:
    from src.configs.color_config import ColorConfig
    from src.configs.animation_config import AnimationConfig
    from src.util.decorators import singleton
    from src.scheduler.operation import Operation
except ImportError as e:
    raise e


@singleton
class EventScheduler():
    """Event scheduler class used to schedule events as operations with kivy Clock."""
    colors = ColorConfig()
    durations = AnimationConfig()
    bar_chart: object
    bars: list[object]

    def __init__(self):
        self.loop_counter = 0
        self.next_timeout = 0
        self.operations = []
        self.stopper = 0

    def clear_scheduler(self) -> None:
        """Reset singleton values to fallback."""
        self.loop_counter = 0
        self.next_timeout = 0
        self.operations = []
        self.stopper = 0

    def schedule_event(self, operation: str, index_a: int, index_b: int) -> None:
        """Schedule event of type x on event scheduler and create operation object.
        - compare - Compare two values
        - switch - Switch two values

        Args:
            operation (str): Type of operation
            index_a (int): list index a
            index_b (int): list index b
        """
        self._add_operation(operation, index_a, index_b)
        if operation == "compare":
            self.schedule_compare()
        elif operation == "switch":
            self.schedule_switch()

    def _add_operation(self, operation: str, index_a: int, index_b: int) -> None:
        """Create operation and add to operation list.

        Args:
            operation (str): Type of operation
            index_a (int): list index a
            index_b (int): list index b
        """
        op_object = Operation(operation=operation, timeout=self.next_timeout)
        op_object.index_pair = (index_a, index_b)

        if not self.operations:
            numbers = []
            for widget in self.bars:
                numbers.append(int(widget.text))
            op_object.numbers_before = numbers
        else:
            numbers = self.operations[-1].numbers_after().copy()
            op_object.numbers_before = numbers

        self.operations.append(op_object)

    def schedule_compare(self) -> None:
        """Schedule compare event on time x.
        - Set next possible event time."""
        event = Clock.create_trigger(self.compare_event, self.next_timeout)
        curr_object = self.operations[-1]
        curr_object.event = event
        self.next_timeout += (self.durations.duration_compare +
                              self.durations.duration_pause +
                              0.0001)

    def schedule_switch(self) -> None:
        """Schedule switch event on time x.
        - Set next possible event time."""
        event = Clock.create_trigger(self.switch_event, self.next_timeout)
        curr_object = self.operations[-1]
        curr_object.event = event
        self.next_timeout += (self.durations.duration_switch +
                              self.durations.duration_pause +
                              0.0001)

    def compare_event(self, _timing) -> None:
        """Highlight selected bars."""
        if self.loop_counter >= len(self.operations):
            return
        index_a, index_b = self.operations[self.loop_counter].index_pair
        widget_a = self.bars[index_a]
        widget_b = self.bars[index_b]
        self.compare_animation(widget_a)
        self.compare_animation(widget_b)
        self.loop_counter += 1

    def compare_animation(self, widget) -> None:
        """Create and start compare animation for widget x.

        Args:
            widget (Widget): Widget to animate
        """
        animation = Animation(x=widget.x, y=widget.y,
                              duration=self.durations.duration_compare)
        animation.bind(on_start=self.compare_on_start)
        animation.bind(on_complete=self.compare_on_complete)
        animation.start(widget)

    def compare_on_start(self, _animation, widget) -> None:
        """Change widget state on animation start and reset widget state of previous iteration."""
        self.reset_state()
        widget.state = "compare"

    def compare_on_complete(self, _animation, widget) -> None:
        """Change widget state on animation completion and check if widget position is correct."""
        self.check_position(widget)
        self.check_finished()


    def switch_event(self, _timing) -> None:
        """Start switch event."""
        if self.loop_counter >= len(self.operations):
            return
        index_a, index_b = self.operations[self.loop_counter].index_pair
        widget_a = self.bars[index_a]
        widget_b = self.bars[index_b]
        self.switch_animation(widget_a, widget_b.x)
        self.switch_animation(widget_b, widget_a.x)
        self.adjust_list()
        self.loop_counter += 1

    def switch_animation(self, widget, x: int) -> None:
        """Create and start switch animation for widget x.

        Args:
            widget (Widget): Widget to animate
            x (int): Position x after animation
        """
        animation = Animation(x=x, y=widget.y,
                              duration=self.durations.duration_switch)
        animation.bind(on_start=self.switch_on_start)
        animation.bind(on_complete=self.switch_on_complete)
        animation.start(widget)

    def switch_on_start(self, _animation, widget) -> None:
        """Change widget state on animation start and reset widget state of previous iteration."""
        self.reset_state()
        widget.state = "switch"

    def switch_on_complete(self, _animation, widget) -> None:
        """Change widget state on animation completion and check if widget position is correct."""
        self.check_position(widget)
        self.check_finished()


    def adjust_list(self) -> None:
        """Switch widget position in list after switch."""
        index_a, index_b = self.operations[self.loop_counter].index_pair
        left = self.bars[index_a]
        right = self.bars[index_b]
        self.bars[index_a] = right
        self.bars[index_b] = left

    def reset_state(self):
        """Reset state of widgets."""
        self.stopper += 1
        if self.stopper > 1:
            self.stopper = 0
            return

        for widget in self.bars:
            widget.state = "default"

    def check_finished(self) -> None:
        """Check if final iteration, change state of widgets."""
        self.stopper += 1
        if self.stopper > 1:
            self.stopper = 0
            return

        if self.loop_counter >= len(self.operations):
            for widget in self.bars:
                widget.state = "sorted"

    def check_position(self, widget) -> None:
        """Check if widget x is correct, adjust if not."""
        if widget not in self.bars:
            return
        index = self.bars.index(widget)
        if widget.x != self.bar_chart.ref_x[index]:
            widget.x = self.bar_chart.ref_x[index]
