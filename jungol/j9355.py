lst = []

for x in range(5):
    N = input()
    lst.append(N)

list = list(map(int, lst)) # 리스트에 들어있는 모든 요소를 int(정수)로 변환 
print(list)

print(*lst)   # *언패킹. 원소들을 하나씩 꺼낸다



#2 ############################################
lst = []

for x in range(5):
    N = input()
    lst.append(int) # int(정수)로 추가가

print(lst)
for i in lst:
    print(i, end=" ")


#3################################################
nums = [int(input()) for i in range(5)]
print(nums)
print(*nums)