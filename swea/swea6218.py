# 약수: 나누어서 0으로 떨어지면 약수이다다
n = int(input())

for x in range(1, n+1):
    if n % x == 0:
        print(f"{x}(은)는 {n}의 약수입니다.")