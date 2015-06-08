import roll as r
import json
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

    def save(self):
        with open('player.json','w') as outfile:
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
if __name__=='__main__':
    player=Player()
    player.showstats()
    player.save()
