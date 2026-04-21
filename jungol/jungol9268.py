N = int(input())
#print(N)

for i in range(N, 4, -1): #시작, 끝, 증가(역으로 츨력되니 -1)
    print(i)


#2 while
N =  int(input())
print(N)

while 5 < N:
    print(N)
    N -= 1 # 같은의미:N = N -1 

#문자열 .join
n = int(input())
# print(n)
print('\n'.join(map(str, range(n, 4, -1))))