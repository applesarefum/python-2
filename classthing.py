import roll
class Stats():
    def setstats(self):
        self.basehp=100
        self.speed=roll.parse_roll('3d6')
        self.strength=roll.parse_roll('3d6')
        self.charm=roll.parse_roll('3d6')
        self.wisdom=roll.parse_roll('3d6')
        self.intelligence=roll.parse_roll('3d6')

    def showstats(self):
        text='''
    Speed=         {s.speed:>2}
    Strength=      {s.strength:>2}
    Charm=         {s.charm:>2}
    Wisdom=        {s.wisdom:>2}
    Intelligence=  {s.intelligence:>2}
    Base HP=       {s.basehp:>2}
    '''
        print(text.format(s=self))

class Enemy(Stats):
    def __init__():
        self.setstats()
    

if __name__=='__main__':
    p=Enemy()
    p.showstats()
