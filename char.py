from roll import roll
import json
class Char():
    def setstats(self):
        self.intelligence=roll(3,6)
        self.strength=roll(3,6)
        self.wisdom=roll(3,6)
        self.agility=roll(3,6)
        self.luck=roll(3,6)
        self.charisma=roll(3,6)
        self.dexterity=roll(3,6)
        self.tenacity=roll(3,6)
    def showstats(self):
        text='''
        Intelligence:  {s.intelligence}
        Strength:      {s.strength}
        Wisdom:        {s.wisdom}
        Agility:       {s.agility}
        Luck:          {s.luck}
        Charisma:      {s.charisma}
        Dexterity:     {s.dexterity}
        Tenacity:      {s.tenacity}
        '''
        print(text.format(s=self))

    def savestats(self):
        with open('.player.json','w') as outfile:
            outfile.write(json.dumps({
            "strength":self.strength,
            "wisdom":self.wisdom,
            "agility":self.agility,
            "luck":self.luck,
            "charisma":self.charisma,
            "dexterity":self.dexterity,
            "tenacity":self.tenacity,
            "intelligence":self.intelligence
            }))
    def loadstats(self):
        with open('.player.json','r') as infile:
            j=json.load(infile)
            self.strength=j["strength"]
            self.wisdom=j["wisdom"]
            self.agility=j["agility"]
            self.luck=j["luck"]
            self.charisma=j["charisma"]
            self.dexterity=j["dexterity"]
            self.tenacity=j["tenacity"]
            self.intelligence=j["intelligence"]

class NewPlayer(Char):
    def __init__(self):
        self.setstats()

class OldPlayer(Char):
    def __init__(self):
        self.loadstats()

class Dragon(Char):
    def __init__(self):
        self.setstats()
        self.strength+=10

class Lich(Char):
    def __init__(self):
        self.setstats()
        self.intelligence+=10
        self.wisdom+=5

if __name__=='__main__':
    player_a=NewPlayer()
    player_b=OldPlayer()
    enemy_a=Dragon()
    enemy_b=Lich()
    print('enemy stats:')
    enemy_a.showstats()
    enemy_b.showstats()
    print('player stats:')
    player_b.showstats()
    player_a.showstats()
