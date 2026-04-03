lst = []

for i in range(50):
   lst.append(int(input()))


for i in lst[::-1]:  #for 변수 in 반복 범위 또는 대상:   
          # [-1, -1, -1]도 가능   / ::(:간격만틈 건너뛰라) 
   print(i, end=" ")

#--------------------------------------------------------------
#2
L =[]
for i in range(50):
    L.append(int(input()))
print(*L[::-1])

#2
inp = [int(input()) for i in range(50)]
# print(inp)
print(*inp[::-1])

