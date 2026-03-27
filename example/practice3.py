num = 3
print(num)
num += 2
print(num)
num -= 1
print(num)
num *= 2
print(num)
num /= 4
print(num)

snack = '꿀꽈배기'
print(len(snack))

print('_' * 10)

letter = "how are YOu"
print(letter.upper())
print(letter.capitalize())
print(letter.swapcase())
print(letter.split())
print(letter.lower())
print(letter.title())

# *(에스터리스트)의 의미 : 모든것

set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 4, 5, 6, 7}
print(set1)
print(set2)
#중복된 값을 허용하지 않기때문에 결과값은 {3, 4, 5, 6, 7}

set1 = {5, 7, 6, 2, 9, 0}
set2 = {3, 4, 4, 5, 6, 7}
print(set1)
print(set2)
#순서는 상관없이 그대로 출력된다

#List:[ ], 중복허용, 순서O, 수정0
#Tuple:( ), 중복허용, 순서O, 수정X
#Set: { }, 중복X, 순서X

my_list = ['오예스', '몽쉘', '초코파이']
print(my_list[0])
my_list[0] = '빅파이'
print(my_list)

my_tuple = ('오예스','몽쉘','초코파이')
print(my_tuple[1])

#set1={'다다다', '가가가', '나나나'}
#print(set1)

#set2={2345234234, 23423452536,67567567567567,8978697689789}
#print(set2)

#set3={"1","2","3","4"}
#print(set3)

my_set = {'돈까스', '보쌈', '제육덮밥'}
print(my_set)
# print(my_set[1])
# my_set[1] = '빅파이'
my_set.add('닭갈비')
print(my_set)
my_set.remove('제육덮밥')
print(my_set)
my_set.clear()
print(my_set)
del my_set