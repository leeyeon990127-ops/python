#3
#26 40 83
#49 60 57
#13 89 99

#     R           G           B
#1-   26          40          83
#2-(40+49=89) (26+60=86) (26+57=83)
#3-(83+13=96) ()




#N = (input())  # 집의 수 입력
#print(N)

#lst = []  # 칠하는 비용 입력
#for i in range(N):
#    cost = list(map(int, input().split()))  #공백으로 구분된 숫자들을 리스트를 만들어서 lst에 추가
#    cost.append()

# 1. -----------------------------------
R = []; G = []; B = []
crdR = []; crdG = []; crdB = []
N = int(input())
for x in range(N):
    r, g, b = map(int, input().split())
    R.append(r)
    G.append(g)
    B.append(b)

crdR = R.copy()
crdG = G.copy()
crdB = B.copy()

# print(f"crdRGB -----")
# for x in range(N):
#     print(crdR[x], crdG[x], crdB[x])

for x in range(1, N):
    crdR[x] = R[x] + min(crdG[x-1], crdB[x-1])
    crdG[x] = G[x] + min(crdR[x-1], crdB[x-1])
    crdB[x] = B[x] + min(crdR[x-1], crdG[x-1])

print(f"crdRGB -----")
for x in range(N):
    print(crdR[x], crdG[x], crdB[x])

print(min(crdR[N-1], crdG[N-1], crdB[N-1]))

#3 리스트를 사용해서 튜플로 문제풀이
n = int(input())
# print(n)
r, g, b = map(int, input().split())

for x in range(n - 1):
    nr, ng, nb = map(int, input().split())
    
    r, g, b = nr + min(g, b), ng + min(r, b), nb + min(r, g)

print(min(r, g, b))