#s, e = map(int, input().split())
#print(s, e)
 #2중 for문 
#for i in range(1, 10):
#   for x in range(3, ):
#        print(f"{} * {} = {i*x}", end="")
#   print()    


#####################################################
s, e = map(int, input().split())
#print(s, e)

step = 1
if s < e:
    step = 1
else:
    step = -1

if s > 2 
for i in range(1, 10):
    for j in range(s, e+step, step): 
        print(f"{j} * {i} = {i * j}   ", end='')
    print()
          
#else:
#    print("INPUT ERROR!")


s = 0
e = 0
while True:
    s, e = map(int, input().split())
    if(not(2<=s and s<=9) or not(2<=e and e<=9)):
        print("INPUT ERROR!")
    else:
        break

if s < e:
    for j in range(1, 10):
        for i in range(s, e+1):
            print(f"{i} * {j} = {i*j:2d}", end="   ")
        print()
else:
    for j in range(1, 10):
        for i in range(s, e-1, -1):
            print(f"{i} * {j} = {i*j:2d}", end="   ")       
        
        print()
###39~47줄을  요약하면 
for i in range(1, 10):
    row = []
    for dan in range(s, e + step, step):
        row.append(f"{dan} * {i} = {dan * i:2d}")
    print("   ".join(row))