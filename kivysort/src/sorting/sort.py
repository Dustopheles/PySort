"""Sort base module."""

from kivy.animation import Animation
from kivy.clock import Clock

from src.bar_widget import Bar
from src.config import bar_dict as BAR
from src.config import animation_dict as ANIM


class Sort():
    """Sort base class."""
    def __init__(self, **kwargs):
        self.ids = kwargs['ids']
        # Ordered bar widget list
        self.bars = kwargs['bars']
        self.global_x = kwargs['static_x']
        # Numbers to sort
        self.numbers = kwargs['numbers']
        self.sorted_numbers = []
        # List of compares
        self.pairs = []
        self.loop_counter = 0
        # List of switches
        self.switches = []
        self.switch_counter = 0
        # List of all Events
        self.events = []
        self.sort_name = ''

    def sort(self):
        """Sort method."""

    def schedule_compare(self, time: float,
                         i_left: int, i_right: int) -> float:
        """Schedule compare event on time x.
        - Return next possible event time."""
        self.pairs.append((i_left, i_right))
        self.events.append(Clock.schedule_once(self.highlight_bars, time))
        time += ANIM["compare_duration"] + ANIM["pause_duration"]
        return time

    def schedule_switch(self, time: float, i_left: int, i_right: int) -> float:
        """Schedule compare event on time x.
        - Return next possible event time."""
        self.switches.append((i_left, i_right))
        self.events.append(Clock.schedule_once(self.switch_bars, time))
        time += ANIM["switch_duration"] + ANIM["pause_duration"]
        return time

    def check_finished(self, widget: Bar) -> None:
        """Check if bar is in final place and color if."""
        index = self.bars.index(widget)
        if int(widget.text) == self.sorted_numbers[index]:
            widget.redraw_rectangle(rgba=BAR['color_sorted'])

    def check_position(self, widget: Bar) -> None:
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

    def highlight(self, widget: Bar) -> Animation:
        """Highlighting animation."""
        animation = Animation(x=widget.x, y=widget.y,
                              duration=ANIM["compare_duration"])
        animation.bind(on_start=self.highlight_on_start)
        animation.bind(on_complete=self.highlight_on_complete)
        animation.start(widget)
        return animation

    def highlight_on_start(self, _animation, widget: Bar) -> None:
        """Switch color on animation start."""
        widget.redraw_rectangle(rgba=BAR['color_active'])

    def highlight_on_complete(self, _animation, widget: Bar) -> None:
        """Reset color after animation completion."""
        self.check_position(widget)
        widget.redraw_rectangle(rgba=BAR['color_passive'])
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

    def switch(self, widget: Bar, x: int) -> Animation:
        """Switch animation."""
        animation = Animation(x=x, y=widget.y,
                              duration=ANIM["switch_duration"])
        animation.bind(on_start=self.switch_on_start)
        animation.bind(on_complete=self.switch_on_complete)
        animation.start(widget)
        return animation

    def switch_on_start(self, _animation, widget: Bar) -> None:
        """Reactivate start bttn after finishing animation."""
        widget.redraw_rectangle(rgba=BAR['color_switch'])
        if self.switch_counter == 0:
            self.ids.start_bttn.disabled = True

    def switch_on_complete(self, _animation, widget: Bar) -> None:
        """Reactivate start bttn after finishing animation."""
        self.check_position(widget)
        widget.redraw_rectangle(rgba=BAR['color_passive'])
        if self.switch_counter >= len(self.switches):
            self.ids.start_bttn.disabled = False
        self.check_finished(widget)
