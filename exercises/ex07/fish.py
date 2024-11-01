"""File to define Fish class."""

__author__ = "730391230"


class Fish:
    """Defines the class Fish."""

    age: int

    def __init__(self):
        """Initializes the class Fish."""
        self.age = 0
        return None

    def one_day(self):
        """Increases age by one after one day."""
        self.age += 1
        return None
