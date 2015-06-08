"""A simple Player class with stats generated on creation."""

from dice import roll

class Player():
    strength = 10

    def __init__(self):
        print("default " + str(self.strength))
        self.strength = roll(3,6)

if __name__ == '__main__':
    player1 = Player()
    print(player1.strength)
    player2 = Player()
    print(player2.strength)
