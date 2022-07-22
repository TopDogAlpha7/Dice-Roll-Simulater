from random import randint

class Die:

    def __init__(self, num_sides=6):
        """"Assume a 6 sided die"""
        self.num_sides = num_sides

    def roll(self):
        """Return a random value between 1 and 6"""
        return randint(1, self.num_sides)
        