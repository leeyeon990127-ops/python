lst = []

for x in range(5):
    num = int(input())
    lst.append(num)
print(lst)

print(lst[0:3])  #슬라이싱. 123만 출력


#2 pop ######################################################################### 
lst = list()

for i in range(5):
    inp = int(input())
    lst.append(inp)

print(lst)


#3 #############################################################################
for i in range(2):
        lst.pop()
print(lst)

nums = [int(input()) for x in range(5)]
print(nums)

nums = nums[:-2]

print(nums)

