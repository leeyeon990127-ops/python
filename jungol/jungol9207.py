a, b = map(int,input().split())
#print(a, b)

#print(a % 2)
#print(b + 10)
print(f"{a % 2} {b + 10} {(a % 2)+(b + 10)}")


#2
def cal(N, M):
    A = N%2
    B = M+10
    return A, B, A+B

N, M = map(int, input().split())
a, b, c = cal(N, M)
print(*cal(N, M))


#3
a, b = map(int, input().split())

first = a % 2
second = b + 10
total = first + second

print(first, second, total)