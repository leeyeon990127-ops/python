N = int(input())
#print(N)

for X in range(N, 0, -1): #시작, 끝, 간격
    print(X, end= " ")



###################################################
#whlie문
while N >=1:
    print(N, end= " ")
    N = N -1    

##################################################
#lst 
lst = []
N = int(input())
for i in range(1, N+1):
    lst.append(i)
lst2 = list(reversed(lst))
print(*lst2, end = ' ')   