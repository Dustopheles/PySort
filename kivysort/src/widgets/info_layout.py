"""InfoLayout module."""

import platform

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.graphics import Color, Rectangle

class InfoLayout(BoxLayout):
    """Info layout widget class."""
    def __init__(self, **kwargs):
        super(InfoLayout, self).__init__(**kwargs)
        self.size_hint_y = None
        self.height = 25
        self.padding = (5,0,10,2)
        self.spacing = 1
        self.draw_canvas()
        self.add_label("SBSZ - Hermsdorf Projekt 2024")
        self.add_widget(Label(width=self.width))
        self.add_label(f"Python {platform.python_version()}")
        self.add_label(f"{platform.system()}")
        print(self.children[0].pos)

    def draw_canvas(self) -> None:
        """Draw widget canvas."""
        with self.canvas:
            self.canvas_color = Color(.15, .15, .15, 1)
            self.rect = Rectangle(pos=self.pos,
                                  size=self.size)
            self.canvas_color = Color(.12, .12, .12, .9)
            self.liner = Rectangle(pos=(0, self.y + self.height),
                                   size=(self.width, 2))
        self.canvas.ask_update()

        # pylint: disable=no-member
        self.bind(pos=self.update_rect)
        self.bind(size=self.update_rect)

    def add_label(self, text: str) -> None:
        """Add info label"""
        label = Label(size_hint_x=None,
                      text=text,
                      width=len(text)*8)

        self.add_widget(label)

    def update_rect(self, *_args):
        """Position and size binding for canvas rectangle."""
        self.rect.size = self.size
        self.liner.size = (self.width, 2)
