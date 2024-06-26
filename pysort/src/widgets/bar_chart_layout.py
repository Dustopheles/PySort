"""Bar chart layout widget."""

from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Rectangle, Color
# pylint: disable=no-name-in-module
from kivy.properties import BooleanProperty, ListProperty

try:
    from src.widgets.bar_widget import BarWidget
    from src.configs.generator_config import GeneratorConfig
    from src.configs.color_config import ColorConfig
except ImportError as e:
    raise e

class BarChartLayout(FloatLayout):
    """Bar chart layout widget class."""
    config = ColorConfig()
    freeze = BooleanProperty(False)
    bars = ListProperty([])

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.numbers = []
        self.ref_x = []
        # pylint: disable=no-member
        self.bind(size=self.resize_bars)
        self.redraw_rectangle()

    def calc_bar_layout(self) -> tuple:
        """Calculate bar layout size."""
        x = 10
        root_width = self.width - len(self.numbers)*5 - x
        numbers = GeneratorConfig()
        width = max(int(root_width/numbers.numbers_length), 1)
        height = self.height - 80
        max_num = max(self.numbers)
        return width, height, max_num

    def build_bars(self) -> None:
        """Build bars in relation to screen size."""
        x = 10
        width, root_height, max_num = self.calc_bar_layout()
        for number in self.numbers:
            height = root_height*(number/max_num)
            self.ref_x.append(x)
            self.bars.append(self.add_bar(width, height, x, number))
            x += width + 5
        self.resize_bars()

    def clear_bars(self) -> None:
        """Remove children."""
        self.clear_widgets()
        self.bars = []

    def resize_bars(self, *_args):
        """Resize bar widgets."""
        if not self.bars:
            return
        if self.freeze:
            return
        x = 10
        width, root_height, max_num = self.calc_bar_layout()
        for index, widget in enumerate(self.bars):
            widget.height = root_height*(int(widget.text)/max_num)
            widget.width = width
            widget.x = x
            self.ref_x[index] = x
            x += width + 5

    def add_bar(self, width: int, height: int, x: int, number: int) -> BarWidget:
        """Add bar to parent widget."""
        bar_widget = BarWidget(x=x, height=height, width=width, text=str(number))
        self.add_widget(bar_widget)
        return bar_widget

    def redraw_rectangle(self) -> None:
        """Redraw and bind canvas rectangle with input rgba."""
        r, g, b, a = self.config.color_background
        self.canvas.clear()
        with self.canvas:
            self.canvas_color = Color(r, g, b, a)
            self.rect = Rectangle(pos=self.pos, size=self.size)
            self.canvas.ask_update()

        # pylint: disable=no-member
        self.bind(pos=self.update_rect)
        self.bind(size=self.update_rect)

    def update_rect(self, *_args):
        """Position and size binding for canvas rectangle."""
        self.rect.pos = self.pos
        self.rect.size = self.size
