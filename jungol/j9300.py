#홀수출력, 반대로 출력
S, E= map(int,input().split())

for i in range(E, S):
    if i % 2 == 0:  
        print(i)