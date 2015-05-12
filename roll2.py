import random as rand
def roll1(sides):
    return rand.randint(1,int(sides))
def roll(times,sides):
    return rand.randint(int(times),int(sides)*int(times))

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

