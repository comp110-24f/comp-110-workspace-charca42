"""File to define Bear class."""

__author__ = "730391230"


class Bear:
    """Defines the class Bear."""

    age: int
    hunger_score: int

    def __init__(self):
        """Initializes the class Bear."""
        self.age = 0
        self.hunger_score = 0
        return None

    def one_day(self):
        """Increases the value of age by one, and decreases the hunger score."""
        self.age += 1
        self.hunger_score -= 1
        return None

    def eat(self, num_fish: int):
        """Update hungers score so that it increases by num_fish."""
        self.hunger_score = +num_fish
        return None
