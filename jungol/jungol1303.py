n, m = map(int, input().split())
#print(n, m)

num = 1  # 시작숫자
for i in range(n):     # 행
    for j in range(m): # 열
        print(num, end=' ')
        num += 1
    
    print() 

#2
n, m = map(int, input().split())
# print(n, m)
for i in range(1, n * m + 1):
    print(i, end=" ")
    if i % m == 0:
        print()