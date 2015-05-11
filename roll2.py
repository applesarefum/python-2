import random as rand
def roll1(sides):
    return rand.randint(1,sides)
def roll(times,sides):
    total=0
    for count in range(times):
        total+=roll1(sides)
    print(total)

if __name__=='__main__':
    qwe=roll1(7)
    print(qwe)
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

