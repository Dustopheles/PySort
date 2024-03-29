"""Event scheduler module."""

from kivy.animation import Animation
from kivy.clock import Clock

# pylint: disable=no-name-in-module
# pylint: disable=import-error
from src.configs.color_config import ColorConfig
from src.configs.animation_config import AnimationConfig
from src.util.decorators import singleton
from src.util.operation import Operation


@singleton
class EventScheduler():
    """Event scheduler class used to schedule events with event clock."""
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
        """Reset singleton"""
        self.loop_counter = 0
        self.next_timeout = 0
        self.operations = []
        self.stopper = 0

    def schedule_event(self, operation: str, index_a: int, index_b: int) -> None:
        """Schedule event of type x on event scheduler.
        - compare - Compare two values
        - switch - Switch two values"""
        self.add_operation(operation, index_a, index_b)
        if operation == "compare":
            self.schedule_compare()
        elif operation == "switch":
            self.schedule_switch()

    def add_operation(self, operation: str, index_a: int, index_b: int) -> None:
        """Add operation to operation list."""
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
        - Return next possible event time."""
        event = Clock.create_trigger(self.highlight_bars, self.next_timeout)
        curr_object = self.operations[-1]
        curr_object.event = event
        self.next_timeout += (self.durations.duration_compare +
                              self.durations.duration_pause +
                              0.0001)

    def schedule_switch(self) -> None:
        """Schedule compare event on time x.
        - Return next possible event time."""
        event = Clock.create_trigger(self.switch_bars, self.next_timeout)
        curr_object = self.operations[-1]
        curr_object.event = event
        self.next_timeout += (self.durations.duration_switch +
                              self.durations.duration_pause +
                              0.0001)

    def check_finished(self, _widget) -> None:
        """Check if bar is in final place and color if."""
        self.stopper += 1
        if self.stopper > 1:
            self.stopper = 0
            return

        if self.loop_counter >= len(self.operations):
            for widget in self.bars:
                widget.state = "sorted"

    def check_position(self, widget) -> None:
        """Check if bar is on right x."""
        index = self.bars.index(widget)
        if widget.x != self.bar_chart.ref_x[index]:
            widget.x = self.bar_chart.ref_x[index]

    def highlight_bars(self, _timing) -> None:
        """Highlight selected bars."""
        if self.loop_counter >= len(self.operations):
            return
        index_a, index_b = self.operations[self.loop_counter].index_pair
        widget_a = self.bars[index_a]
        widget_b = self.bars[index_b]
        self.highlight(widget_a)
        self.highlight(widget_b)
        self.loop_counter += 1

    def highlight(self, widget) -> Animation:
        """Highlighting animation."""
        animation = Animation(x=widget.x, y=widget.y,
                              duration=self.durations.duration_compare)
        animation.bind(on_start=self.highlight_on_start)
        animation.bind(on_complete=self.highlight_on_complete)
        animation.start(widget)
        return animation

    def highlight_on_start(self, _animation, widget) -> None:
        """Switch color on animation start."""
        self.reset_colors()
        widget.state = "compare"

    def highlight_on_complete(self, _animation, widget) -> None:
        """Reset color after animation completion."""
        self.check_position(widget)
        self.check_finished(widget)

    def switch_bars(self, _timing) -> None:
        """Switch two bars."""
        if self.loop_counter >= len(self.operations):
            return
        index_a, index_b = self.operations[self.loop_counter].index_pair
        widget_a = self.bars[index_a]
        widget_b = self.bars[index_b]
        self.switch(widget_a, widget_b.x)
        self.switch(widget_b, widget_a.x)
        self.adjust_list()

    def adjust_list(self) -> None:
        """Adjust bar widget list to new position."""
        index_a, index_b = self.operations[self.loop_counter].index_pair
        left = self.bars[index_a]
        right = self.bars[index_b]
        self.bars[index_a] = right
        self.bars[index_b] = left
        self.loop_counter += 1

    def switch(self, widget, x: int) -> Animation:
        """Switch animation."""
        animation = Animation(x=x, y=widget.y,
                              duration=self.durations.duration_switch)
        animation.bind(on_start=self.switch_on_start)
        animation.bind(on_complete=self.switch_on_complete)
        animation.start(widget)
        return animation

    def reset_colors(self):
        """Reset widgets colors back to passive."""
        self.stopper += 1
        if self.stopper > 1:
            self.stopper = 0
            return

        for widget in self.bars:
            widget.state = "default"

    def switch_on_start(self, _animation, widget) -> None:
        """Reactivate start bttn after finishing animation."""
        self.reset_colors()
        widget.state = "switch"

    def switch_on_complete(self, _animation, widget) -> None:
        """Reactivate start bttn after finishing animation."""
        self.check_position(widget)
        self.check_finished(widget)
