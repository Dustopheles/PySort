"""Main UI Widget for kivy app."""

import random
import gc
import platform

from kivy.uix.tabbedpanel import TabbedPanel
from kivy.uix.button import Button

# from src.bar_layout import BarLayout
from src.bar_widget import Bar
from src.config import settings_dict as SETT
# from src.config import bar_dict as BAR
from src.config import animation_dict as ANIM

# pylint: disable=all
from src.sorting.sort_handler import get_sort, available_sorts


class MainWidget(TabbedPanel):
    """Main widget for window."""
    def __init__(self, **kwargs):
        super(MainWidget, self).__init__(**kwargs)
        # Ordered bar widget list
        self.bars = []
        self.static_x = []
        # Numbers to sort
        self.numbers = []
        self.choices = []
        self.sort_name = "BubbleSort"
        self.sort_obj = None
        self.on_start()

    def on_start(self):
        """Block that is executed at app start."""
        self.ids['platform'].text = f"{platform.system()} {platform.release()}"
        self.ids['py_version'].text = f"Python {platform.python_version()}"
        self.ids['bars'].bind(size=self.resize_bars)
        self.update_entries()
        self.choices = available_sorts()
        self.fill_grid()

    def fill_grid(self) -> None:
        """Fill choice grid with choices."""
        for choice in self.choices:
            bttn = Button(text=choice, size_hint=(None, None),
                          height=50, width=200)
            bttn.bind(on_press=self.change_sort)
            self.ids['choice_grid'].add_widget(bttn)

    def change_sort(self, widget) -> None:
        """Change sort type."""
        self.sort_name = widget.text

    def load(self):
        """Generate random number."""
        self.clear_workspace()
        for _i in range(SETT['members']):
            self.numbers.append(random.randint(SETT['lower_limit'],
                                               SETT['upper_limit']))

        self.build_bars()
        self.ids['start_bttn'].disabled = False
        self.ids['stop_bttn'].disabled = False
        self.ids['next_bttn'].disabled = False
        self.ids['previous_bttn'].disabled = False

    def clear_workspace(self) -> None:
        """Clear lists and widgets."""
        self.static_x.clear()
        self.numbers.clear()
        self.ids.bars.clear_widgets()
        self.bars.clear()
        self.sort_obj = None
        gc.collect()

    def calc_bar_layout(self) -> tuple:
        """Calculate bar layout size."""
        x = 10
        root_width = self.width - len(self.numbers)*5 - x
        width = max(int(root_width/SETT['members']), 1)
        height = self.ids['bars'].height - 80
        max_num = max(self.numbers)
        return width, height, max_num

    def build_bars(self) -> None:
        """Build bars in relation to screen size."""
        x = 10
        width, root_height, max_num = self.calc_bar_layout()
        for number in self.numbers:
            height = root_height*(number/max_num)
            self.static_x.append(x)
            self.bars.append(self.add_bar(width, height, x, number))
            x += width + 5

    def resize_bars(self, *_args):
        """Resize bar widgets."""
        if not self.bars:
            return
        x = 10
        width, root_height, max_num = self.calc_bar_layout()
        for index, widget in enumerate(self.bars):
            widget.height = root_height*(int(widget.text)/max_num)
            widget.width = width
            widget.x = x
            self.static_x[index] = x
            x += width + 5

        if self.sort_obj:
            self.sort_obj.global_x = self.static_x

    def add_bar(self, width: int, height: int, x: int, number: int) -> Bar:
        """Add bar to parent widget."""
        bar_widget = Bar(x=x, height=height, width=width, text=str(number))
        self.ids['bars'].add_widget(bar_widget)
        return bar_widget

    def start(self):
        """Start sorting animation."""
        self.ids['next_bttn'].disabled = True
        self.ids['previous_bttn'].disabled = True
        self.call_sort()

    def call_sort(self):
        """Call selected sorting class."""
        self.sort_obj = get_sort(sort=self.sort_name, numbers=self.numbers,
                                 bars=self.bars,
                                 static_x=self.static_x, ids=self.ids)
        self.ids['sort_label'].text = self.sort_obj.sort_name
        if self.sort_obj.events:
            for event in self.sort_obj.events:
                event()
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

    def previous(self):
        """Go to previous animation step."""

    def next(self):
        """Go to next animation step."""
        self.sort_obj.events[self.sort_obj.loop_counter +
                             self.sort_obj.switch_counter]()

    def update_entries(self) -> None:
        """Update settings TextInputs."""
        self.ids['members'].text = str(SETT['members'])
        self.ids['lower_limit'].text = str(SETT['lower_limit'])
        self.ids['upper_limit'].text = str(SETT['upper_limit'])

        self.ids['switch_duration'].text = str(ANIM['switch_duration'])
        self.ids['pause_duration'].text = str(ANIM['pause_duration'])
        self.ids['compare_duration'].text = str(ANIM['compare_duration'])

    def save_settings(self) -> None:
        """Save settings to dicts."""
        SETT['members'] = int(self.ids['members'].text)
        SETT['lower_limit'] = int(self.ids['lower_limit'].text)
        SETT['upper_limit'] = int(self.ids['upper_limit'].text)

        ANIM['switch_duration'] = float(self.ids['switch_duration'].text)
        ANIM['pause_duration'] = float(self.ids['pause_duration'].text)
        ANIM['compare_duration'] = float(self.ids['compare_duration'].text)
