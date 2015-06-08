"""The main game engine"""
import colors as c
from player import Player

class Game():

    def __init__(self):
        print(c.clear + 'Welcome to this awesome game.')
        self.player = Player()
        self._choose_monster()

    def run(self):
        while True:
            self.player.show_stats()
            # TODO show monster stats
            action = input('What would you like to do? ')
            print(c.clear)
            #TODO handle action

    def _choose_monster(self):
        pass
        
if __name__ == '__main__':
    agame = Game()
    agame.run()
