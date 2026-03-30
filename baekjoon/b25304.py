X = int(input())
#print(X)
N = int(input())
#print(N)
res = 0
for i in range(N):
    a, b = map(int, input().split())
    #print(a, b)
    res += (a * b)
#print(res)

if X == res:
    print("Yes")
else:
    print("No")


#2-------------------------------
X = int(input())
N = int(input())

total_price = sum(a * b for _ in range(N) for a, b in [map(int, input().split())])
print("Yes" if total_price == X else "No")



#3-----------------------------------
X=int(input())
A=[]
B=[]
total = 0
for _ in range(int(input())):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)
    
for t in range(len(A)):
    total += A[t] * B[t]

if X==total:
    print('yes')
else:
    print('no')