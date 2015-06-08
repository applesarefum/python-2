"""A simple Player class with stats generated on creation."""

from dice import roll

# WRONG
class Player():
    strength = roll(3,6)

if __name__ == '__main__':
    player1 = Player()
    print(player1.strength)
    player2 = Player()
    print(player2.strength)
