A = "apple orange banana"
words = A.split()
B = "   Hello world!   "

for i in words[::-1]:
    print(i, end= ' ')
print()  #줄바꿈
print(B)
print(B.strip())  #strip : 공백을 줄여주는 


#2
A = "apple orange banana"
words = A.split()[::-1]
print(*words)

B = "   Hello world!   "
print(B)
print(B.strip())


#3
a='apple orange banana'
b='   Hello world!   '

print(' '.join(reversed(a.split())))
print(b)
print(b.strip())