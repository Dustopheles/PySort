"""Visualizer logic module."""

import random

from kivy.clock import Clock

try:
    from src.configs.generator_config import GeneratorConfig
    from src.configs.animation_config import AnimationConfig
    from src.util.sort_handler import SortHandler
    from src.util.event_scheduler import EventScheduler
except ImportError as i_err:
    print(i_err)

class Visualizer():
    """Visualizer class."""
    numbers = GeneratorConfig()
    durations = AnimationConfig()
    schedular = EventScheduler()
    def __init__(self, ids) -> None:
        self.ids = ids
        self.sort_name = "Bubblesort"
        self.sort_obj = None
        self.loop_id = 0
        self.ids["sort_spinner"].bind(text=self.change_sort)

    def fill_spinner(self) -> None:
        """Fill sort spinner values with sort choices."""
        self.ids["sort_spinner"].values = SortHandler.available_sorts()

    def change_sort(self, _widget, text: str) -> None:
        """Change sort type."""
        self.sort_name = text
        self.load()

    def load(self) -> None:
        """Generate random number."""
        numbers = []
        for _i in range(self.numbers.numbers_length):
            numbers.append(random.randint(self.numbers.numbers_lower_limit,
                                          self.numbers.numbers_upper_limit))

        self.ids["bars"].numbers = numbers
        self.ids["bars"].clear_bars()
        self.ids["bars"].build_bars()

        self.schedular.clear_scheduler()
        self.schedular.bar_layout = self.ids["bars"]
        self.sort_obj = SortHandler.get_sort(sort=self.sort_name,
                                             numbers=numbers,)


        self.ids["sort_spinner"].text = self.sort_obj.sort_name

    def start(self) -> None:
        """Start sorting animation."""
        self.call_sort()
        #self.ids["bars"].freeze = True

    def call_sort(self) -> None:
        """Call selected sorting class."""
        if not self.schedular.operations:
            self.sort_obj.sort()
            return

        self.correct_zero()
        self.correct_indexes()

        ident = self.schedular.loop_counter
        for i in range(ident, len(self.schedular.operations)):
            timeout = (self.schedular.operations[i].timeout -
                       self.schedular.operations[ident].timeout)
            self.schedular.operations[i].event.timeout = timeout
            self.schedular.operations[i].event()

    def stop(self) -> None:
        """Stop animation."""
        if not self.sort_obj:
            return
        for operation in self.schedular.operations:
            operation.event.cancel()
        self.loop_id = self.schedular.loop_counter
        #self.ids["bars"].freeze = False

    def correct_zero(self) -> None:
        """Correct indexex when previous step would hit index 0."""
        if self.loop_id <= 0 or self.schedular.loop_counter < 0:
            self.schedular.loop_counter = 0

    def correct_indexes(self) -> None:
        """Sync local and object counters."""
        if self.loop_id != self.schedular.loop_counter:
            self.schedular.loop_counter -= 1

    def previous(self) -> None:
        """Go to previous animation step."""
        if not self.sort_obj:
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
        Clock.schedule_once(self.enable_manuel, timeout)

    def next(self) -> None:
        """Go to next animation step."""
        if not self.sort_obj:
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
        Clock.schedule_once(self.enable_manuel, timeout)

    def get_timeout(self, operation: str) -> float:
        """Get timeout for animation."""
        timout = 0.1
        if operation == "switch":
            timout = self.durations.duration_switch + self.durations.duration_pause
        else:
            timout = self.durations.duration_compare + self.durations.duration_pause
        return timout

    def enable_manuel(self, *_args) -> None:
        """Enabel manuel controls."""
        self.ids['next_bttn'].disabled = False
        self.ids['previous_bttn'].disabled = False
