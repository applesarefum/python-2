"""A simple Player class with stats generated on creation."""

from dice import roll

class Player():

    def __init__(self):
        self.strength = roll(3,6)
        self.constitution = roll(3,6)
        self.dexterity = roll(3,6)
        self.intelligence = roll(3,6)
        self.wisdom = roll(3,6)
        self.charisma = roll(3,6)

if __name__ == '__main__':
    player = Player()
    print(player)
