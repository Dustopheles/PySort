"""Visualizer logic module."""

import random

from kivy.clock import Clock

try:
    from src.configs.generator_config import GeneratorConfig
    from src.configs.animation_config import AnimationConfig
    from src.util.sort_handler import SortHandler
    from src.util.event_scheduler import EventScheduler
    from src.util.decorators import singleton
    from src.util.context import Context
except ImportError as i_err:
    print(i_err)


@singleton
class VisualizerViewModel():
    """Visualizer class."""
    numbers = GeneratorConfig()
    durations = AnimationConfig()
    schedular = EventScheduler()
    context = Context()
    sort: object

    def __init__(self, ids) -> None:
        self.ids = ids
        self.loop_id = 0
        self.on_init()

    def on_init(self) -> None:
        """Bind properties on load."""
        self.ids["load_bttn"].bind(on_press=self.load)
        self.ids["start_bttn"].bind(on_press=self.start)
        self.ids["stop_bttn"].bind(on_press=self.stop)
        self.ids["previous_bttn"].bind(on_press=self.previous)
        self.ids["next_bttn"].bind(on_press=self.next)
        self.ids["sort_spinner"].values = SortHandler.available_sorts()
        self.ids["sort_spinner"].bind(text=self.change_sort)

    def change_sort(self, _widget, _text) -> None:
        """Change sort type."""
        self.load()

    def load(self, *_args) -> None:
        """Generate random number."""
        self.context.in_progress = False
        self.enable_widgets('start_bttn', 'stop_bttn',
                            'next_bttn', 'previous_bttn')
        numbers = []
        for _i in range(self.numbers.numbers_length):
            numbers.append(random.randint(self.numbers.numbers_lower_limit,
                                          self.numbers.numbers_upper_limit))

        self.ids["bars"].numbers = numbers
        self.ids["bars"].clear_bars()
        self.ids["bars"].build_bars()

        self.schedular.clear_scheduler()
        self.schedular.bar_layout = self.ids["bars"]
        sort_name = self.ids["sort_spinner"].text
        self.sort = SortHandler.get_sort(sort=sort_name, numbers=numbers,)

    def start(self, *_args) -> None:
        """Start sorting animation."""
        self.context.in_progress = True
        self.disable_widgets('start_bttn',
                             'next_bttn', 'previous_bttn')
        self.call_sort()

    def call_sort(self, *_args) -> None:
        """Call selected sorting class."""
        if not self.schedular.operations:
            self.sort.start_sort()
            return

        self.correct_zero()
        self.correct_indexes()

        ident = self.schedular.loop_counter
        for i in range(ident, len(self.schedular.operations)):
            timeout = (self.schedular.operations[i].timeout -
                       self.schedular.operations[ident].timeout)
            self.schedular.operations[i].event.timeout = timeout
            self.schedular.operations[i].event()

    def stop(self, *_args) -> None:
        """Stop animation."""
        self.enable_widgets('start_bttn',
                            'next_bttn', 'previous_bttn')
        if not self.sort:
            return
        for operation in self.schedular.operations:
            operation.event.cancel()
        self.loop_id = self.schedular.loop_counter

    def correct_zero(self) -> None:
        """Correct indexex when previous step would hit index 0."""
        if self.loop_id <= 0 or self.schedular.loop_counter < 0:
            self.schedular.loop_counter = 0

    def correct_indexes(self) -> None:
        """Sync local and object counters."""
        if self.loop_id != self.schedular.loop_counter:
            self.schedular.loop_counter -= 1

    def previous(self, *_args) -> None:
        """Go to previous animation step."""
        if not self.sort:
            return

        if not self.schedular.operations:
            return

        self.correct_zero()

        index = self.loop_id - 1
        if index < 0:
            return
        event = self.schedular.operations[index].event
        if self.loop_id < 0:
            return

        self.ids['next_bttn'].disabled = True
        self.ids['previous_bttn'].disabled = True

        self.schedular.loop_counter = self.loop_id - 1
        event.timeout = 0.1
        event()
        self.loop_id -= 1
        timeout = self.get_timeout(self.schedular.operations[self.schedular.loop_counter-1])
        Clock.schedule_once(self.enable_controls, timeout)

    def next(self, *_args) -> None:
        """Go to next animation step."""
        if not self.sort:
            return

        if not self.schedular.operations:
            return

        self.correct_zero()
        self.correct_indexes()

        index = self.schedular.loop_counter
        if index >= len(self.schedular.operations):
            return

        self.ids['next_bttn'].disabled = True
        self.ids['previous_bttn'].disabled = True

        event = self.schedular.operations[index].event
        event.timeout = 0.1
        event()
        self.loop_id = self.schedular.loop_counter + 1
        timeout = self.get_timeout(self.schedular.operations[self.schedular.loop_counter])
        Clock.schedule_once(self.enable_controls, timeout)

    def get_timeout(self, operation: str) -> float:
        """Get timeout for animation."""
        timout = 0.1
        if operation == "switch":
            timout = self.durations.duration_switch + self.durations.duration_pause
        else:
            timout = self.durations.duration_compare + self.durations.duration_pause
        return timout

    def enable_controls(self, *_args) -> None:
        """Enabel manuel controls."""
        self.ids['next_bttn'].disabled = False
        self.ids['previous_bttn'].disabled = False

    def disable_widgets(self, *args):
        """Disable list of widgets."""
        for ident in args:
            self.ids[ident].disabled = True

    def enable_widgets(self, *args):
        """Enable list of widgets."""
        for ident in args:
            self.ids[ident].disabled = False
