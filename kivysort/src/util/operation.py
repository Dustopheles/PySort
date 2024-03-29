"""Operation dataclass module."""

from dataclasses import dataclass, field

@dataclass
class Operation():
    """Operation data class respresenting one operation step."""
    operation: str = ""
    timeout: float = 0.0
    index_pair: tuple = ()
    event: object = None
    numbers_before: list[int] = field(default_factory=list)

    def number_pair(self) -> tuple:
        """Return numbers of indexes."""
        num_a = self.numbers_before[self.index_pair[0]]
        num_b = self.numbers_before[self.index_pair[1]]
        return (num_a, num_b)

    def numbers_after(self) -> list:
        """Return numbers after operation."""
        numbers = self.numbers_before
        if self.operation == "compare":
            return numbers
        tmp = numbers[self.index_pair[0]]
        numbers[self.index_pair[0]] = numbers[self.index_pair[1]]
        numbers[self.index_pair[1]] = tmp
        return numbers
