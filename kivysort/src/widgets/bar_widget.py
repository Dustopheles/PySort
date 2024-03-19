"""Bar UI Widget."""

from kivy.uix.button import Label
from kivy.graphics import Color, Rectangle

try:
    from src.configs.color_config import ColorConfig as Colors
    from src.widgets.number_label import NumberLabel
except ImportError as i_err:
    print(i_err)

class BarWidget(Label):
    """Bar widget class."""
    def __init__(self, **kwargs):
        super(BarWidget, self).__init__(**kwargs)
        self.size_hint = (None, None)
        self.pos = (kwargs["x"], 100)
        self.size = (kwargs["width"], kwargs["height"])

        self.text = kwargs["text"]
        self.rgba = Colors.passive
        self.redraw_rectangle(rgba=self.rgba)

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
