from random import randint

class Die():
    """Klasa przedsawiająca rzut pojedyńczą kością"""

    def __init__(self, num_sides=6):
        """funkcja zakładajaca ze kostka ma 6 ścian"""
        self.num_sides=num_sides

    def roll(self):
        """Zwrot wartosc od 1 do ilości scian"""
        return randint(1,self.num_sides)

