N = int(input())
#print(N)

for x in range(10, N+1, 10): 
    print(x)

#---------------------------------------
#2 for문 %사용
for i in range(10, N+1):
    if i%10 == 0:
        print(i)    

#3 while 
j = 10 
while j <= N:
    print(j)
    j += 10        

#4 함수
def print_tens(N):
    i = 10
    while i <= N:
        print(i)
        i += 10

limit = int(input())
# print(limit)
print_tens(limit)
   