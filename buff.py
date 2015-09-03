class Buff():
    def __init__(self,affects=None,duration='turn',amount=0,percent=0):
        self.affects=affects
        self.amount=0
        self.percent=0
        self.duration=duration

if __name__=='__main__':
    buff=Buff()
