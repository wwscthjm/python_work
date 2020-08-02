"""Using Pygal to Create a Die"""

from random import randint


class Die:
    """Class represents a die"""

    def __init__(self, num_sides=6):
        """6 facets on a die"""
        self.num_sides = num_sides

    def roll(self):
        """Return a random int between 1 and facets number"""
        return randint(1, self.num_sides)
