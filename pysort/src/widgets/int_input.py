"""IntInput module."""

import re
from kivy.uix.textinput import TextInput

class IntInput(TextInput):
    """TextInput class for only int values > 0."""
    pat = re.compile('[^0-9]')
    def insert_text(self, substring, from_undo=False):
        pat = self.pat
        s = re.sub(pat, '', substring)
        if s.startswith('0') and not self.text:
            s = s.replace('0', '')
        return super().insert_text(s, from_undo=from_undo)
