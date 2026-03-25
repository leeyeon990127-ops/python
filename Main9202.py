a = 5
b = 3
# print(a/b)  #결과
# print(a//b) #몫
# print(a%b)  #나머지

a, b = input().split()
na = int(a)
nb = int(b)
print(a, '/', b, '=', na//nb, '...', na%nb)
