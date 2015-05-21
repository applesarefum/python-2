"""Library for dice rolling"""
import random as rand

def roll(times=1,sides=6):
    """qwe"""
    total=0
    for count in range(times):
        total+=rand.randint(1,sides)
    return total

def parse(text):#text should be something like '2d5'
    """Parses traditional dice notation(ex: '2d5' returns 2,5)"""
    times,sides=text.split('d')
    return int(times),int(sides)

def parse_roll(text):#text should be something like '2d5'
    """Parses traditional dice notation and rolls(ex: 2d5 could return 8)"""
    (times,sides)=parse(text)
    return roll(times,sides)

if __name__=='__main__':
    import colors as c
    print(c.magenta+'\b')
    print('roll(3,6) ran 5 times results in:')
    for count in range(4):
        qwe=roll(3,6)
        print(qwe,end=', ')
    qwe=roll(3,6)
    print(qwe)
    
    print('parse(2d5) returns:')
    qwe=parse('2d5')
    print(qwe)
    
    print('parse_roll(2d5) ran 4 times results in:')
    for count in range(3):
        qwe=parse_roll('2d5')
        print(qwe,end=', ')
    qwe=parse_roll('2d5')
    print(qwe)
