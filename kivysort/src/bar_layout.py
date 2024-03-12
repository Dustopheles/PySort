"""Bar layout widget."""

from kivy.uix.floatlayout import FloatLayout

from src.bar_widget import Bar
from src.config import settings_dict as SETT

class BarLayout(FloatLayout):
    """Bar layout widget class."""
    def __init__(self, root, numbers, **kwargs):
        super(BarLayout, self).__init__(**kwargs)
        self.root = root
        self.numbers = numbers
        self.bars = []
        self.static_x = []
        self.build_bars()

    def build_bars(self) -> None:
        """Build bars in relation to screen size."""
        x = 10
        root_width = self.root.width - len(self.numbers)*5 - x
        width = max(int(root_width/SETT['members']), 1)

        root_height = 400
        biggest = max(self.numbers)

        for number in self.numbers:
            height = root_height*(number/biggest)
            self.static_x.append(x)
            self.bars.append(self.add_bar(width, height, x, number))
            x += width + 5

    def add_bar(self, width: int, height: int, x: int, number: int) -> Bar:
        """Add bar to parent widget."""
        bar_widget = Bar(x=x, height=height, width=width, text=str(number))
        self.add_widget(bar_widget)
        return bar_widget
