class Player:
    def __init__(self, name, ab, h):
        self.name = name
        self.ab = ab
        self.h = h

    def print(self):
        print(f"name:{self.name}, AVG:{self.getAVG} , AB:{self.ab} , H:{self.h} ")
        print(format(self.getAVG(), ".3f"))
    
    def getAVG(self):
        return int(self.h)/int(self.ab)

for x in range(2):
        name, ab, h = input().split()
        print(name, ab, h)        
        P = Player(name, ab, h)
        P.print()     