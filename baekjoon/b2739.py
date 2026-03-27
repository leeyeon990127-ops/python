N = int(input())
#print(N)

for i in range(9): 
    print(N, '*', i+1, '=', N*(i+1))


#2--------------
N = int(input())
for x in range(1, 10, 1):
    print(f'{N} * {x} =', N*x)

#3---------------
N = int(input())
for i in range(1, 10):
    print(f"{N} * {i} = {N * i}")