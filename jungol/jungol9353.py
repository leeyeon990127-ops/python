A = ['a', 'b', 'c', 'd', 'e']
print(A)

for x in A[::-1]:
    print(x, end =' ')

#---------------------------------------------
#2 while
length = len(A)
#print(length)
i = 1
while i <= length:
    print(A[length-i], end= ' ')
    i+1

#2-1 while 
A = ['a', 'b', 'c', 'd', 'e']

print(A)

i = len(A) - 1

while i >= 0:
    print(A[i], end=' ')
    i -= 1   