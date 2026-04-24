#밖 for:행
#안 for : 열
# ->밖for과 안for의 형식을 생각해기 

#2중 for문
N = int(input())
#print(N)

for x in range(N):  #밑3줄이 위 for문에 포함되어있음  
    for y in range(N, 0, -1): # 별이 찍혀있는 숫자가 안for의 의미  
        print(x, y)
    print()  #줄바꿈

##별찍기로 변경
for x in range(N):  
    for y in range(0, N-x): 
        print('*', end=" ")
    print() 


#2
n = int(input())
for i in range(n,0,-1):
    print('*'*i)

#3
N = int(input())
# print(N)
stars = "*" * N  #별 개수만큼을 변수에 저장

for i in range(N):
    print(stars[:N - i])    