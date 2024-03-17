"""Bar layout widget."""

from kivy.uix.floatlayout import FloatLayout

try:
    from src.widgets.bar_widget import BarWidget
    from src.configs.generator_config import GeneratorConfig as Generator
except ImportError as i_err:
    print(i_err)

class BarLayout(FloatLayout):
    """Bar layout widget class."""
    def __init__(self, **kwargs):
        super(BarLayout, self).__init__(**kwargs)
        self.numbers = []
        self.bars = []
        self.static_x = []
        self.sort_obj = None
        # pylint: disable=no-member
        self.bind(size=self.resize_bars)

    def calc_bar_layout(self) -> tuple:
        """Calculate bar layout size."""
        x = 10
        root_width = self.width - len(self.numbers)*5 - x
        width = max(int(root_width/Generator.members), 1)
        height = self.height - 80
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
        self.resize_bars()

    def clear_bars(self) -> None:
        """Remove children."""
        self.clear_widgets()
        self.bars = []

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

    def add_bar(self, width: int, height: int, x: int, number: int) -> BarWidget:
        """Add bar to parent widget."""
        bar_widget = BarWidget(x=x, height=height, width=width, text=str(number))
        self.add_widget(bar_widget)
        return bar_widget
