#a = int(input())
#b = int(input())
#print(a)
#print(b)


a, b = map(int, input().split())
#print(a, b)

if a < b:
    print(a)
    print(b)
else:
    print(b)
    print(a)    

#2--------------
a, b = map(int, input().split())
print(min(a, b)) #min(최솟값) 작은 값이 나옴
print(max(a, b)) #max(최댓값) 큰 값이 나옴옴
