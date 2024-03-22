"""Visualizer logic module."""

import random

try:
    from src.configs.generator_config import GeneratorConfig
    from src.sorting.sort_handler import SortHandler
except ImportError as i_err:
    print(i_err)

class Visualizer():
    """Visualizer class."""
    def __init__(self, ids) -> None:
        self.numbers = GeneratorConfig()
        self.ids = ids
        self.sort_name = "Bubblesort"
        self.sort_obj = None
        self.comp_id = 0
        self.switch_id = 0
        self.ids["sort_spinner"].bind(text=self.change_sort)

    def fill_spinner(self) -> None:
        """Fill sort spinner values with sort choices."""
        self.ids["sort_spinner"].values = SortHandler.available_sorts()

    def change_sort(self, _widget, text: str) -> None:
        """Change sort type."""
        self.sort_name = text
        self.load()

    def load(self):
        """Generate random number."""
        numbers = []
        for _i in range(self.numbers.numbers_length):
            numbers.append(random.randint(self.numbers.numbers_lower_limit,
                                          self.numbers.numbers_upper_limit))

        self.ids["bars"].numbers = numbers
        self.ids["bars"].clear_bars()
        self.ids["bars"].build_bars()

        self.sort_obj = SortHandler.get_sort(sort=self.sort_name,
                                             numbers=numbers,
                                             bars=self.ids["bars"].bars,
                                             static_x=self.ids["bars"].static_x)

        self.ids["bars"].sort_obj = self.sort_obj
        self.ids["sort_spinner"].text = self.sort_obj.sort_name

    def start(self):
        """Start sorting animation."""
        self.call_sort()

    def call_sort(self):
        """Call selected sorting class."""
        if not self.sort_obj.events:
            self.sort_obj.sort()
            return

        self.correct_zero()
        self.correct_indexes()

        ident = self.sort_obj.compare_counter + self.sort_obj.switch_counter
        for i in range(ident, len(self.sort_obj.events)):
            timeout = self.sort_obj.event_times[i] - self.sort_obj.event_times[ident]
            self.sort_obj.events[i].timeout = timeout
            self.sort_obj.events[i]()

    def stop(self):
        """Stop animation."""
        if not self.sort_obj:
            return
        for event in self.sort_obj.events:
            event.cancel()
        self.comp_id = self.sort_obj.compare_counter
        self.switch_id = self.sort_obj.switch_counter

    def correct_zero(self) -> None:
        """Correct indexex when previous step would hit index 0."""
        if self.comp_id <= 0 or self.sort_obj.compare_counter < 0:
            self.sort_obj.compare_counter = 0
        if self.switch_id <= 0 or self.sort_obj.switch_counter < 0:
            self.sort_obj.switch_counter = 0

    def correct_indexes(self) -> None:
        """Sync local and object counters."""
        if self.comp_id != self.sort_obj.compare_counter:
            self.sort_obj.compare_counter -= 1
        if self.switch_id != self.sort_obj.switch_counter:
            self.sort_obj.switch_counter -= 1

    def previous(self):
        """Go to previous animation step."""
        if not self.sort_obj:
            return

        if not self.sort_obj.events:
            return

        self.correct_zero()

        index = self.comp_id + self.switch_id - 1
        if index < 0:
            return
        event = self.sort_obj.events[index]
        name = event.weak_callback.method_name
        if name == "switch_bars":
            if self.switch_id < 0:
                return
            self.sort_obj.switch_counter = self.switch_id - 1
            event.timeout = 0.1
            event()
            self.switch_id -= 1
        elif name == "highlight_bars":
            if self.comp_id < 0:
                return
            self.sort_obj.compare_counter = self.comp_id - 1
            event.timeout = 0.1
            event()
            self.comp_id -= 1

    def next(self):
        """Go to next animation step."""
        if not self.sort_obj:
            return

        if not self.sort_obj.events:
            return

        self.correct_zero()
        self.correct_indexes()

        index = self.sort_obj.compare_counter + self.sort_obj.switch_counter
        if index >= len(self.sort_obj.events):
            return
        event = self.sort_obj.events[index]
        event.timeout = 0.1
        event()
        name = event.weak_callback.method_name
        if name == "switch_bars":
            self.comp_id = self.sort_obj.compare_counter
            self.switch_id = self.sort_obj.switch_counter + 1
        elif name == "highlight_bars":
            self.comp_id = self.sort_obj.compare_counter + 1
            self.switch_id = self.sort_obj.switch_counter
