"""Operation dataclass module."""

from dataclasses import dataclass, field

@dataclass
class Operation():
    """Operation data class respresenting one operation step."""
    operation: str = ""
    timeout: float = 0.0
    index_pair: tuple = ()
    event: object = None
    widgets: list[object] = field(default_factory=list)

    def widget_pair(self) -> tuple:
        """Return widgets from index."""
        a = self.widgets[self.index_pair[0]]
        b = self.widgets[self.index_pair[1]]
        return (a, b)

    def number_pair(self) -> tuple:
        """Return numbers from indexed widgets."""
        widget_pair = self.widget_pair()
        a = int(widget_pair[0].text)
        b = int(widget_pair[1].text)
        return (a, b)

    def numbers_before(self) -> list:
        """Return numbers from widgets."""
        numbers = []
        for widget in self.widgets:
            numbers.append(int(widget.text))
        return numbers

    def numbers_after(self) -> list:
        """Return numbers from widgets."""
        numbers = self.numbers_before()
        if self.operation == "compare":
            return numbers
        tmp = numbers[self.index_pair[0]]
        numbers[self.index_pair[0]] = numbers[self.index_pair[1]]
        numbers[self.index_pair[1]] = tmp
        return numbers
