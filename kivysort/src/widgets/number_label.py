"""NumberLabel module."""

from kivy.uix.label import Label
from kivy.graphics import Color, Rectangle

class NumberLabel(Label):
    """NumberLabel class."""
    def __init__(self, root, **kwargs):
        super(NumberLabel, self).__init__(**kwargs)
        self.root = root
        self.root.bind(pos=self.update_self)
        self.root.bind(size=self.update_self)
        self.height = 30
        self.redraw_rectangle(rgba=self.root.rgba)

    def redraw_rectangle(self, rgba: list) -> None:
        """Redraw and bind canvas rectangle with input rgba."""
        r, g, b, a = rgba
        self.canvas.clear()
        with self.canvas:
            self.canvas_color = Color(r/255, g/255, b/255, a)
            self.rect = Rectangle(pos=self.pos, size=self.size)
            self.label = Label(text=self.text,
                               pos=(self.x, self.y + self.height/2),
                               size=(self.width, 1))
        self.canvas.ask_update()

        # pylint: disable=no-member
        self.bind(pos=self.update_self)
        self.bind(size=self.update_self)

    def update_self(self, *_args):
        """Update pos/size of widget."""
        self.pos = (self.root.x, self.root.y - 35)
        self.size = self.root.width, self.height
        self.update_canvas()

    def update_canvas(self, *_args):
        """Update pos/size or canvas."""
        self.rect.pos = self.pos
        self.rect.size = self.size
        self.update_label()

    def update_label(self, *_args):
        """Updaze pos/size/text of label"""
        self.label.pos = self.pos
        self.label.size = self.size
        self.label.text = self.text
