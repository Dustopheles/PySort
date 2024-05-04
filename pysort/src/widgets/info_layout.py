"""InfoLayout module."""

import platform

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.graphics import Color, Rectangle, SmoothEllipse
from kivy.uix.image import Image

class InfoLayout(BoxLayout):
    """Info layout widget class."""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size_hint_y = None
        self.height = 50
        self.padding = (13,0,13,1)
        self.spacing = 4
        self.on_load()

    def on_load(self) -> None:
        """On load event."""
        self.draw_canvas()
        self.add_widget(Image(source='res/sbsz.png',
                        fit_mode='scale-down',
                        width=45,
                        size_hint_x=None,
                        color=(1,1,1,1)))
        self.add_label("SBSZ - Hermsdorf Projekt 2024")
        self.add_widget(Label(width=self.width))
        self.add_label(f"Python {platform.python_version()}")
        self.add_label(f"{platform.system()}")

    def draw_canvas(self) -> None:
        """Draw widget canvas."""
        with self.canvas:
            # pylint: disable=all
            self.canvas_color = Color(23/255, 29/255, 37/255, 1)
            self.rect = Rectangle(pos=self.pos,
                                  size=self.size)
            self.canvas_color = Color(47/255, 54/255, 65/255, 1)
            self.liner = Rectangle(pos=(0, self.y + self.height),
                                   size=(self.width, 1))
            self.canvas_color = Color(1, 1, 1, 1)
            SmoothEllipse(pos=(8, self.y+5),
                          size=(self.height-10, self.height-10))

        self.canvas.ask_update()

        # pylint: disable=no-member
        self.bind(pos=self.update_rect)
        self.bind(size=self.update_rect)

    def add_label(self, text: str) -> None:
        """Add info label"""
        label = Label(size_hint_x=None,
                      text=text,
                      color=(154/255, 162/255, 171/255, 1),
                      width=len(text)*8)

        self.add_widget(label)

    def update_rect(self, *_args):
        """Position and size binding for canvas rectangle."""
        self.rect.size = self.size
        self.liner.size = (self.width, 2)
