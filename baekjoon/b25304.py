X = int(input())
#print(X)
N = int(input())
#print(N)
prod = 0
for i in range(N):
    a, b = map(int, input().split())
    #print(a, b)
    prod += (a * b)

#print(prod)

if X == prod:
    print("Yes")
else:
    print("No")


#2-------------------------------
X = int(input())
N = int(input())

total_price = sum(a * b for _ in range(N) for a, b in [map(int, input().split())])
print("Yes" if total_price == X else "No")
