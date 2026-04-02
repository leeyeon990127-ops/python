N = int(input())
#print(N)

def Numbers():
    if N > 0:
        return 'positive'
    elif N < 0:
        return 'negative'
    else:
        return 'zero'
print(Numbers())          #함수 호출 및 결과 저장
