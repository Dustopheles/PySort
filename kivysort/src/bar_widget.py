"""Bar UI Widget."""

from kivy.uix.button import Label
from kivy.graphics import Color, Rectangle

from src.config import bar_dict as BAR

class Bar(Label):
    """Bar widget class."""
    def __init__(self, **kwargs):
        super(Bar, self).__init__(**kwargs)
        self.size_hint = (None, None)
        self.pos = (kwargs["x"], 80)
        self.size = (kwargs["width"], kwargs["height"])
        self.redraw_rectangle(rgba=BAR['color_passive'])
        self.text = kwargs["text"]

    def redraw_rectangle(self, rgba: list) -> None:
        """Redraw and bind canvas rectangle with input rgba."""
        # pylint: disable=all
        r, g, b, a = rgba
        self.canvas.clear()
        with self.canvas:
            self.canvas_color = Color(r/255, g/255, b/255, a)
            self.rect = Rectangle(pos=self.pos, size=self.size)
            self.label = Label(text=self.text,
                            pos=(self.x, self.y -25),
                            size=(self.width, 1))

        self.bind(pos=self.update_rect)
        self.bind(size=self.update_rect)

    def update_rect(self, *_args):
        """Position and size binding for canvas rectangle."""
        self.rect.pos = self.pos
        self.rect.size = self.size
        self.label.pos = (self.x, self.y -25)
        self.label.text = self.text
