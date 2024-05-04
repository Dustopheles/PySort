"""Bar UI Widget."""

from kivy.uix.button import Label
from kivy.graphics import Color, Rectangle
# pylint: disable=no-name-in-module
from kivy.properties import StringProperty

try:
    from src.configs.color_config import ColorConfig
    from src.widgets.number_label import NumberLabel
except ImportError as e:
    raise e

class BarWidget(Label):
    """Bar widget class."""
    state = StringProperty(None)
    colors = ColorConfig()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size_hint = (None, None)
        self.y = 100
        self.redraw_rectangle(rgba=self.colors.color_passive)
        # pylint: disable=no-member
        self.bind(state=self.on_state_change)

    def on_state_change(self, *_args) -> None:
        """State change event."""
        match self.state:
            case "compare":
                color = self.colors.color_active
            case "switch":
                color = self.colors.color_switch
            case "sorted":
                color = self.colors.color_sorted
            case _:
                color = self.colors.color_passive
        self.redraw_rectangle(color)

    def redraw_rectangle(self, rgba: list) -> None:
        """Redraw and bind canvas rectangle with input rgba."""
        self.rgba = rgba
        r, g, b, a = rgba
        self.canvas.clear()
        with self.canvas:
            self.canvas_color = Color(r, g, b, a)
            self.rect = Rectangle(pos=self.pos, size=self.size)
            self.label = NumberLabel(self, text=self.text,
                                     pos=(self.x, self.y - 35),
                                     width=self.width)
            self.label.redraw_rectangle(rgba)
        self.canvas.ask_update()

        # pylint: disable=no-member
        self.bind(pos=self.update_rect)
        self.bind(size=self.update_rect)

    def update_rect(self, *_args):
        """Position and size binding for canvas rectangle."""
        self.rect.pos = self.pos
        self.rect.size = self.size
