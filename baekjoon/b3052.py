#number = list(map(int,input().split()))
#print(*number, sep="\n")

number = [int(input()) for i in range(10)]
#print(number)

print(len({n % 42 for n in number}))  #len 요소가 몇개 들어있는지를 숫자로 반황

#리스트 numbers 안에 있는 숫자(n)들을 하나씩 꺼내서,
#그 n을 42로 나눈 나머지를 구한 다음,
#그걸 중복 없는 집합({})으로 모아서,
#그 개수(len)를 화면에 보여줘(print).

#2 ################################################################################
output = set()
for i in range(10):
    inp = int(input())
    print(inp)

    output.add(int%42)
print(len(output))    