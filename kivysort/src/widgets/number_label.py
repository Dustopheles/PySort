"""NumberLabel module."""

from kivy.uix.label import Label
from kivy.graphics import Color, Rectangle

try:
    from src.configs.color_config import ColorConfig
except ImportError as i_err:
    print(i_err)

class NumberLabel(Label):
    """NumberLabel class."""
    def __init__(self, root, **kwargs):
        super().__init__(**kwargs)
        self.root = root
        self.root.bind(pos=self.update_self)
        self.root.bind(size=self.update_self)
        self.height = 30
        self.redraw_rectangle(rgba=self.root.rgba)

    def redraw_rectangle(self, rgba: list) -> None:
        """Redraw and bind canvas rectangle with input rgba."""
        r, g, b, a = rgba
        self.canvas.clear()
        config = ColorConfig()
        with self.canvas:
            self.canvas_color = Color(r, g, b, a)
            self.rect = Rectangle(pos=self.pos, size=self.size)
            self.label = Label(text=self.text,
                               pos=(self.x, self.y + self.height/2),
                               size=(self.width, 1),
                               color=config.color_text,
                               font_size=self.get_font_size())
        self.canvas.ask_update()

        # pylint: disable=no-member
        self.bind(pos=self.update_self)
        self.bind(size=self.update_self)

    def update_self(self, *_args) -> None:
        """Update pos/size of widget."""
        self.pos = (self.root.x, self.root.y - 35)
        self.size = self.root.width, self.height
        self.update_canvas()

    def update_canvas(self, *_args) -> None:
        """Update pos/size or canvas."""
        self.rect.pos = self.pos
        self.rect.size = self.size
        self.update_label()

    def update_label(self, *_args) -> None:
        """Updaze pos/size/text of label"""
        self.label.pos = self.pos
        self.label.size = self.size
        self.label.text = self.text
        self.label.font_size = self.get_font_size()

    def get_font_size(self) -> float:
        """Return adjusted text size in relation to text length and widget size."""
        if len(self.text) > 2:
            size = min(self.height*0.9, self.width*0.9 / len(self.text))
            return size
        size = min(self.height*0.7, self.width*0.7)
        return size
