"""Event scheduler module."""

from kivy.animation import Animation
from kivy.clock import Clock

try:
    from src.widgets.bar_widget import BarWidget
    from src.configs.color_config import ColorConfig
    from src.configs.animation_config import AnimationConfig
    from src.util.decorators import singleton
    from src.util.operation import Operation
except ImportError as i_err:
    print(i_err)

@singleton
class EventScheduler():
    """Event scheduler class used to schedule events with event clock."""
    def __init__(self):
        # Configs
        self.colors = ColorConfig()
        self.durations = AnimationConfig()
        # Barlayout
        self.bar_layout = None
        # Indexer
        self.loop_counter = 0
        self.next_timeout = 0
        self.operations = []

    def clear_scheduler(self) -> None:
        """Reset singleton"""
        self.loop_counter = 0
        self.next_timeout = 0
        self.operations = []

    def schedule_event(self, operation: str, index_a: int, index_b: int) -> None:
        """Schedule event of type x on event scheduler.
        - compare - Compare two values
        - switch - Switch two values"""
        self.operations.append(Operation(operation=operation,
                                         timeout=self.next_timeout,
                                         index_pair=(index_a, index_b),
                                         widgets=self.bar_layout.bars))
        if operation == "compare":
            self.schedule_compare()
        elif operation == "switch":
            self.schedule_switch()

    def schedule_compare(self) -> None:
        """Schedule compare event on time x.
        - Return next possible event time."""
        event = Clock.schedule_once(self.highlight_bars, self.next_timeout)
        curr_object = self.operations[-1]
        curr_object.event = event
        self.next_timeout += (self.durations.duration_compare +
                              self.durations.duration_pause +
                              0.0001)

    def schedule_switch(self) -> None:
        """Schedule compare event on time x.
        - Return next possible event time."""
        event = Clock.schedule_once(self.switch_bars, self.next_timeout)
        curr_object = self.operations[-1]
        curr_object.event = event
        self.next_timeout += (self.durations.duration_switch +
                              self.durations.duration_pause +
                              0.0001)

    def check_finished(self, widget: BarWidget) -> None:
        """Check if bar is in final place and color if."""
        if self.loop_counter >= len(self.operations)-1:
            for widget in self.bar_layout.bars:
                widget.redraw_rectangle(rgba=self.colors.color_sorted)

    def check_position(self, widget: BarWidget) -> None:
        """Check if bar is on right x."""
        index = self.bar_layout.bars.index(widget)
        if widget.x != self.bar_layout.ref_x[index]:
            widget.x = self.bar_layout.ref_x[index]

    def highlight_bars(self, _timing) -> None:
        """Highlight selected bars."""
        if self.loop_counter >= len(self.operations):
            return
        widget_a, widget_b = self.operations[self.loop_counter].widget_pair()
        self.highlight(widget_a)
        self.highlight(widget_b)
        self.loop_counter += 1

    def highlight(self, widget: BarWidget) -> Animation:
        """Highlighting animation."""
        animation = Animation(x=widget.x, y=widget.y,
                              duration=self.durations.duration_compare,
                              s=1/30)
        animation.bind(on_start=self.highlight_on_start)
        animation.bind(on_complete=self.highlight_on_complete)
        animation.start(widget)
        return animation

    def highlight_on_start(self, _animation, widget: BarWidget) -> None:
        """Switch color on animation start."""
        self.reset_colors()
        widget.redraw_rectangle(rgba=self.colors.color_active)

    def highlight_on_complete(self, _animation, widget: BarWidget) -> None:
        """Reset color after animation completion."""
        self.check_position(widget)
        self.check_finished(widget)

    def switch_bars(self, _timing) -> None:
        """Switch two bars."""
        if self.loop_counter >= len(self.operations):
            return
        widget_a, widget_b = self.operations[self.loop_counter].widget_pair()
        self.switch(widget_a, widget_b.x)
        self.switch(widget_b, widget_a.x)
        self.adjust_list()

    def adjust_list(self) -> None:
        """Adjust bar widget list to new position."""
        index_a, index_b = self.operations[self.loop_counter].index_pair
        left = self.bar_layout.bars[index_a]
        right = self.bar_layout.bars[index_b]
        self.bar_layout.bars[index_a] = right
        self.bar_layout.bars[index_b] = left
        self.loop_counter += 1

    def switch(self, widget: BarWidget, x: int) -> Animation:
        """Switch animation."""
        animation = Animation(x=x, y=widget.y,
                              duration=self.durations.duration_switch,
                              s=1/30)
        animation.bind(on_start=self.switch_on_start)
        animation.bind(on_complete=self.switch_on_complete)
        animation.start(widget)
        return animation

    def reset_colors(self):
        """Reset widgets colors back to passive."""
        current = self.operations[self.loop_counter].widget_pair()
        for widget in self.bar_layout.bars:
            if widget not in current:
                widget.redraw_rectangle(rgba=self.colors.color_passive)

    def switch_on_start(self, _animation, widget: BarWidget) -> None:
        """Reactivate start bttn after finishing animation."""
        self.reset_colors()
        widget.redraw_rectangle(rgba=self.colors.color_switch)

    def switch_on_complete(self, _animation, widget: BarWidget) -> None:
        """Reactivate start bttn after finishing animation."""
        self.check_position(widget)
        self.check_finished(widget)
