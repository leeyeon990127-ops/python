N = int(input())
#print(N)

for x in range(-10, N+1, 1):   #(시작, 끝(바로 이전의 값), 증감 ) (-10, N+1)
    print(x, end=" ")


#2 while문 사용
n = int(input())
# print(n)
pie = -10
while pie <= n:
    print(pie, end=" ")
    pie += 1  

#3 리스트 사용
N = int(input())
lst = []
for i in range(-10, N+1):
    lst.append(i)
print(*lst)  #*는 언패킹. 리스트는 하나의 덩어리 -> 내용물을 하나씩 풀어서 함수에 전달
# ex
# lst = ['사과', '바나나', '포도']

# 1. 리스트를 그대로 출력할 경우
#print(lst)
# 결과: ['사과', '바나나', '포도']  (리스트 형태 그대로 출력됨)

# 2. 언패킹해서 출력할 경우
#print(*lst)
# 결과: 사과 바나나 포도  (리스트 안의 값들이 각각 떨어져서 출력됨)