# 1+2+3+...+9+10 = 55
# 1+2+3+...+99+100 = 
# 1+2+3+...+1000 = 500500
# 1+2+...10000 = 50005000

N = int(input())
#print(N)

#for문
sum = 0  #변수 선언 0으로 초기화 
for i in range(1, N+1):
    #print(i)
    sum += i
print(sum)

#while문 ---------------------range 안에 있는 조건을 하니씩 나열
sum =  0
i = 1
while i <= N:
    sum += i
    i += 1
print(sum)
#초기화 식은 while문 전에 
#조건식은 


