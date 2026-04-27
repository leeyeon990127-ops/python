n, m = map(int, input().split())
#print(n, m)

for i in range(n):     # 행
    if i % 2 == 0: # 방향결정; i가 0, 2 일때는 정방향/ i가 1, 3 일때는 역방향
        for j in range(1, m +1 ): # 열 (정방향 출력)
            print(i * m + j, end=" ") # i:몇번째 행 인지/ num:한줄에 들어가는 숫자의 개수 /j :현재 줄 안에서 몇번쨰 숫자인지지
    else:    
        for j in range(n, 0, -1): # 역방향 출력
            print(i * m + j, end=" ")    
        
    
    print()    #줄바꿈

#짝수줄과 홀수줄로 구분

#2 ################################################################################
n, m = map(int, input().split())
#print(n, m)

num = 1
if i % 2 == 0:
    if i != 0:
        num += m
    for j in range(m):
        print(num, )
