"""A simple Player class with stats generated on creation."""

from dice import roll
import colors as c

class Player():

    def __init__(self):
        self.strength = roll(3,6)
        self.constitution = roll(3,6)
        self.dexterity = roll(3,6)
        self.intelligence = roll(3,6)
        self.wisdom = roll(3,6)
        self.charisma = roll(3,6)

    def show_stats(self):
        text = '''
        Strength:      {s.strength:>2}
        Constitution:  {s.constitution:>2} 
        Intelligence:  {s.intelligence:>2}
        Wisdom:        {s.wisdom:>2}
        Charisma:      {s.charisma:>2}
        '''
        print(text.format(s=self))

if __name__ == '__main__':
    player = Player()
    c.clear_screen()
    player.show_stats()
