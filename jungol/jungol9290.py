N = int(input())
#print(N)

for i in range(0, N):
    print(f"Python {i} ")  #print("Python" + str(i))


#2 while문
N = int(input())
# print(N)
i = 0
while True:   # while 옆에 True 가 있는건 무한루프. 근데 무조건 빠져나가는 break가 있어야함
    if i >= N:
        break
    print(f"Python {i}")
    i += 1  