# 테스트 케이스는 2
T = int(input())
#print(T) 

for n in range(T):
    #print(n)
    R, S = input().split()    
    #print(R, S)

    for i in S: 
        for j in range(int(R)):  #S문자열 반복
            print(i, end='')
print()        

#2-------------------------
T = int(input())
#print(T) 


lstr = []
lsts = []

for n in range(T):
    R, S = input().split()    
    lsts.append(int(R))
    lsts.append(S)

#for m in range(len(lstr)):
#print(lstr[m], lets[m])

for m in range(T):
    for i in lsts[m]:
        for j in range(lstr[m]):
            print(i, end='')
    print()        

#3-----------------
T = int(input())

for _ in range(T):
    R, S = input().split()
    R = int(R)

    for x in S:
        print(x*R, end='')
    
    print()


#4-------------------
T = int(input())
for _ in range(T):
    R, S = input().split()

    print(*(char * int(R) for char in S), sep='')