N = int(input())
#print(N)

for X in range(5, N+1):
   print(X)

#2--------------------------
N = int(input())
# print(N)
comp = 5
while True:
    print(comp)
    if comp == N:
        break
    comp += 1
   
#'무한루프'를 쓰게 되면 종료지점을 넣어줘야 끝난다
N = 1
while True:
   print(N)
   N += 1
   #이렇게 출력하면 무한대로 계속 나온다 그래서 break를 걸어줘야함