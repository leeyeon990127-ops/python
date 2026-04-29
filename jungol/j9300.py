#홀수출력, 반대로 출력
S, E= map(int,input().split())

for i in range(E, S-1, -1):  # range(시작,끝,증감)에서 증감값을 -1 = 숫자가 거꾸로 작아진다
    if i % 2 != 0:   #같지 않다; !=
        print(i)