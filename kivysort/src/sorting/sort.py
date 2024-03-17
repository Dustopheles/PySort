"""Sort base module."""

from kivy.animation import Animation
from kivy.clock import Clock

try:
    from src.widgets.bar_widget import BarWidget
    from src.configs.color_config import ColorConfig as Colors
    from src.configs.animation_config import AnimationConfig as Durations
    from src.util.operation import Operation
except ImportError as i_err:
    print(i_err)


class Sort():
    """Sort base class."""
    def __init__(self, **kwargs):
        # Bar widgets
        self.bars = kwargs['bars']
        self.global_x = kwargs['static_x']

        # Numbers
        self.numbers = kwargs['numbers']
        self.sorted_numbers = []

        # Compares
        self.pairs = []
        self.loop_counter = 0

        # Switches
        self.switches = []
        self.switch_counter = 0

        # Events
        self.events = []
        self.event_times = []
        self.time = 0

    def sort(self):
        """Sort method."""

    def schedule_event(self, operation: str, i_left: int, i_right: int) -> None:
        """Redirect event to type."""
        if operation == "compare":
            self.schedule_compare(i_left, i_right)
        elif operation == "switch":
            self.schedule_switch(i_left, i_right)

    def schedule_compare(self, i_left: int, i_right: int) -> None:
        """Schedule compare event on time x.
        - Return next possible event time."""
        self.pairs.append((i_left, i_right))
        self.events.append(Clock.schedule_once(self.highlight_bars, self.time))
        self.event_times.append(self.time)
        self.time += Durations.compare + Durations.pause

    def schedule_switch(self, i_left: int, i_right: int) -> None:
        """Schedule compare event on time x.
        - Return next possible event time."""
        self.switches.append((i_left, i_right))
        self.events.append(Clock.schedule_once(self.switch_bars, self.time))
        self.event_times.append(self.time)
        self.time += Durations.switch + Durations.pause

    def check_finished(self, widget: BarWidget) -> None:
        """Check if bar is in final place and color if."""
        index = self.bars.index(widget)
        if int(widget.text) == self.sorted_numbers[index]:
            widget.redraw_rectangle(rgba=Colors.sorted)

    def check_position(self, widget: BarWidget) -> None:
        """Check if bar is on right x."""
        index = self.bars.index(widget)
        if widget.x != self.global_x[index]:
            widget.x = self.global_x[index]

    def highlight_bars(self, _timing) -> None:
        """Highlight selected bars."""
        if self.loop_counter >= len(self.pairs):
            return
        l_bar = self.bars[self.pairs[self.loop_counter][0]]
        r_bar = self.bars[self.pairs[self.loop_counter][1]]
        self.highlight(l_bar)
        self.highlight(r_bar)
        self.loop_counter += 1

    def highlight(self, widget: BarWidget) -> Animation:
        """Highlighting animation."""
        animation = Animation(x=widget.x, y=widget.y,
                              duration=Durations.compare)
        animation.bind(on_start=self.highlight_on_start)
        animation.bind(on_complete=self.highlight_on_complete)
        animation.start(widget)
        return animation

    def highlight_on_start(self, _animation, widget: BarWidget) -> None:
        """Switch color on animation start."""
        widget.redraw_rectangle(rgba=Colors.active)

    def highlight_on_complete(self, _animation, widget: BarWidget) -> None:
        """Reset color after animation completion."""
        self.check_position(widget)
        widget.redraw_rectangle(rgba=Colors.passive)
        self.check_finished(widget)

    def switch_bars(self, _timing) -> None:
        """Switch two bars."""
        if self.switch_counter >= len(self.switches):
            return
        l_bar = self.bars[self.switches[self.switch_counter][0]]
        r_bar = self.bars[self.switches[self.switch_counter][1]]
        self.switch(l_bar, r_bar.x)
        self.switch(r_bar, l_bar.x)
        self.adjust_list()

    def adjust_list(self) -> None:
        """Adjust bar widget list to new position."""
        left = self.bars[self.switches[self.switch_counter][0]]
        right = self.bars[self.switches[self.switch_counter][1]]
        self.bars[self.switches[self.switch_counter][0]] = right
        self.bars[self.switches[self.switch_counter][1]] = left
        self.switch_counter += 1

    def switch(self, widget: BarWidget, x: int) -> Animation:
        """Switch animation."""
        animation = Animation(x=x, y=widget.y,
                              duration=Durations.switch)
        animation.bind(on_start=self.switch_on_start)
        animation.bind(on_complete=self.switch_on_complete)
        animation.start(widget)
        return animation

    def switch_on_start(self, _animation, widget: BarWidget) -> None:
        """Reactivate start bttn after finishing animation."""
        widget.redraw_rectangle(rgba=Colors.switch)

    def switch_on_complete(self, _animation, widget: BarWidget) -> None:
        """Reactivate start bttn after finishing animation."""
        self.check_position(widget)
        widget.redraw_rectangle(rgba=Colors.passive)
        self.check_finished(widget)
