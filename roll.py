import random as rand
def rolldie(sides=6):#unless other variable is defined, use six sides
    return rand.randint(1,sides)
def roll(times=1,sides=6):
    total=0
    for count in range(times):
        total+=rolldie(sides)
    return total

if __name__=='__main__':
    import colors as c
    print(c.orange)
    print('rolldie(13) ran 8 times results in:')
    for count in range(7):
        qwe=rolldie(13)
        print(qwe,end=', ')
    qwe=rolldie(13)
    print(qwe)
    print('roll(3,6) ran 5 times results in:')
    for count in range(4):
        qwe=roll(3,6)
        print(qwe,end=', ')
    qwe=roll(3,6)
    print(qwe)
#    def varin():
#        
#        bar=input('How many sides would you like this die to have? ')
#        bar=int(bar)
#        qwe=input('How many times would you like to roll this die? ')
#        qwe=int(qwe)
#        foo=roll(qwe,bar)
#        print(foo)

