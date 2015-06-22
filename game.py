import colors as col
import char
class Game():
    def __init__(self):
        print(col.clear+'welcom 2 teh gaem')
        self.player=char.NewPlayer()
    def start(self):
        while True:
            thing=input('wat thing you do for do?(tiyp help for help(duh))')
            if thing=='stats':
                self.player.showstats()
            elif thing=='exit':
                print(col.clear+'bai')
                exit()
            elif thing=='save':
                self.player.savestats()
            elif thing=='help':
                print('''
  help   this(duh)
  stats  show tha stats(also duh)
  save   save gaem(are yoo stuped?)
  exit   exit gaem(o mi gosh u r dum)
''')

            #TODO pick monster

            else:
                print('I dont no hao 2 du tht')
if __name__=='__main__':
    qwer=Game()
    qwer.start()
