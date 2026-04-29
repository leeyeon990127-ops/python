a=int(input())
b=int(input())
c=int(input())

for i in range(a, b+1, c):
    print(i)

#2 언패킹:*, sep='\n' 줄바꿈
S, E, K = [int(input()) for _ in range(3)]

print(*range(S, E + 1, K), sep='\n')   