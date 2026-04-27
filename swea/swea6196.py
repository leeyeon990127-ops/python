#a:9 = 9
#aa :9*2 = 99  
#aaa :9*3 = 999   
#aaaa : 9*4 = 9999  

a = input()    #int로 변환을 해서 숫자 계산이 되어버렸다. a=9 자체로 계산을 해야함
#print(a)

print(int(a) + int(a*2) + int(a*3) + int(a*4))

#2---------------------------------
N = input()

sum = 0
str = N
for i in range(4):
    sum += int(str)
    str += N

#3-------------------------------------
a_Str = input()
# print(a_Str)

term1 = int(a_Str)
term2 = int(a_Str * 2)
term3 = int(a_Str * 3)
term4 = int(a_Str * 4)

print(term1 + term2 + term3 + term4)

#4---------------------------------------
