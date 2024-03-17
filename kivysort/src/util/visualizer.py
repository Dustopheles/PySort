"""Visualizer logic module."""

import random
import gc

from kivy.uix.togglebutton import ToggleButton

try:
    from src.configs.generator_config import GeneratorConfig as Generator
    from src.sorting.sort_handler import SortHandler
except ImportError as e:
    print(e)

class Visualizer():
    """Visualizer class."""
    def __init__(self, ids) -> None:
        self.ids = ids
        self.sort_name = "Bubblesort"
        self.sort_obj = None

    def fill_grid(self) -> None:
        """Fill choice grid with choices."""
        for choice in SortHandler.available_sorts():
            bttn = ToggleButton(text=choice, size_hint=(None, None),
                                height=50, width=200, group='sort')
            # pylint: disable=no-member
            bttn.bind(on_press=self.change_sort)
            self.ids['choice_grid'].add_widget(bttn)

    def change_sort(self, widget) -> None:
        """Change sort type."""
        self.sort_name = widget.text

    def load(self):
        """Generate random number."""
        self.clear_workspace()
        numbers = []
        for _i in range(Generator.members):
            numbers.append(random.randint(Generator.lower_limit,
                                          Generator.upper_limit))

        self.ids["bars"].numbers = numbers
        self.ids["bars"].clear_bars()
        self.ids["bars"].build_bars()
        self.ids['start_bttn'].disabled = False
        self.ids['stop_bttn'].disabled = False
        self.ids['next_bttn'].disabled = False
        self.ids['previous_bttn'].disabled = False
        self.ids['save_bttn'].disabled = False
        self.ids['reset_bttn'].disabled = False
        self.sort_obj = SortHandler.get_sort(sort=self.sort_name,
                                             numbers=numbers,
                                             bars=self.ids["bars"].bars,
                                             static_x=self.ids["bars"].static_x)
        self.ids["bars"].sort_obj = self.sort_obj
        self.ids['sort_label'].text = self.sort_obj.sort_name

    def clear_workspace(self) -> None:
        """Clear lists and widgets."""
        self.sort_obj = None
        gc.collect()

    def start(self):
        """Start sorting animation."""
        self.ids['next_bttn'].disabled = True
        self.ids['previous_bttn'].disabled = True
        self.ids['start_bttn'].disabled = True
        self.ids['save_bttn'].disabled = True
        self.ids['reset_bttn'].disabled = True
        self.call_sort()

    def call_sort(self):
        """Call selected sorting class."""
        if self.sort_obj.events:
            ident = self.sort_obj.loop_counter + self.sort_obj.switch_counter
            for i in range(ident, len(self.sort_obj.events)-1):
                timeout = self.sort_obj.event_times[i] - self.sort_obj.event_times[ident]
                self.sort_obj.events[i].timeout = timeout
                self.sort_obj.events[i]()
        else:
            self.sort_obj.sort()

    def stop(self):
        """Stop animation."""
        if self.sort_obj:
            for event in self.sort_obj.events:
                event.cancel()
            self.ids.start_bttn.disabled = False
        self.ids['next_bttn'].disabled = False
        self.ids['previous_bttn'].disabled = False
        self.ids['start_bttn'].disabled = False

    def previous(self):
        """Go to previous animation step."""
        if not self.sort_obj:
            return
        index = self.sort_obj.loop_counter + self.sort_obj.switch_counter
        if index <= 0:
            return
        event = self.sort_obj.events[index]
        name = event.weak_callback.method_name
        if name == "switch_bars":
            self.sort_obj.switch_counter -= 1
            event.timeout = 0.1
            event()
        else:
            index = self.sort_obj.loop_counter + self.sort_obj.switch_counter -1
            if index <= 0:
                return
            event = self.sort_obj.events[index]
            name = event.weak_callback.method_name
            self.sort_obj.loop_counter -= 1
            event.timeout = 0.1
            event()

    def next(self):
        """Go to next animation step."""
        if not self.sort_obj:
            return
        index = self.sort_obj.loop_counter + self.sort_obj.switch_counter
        if index >= len(self.sort_obj.events)-1:
            return
        event = self.sort_obj.events[index]
        event.timeout = 0.1
        event()
