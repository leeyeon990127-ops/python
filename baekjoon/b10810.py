#리스트를 활용해서 인덱스로 
#5 4
#1 2 3  # -> 1번 바구니에서 2번 바구니까지 공을 3번 넣겠다
#[3,3,0,0,0]
#3 4 4
#[3,3,4,4,0]
#1 4 1
#[1,1,1,1,0]
#2 2 2
#[1,2,1,1,0]

N, M =  map(int, input().split())

basket = []
for row in range(N+1):
    basket.append(0) #처음 모든 바구니에는 공X. 0이 들어있는 N개의 바구니 리스트 생성. 인덱스는 0부터 시작하는데 바구니는 1부터 시작하니 N+1

for x in range(M):
    i, j, k = map(int, input().split())
    for u in range(i, j+1):     # i부터 j+1 까지 
        basket[u] = k
        #작동 원리: basket[3] = 7이라고 하면, 3번 칸에 무엇이 들어있었든 상관없이 전부 비우고 7을 집어넣는 것입니다.
print(*basket[1:])

