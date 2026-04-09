#input : output
#1 : 1(이동거리) 
#2~7 : 2
#8~19 : 3
#20~37 : 4
#26~61 : 5

# 1, 2, 8, 20, 38...
#   +6 +12 +18 +... 6씩 증가

#N =13
#1 = x
#2~7 = x .....6 * x
#8~19


N = int(input())
#print(N)
boundary = 1
x = 1

for x in range(10):
    if N <= boundary:
        break;
    boundary = boundary + (6 * x)
    x = x + 1

#    print(x, boundary)
print(x)


#2
class Honeycomb:
    def __init__(self):
        self.layer = 1
        self.max_room = 1

    def expand(self):
        self.max_room += 6 * self.layer
        self.layer += 1

    def find_dist(self, target):
        while target > self.max_room:
            self.expand()
        return self.layer

h = Honeycomb()
print(h.find_dist(int(input())))