import roll as r
class Player():
    def __init__(self):
        self.intelligence=r.roll(2,5)
        self.strength=r.roll(2,5)
        self.wisdom=r.roll(2,5)
        self.agility=r.roll(2,5)
        self.luck=r.roll(2,5)
        self.charisma=r.roll(2,5)
        self.dexterity=r.roll(2,5)
        self.tenacity=r.roll(2,5)
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

if __name__=='__main__':
    player=Player()
    player.showstats()
