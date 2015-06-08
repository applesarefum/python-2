"""The main game engine"""
import colors as c

class Game():

    def __init__(self):
        print(c.clear + 'Welcome to this awesome game.')
        # TODO create player
        # TODO choose monster

    def run(self):
        # TODO show player stats
        # TODO show monster stats
        while True:
            action = input('What would you like to do? ')
            #TODO handle action
        
if __name__ == '__main__':
    agame = Game()
    agame.run()
