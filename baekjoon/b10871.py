N, X = map(int, input().split())
#print(N, X)

A = map(int, input().split())
#print(A)
#A = list(map(int, input().split()))
#print(A)

for num in A:
    if num < X:
        print(num, end=" ")

#2------------------------------------
#res = [x for x in x int(x)<X]
#print(*res)