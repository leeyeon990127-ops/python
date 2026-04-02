#input().split()은 자동으로 리스트를 만듬듬
#input()으로 받은 데이터는 원래 하나의 긴 **문자열(String)**입니다. 
#하지만 뒤에 .split()을 붙이는 순간, 파이썬은 공백을 기준으로 
#문자열을 쪼개서 자동으로 리스트에 담는다.

#과정: "apple orange banana" (문자열) ➔ .split() ➔ ['apple', 'orange', 'banana'] (리스트)
#그래서 lst = []라고 미리 리스트를 만들지 않아도, split() 자체가 그 역할을 대신 해주는 것

A = input().split() 
print(A)


for x in range(len(A)-1, -1, -1):
    print(A[])

