class Building:
    def __init__(self, year, price):
        self.year = year
        self.price = price
    def print(self):
        print(f"{self.year} {self.price}")

blst = []      #리스트사용    
N = int(input())
#print(N)
for i in range(N):
    year, price = map(int, input().split())
    b = Building(year, price)
    blst.append(b)

#for j in blst:
#    blst[j].print()
    
Y, P = map(int, input().split())
#print(Y, P)
#---------------------------------------1단계

for k in range(N):
    if blst[k].year >= Y and blst[k].price <= P:
        blst[k].print()